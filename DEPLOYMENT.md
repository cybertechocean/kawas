# KAWA'S Café — cPanel Deployment Guide
## Host: Hostnali · Domain: kawas.co.ke · Server: LiteSpeed

---

## Prerequisites Checklist

- [ ] cPanel login credentials from Hostnali welcome email
- [ ] SSH access enabled (cPanel → SSH Access)
- [ ] SSL certificate issued (cPanel → SSL/TLS → AutoSSL)
- [ ] Cloudinary credentials ready (CLOUD_NAME, API_KEY, API_SECRET)
- [ ] A strong Django SECRET_KEY generated (use: `python -c "import secrets; print(secrets.token_hex(50))"`)

---

## Step 1 — Upload the Project

**Option A — cPanel File Manager (easiest)**
1. Open cPanel → File Manager → navigate to `public_html/`
2. Delete the default `index.html` if present
3. Upload the entire project as a ZIP → Extract here
4. Your files should sit at: `/home/<cpanelusername>/public_html/`
   - `manage.py`, `passenger_wsgi.py`, `.htaccess`, `kawas/`, `apps/`, etc.

**Option B — FTP**
Upload via FileZilla to the same `public_html/` path.

**Option C — SSH + Git**
```bash
ssh <cpanelusername>@kawas.co.ke
cd public_html
git clone https://github.com/<yourrepo>/kawas-website.git .
```

---

## Step 2 — Set Up Python App (cPanel)

1. cPanel → **Setup Python App** → **Create Application**
2. Fill in:
   - **Python version:** 3.12 (or latest available)
   - **Application root:** `public_html` (or the subdirectory where you uploaded)
   - **Application URL:** `kawas.co.ke`
   - **Application startup file:** `passenger_wsgi.py`
   - **Application Entry point:** `application`
3. Click **Create** — cPanel creates a virtual environment automatically.
4. Copy the path shown for your virtualenv (e.g. `/home/<user>/virtualenv/public_html/3.12/`).

---

## Step 3 — Install Python Dependencies

In cPanel → Setup Python App → click **"Enter to the virtual environment"** or SSH:

```bash
source /home/<cpanelusername>/virtualenv/public_html/3.12/bin/activate
cd ~/public_html
pip install -r requirements.txt
```

---

## Step 4 — Set Environment Variables

In cPanel → Setup Python App → **Environment variables**, add each one:

| Variable | Value |
|---|---|
| `DJANGO_SETTINGS_MODULE` | `kawas.settings` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `kawas.co.ke,www.kawas.co.ke` |
| `SESSION_SECRET` | `<your-generated-secret-key>` |
| `CLOUDINARY_CLOUD_NAME` | `<your-cloudinary-cloud-name>` |
| `CLOUDINARY_API_KEY` | `<your-cloudinary-api-key>` |
| `CLOUDINARY_API_SECRET` | `<your-cloudinary-api-secret>` |

> ⚠️ Never put actual secret values in any file committed to git. Only set them here.

---

## Step 5 — Run Django Setup Commands

SSH into the server and activate the virtualenv:

```bash
source /home/<cpanelusername>/virtualenv/public_html/3.12/bin/activate
cd ~/public_html

# Apply database migrations
python manage.py migrate

# Collect all static files into staticfiles/
python manage.py collectstatic --noinput

# Seed the database with menu items, categories, FAQs, etc.
python seed_data.py

# Create your admin superuser
python manage.py createsuperuser
```

---

## Step 6 — Verify SSL & Restart

1. cPanel → **SSL/TLS** → **AutoSSL** → run if certificate not yet issued
2. cPanel → **Setup Python App** → click **Restart** on your app
3. Visit **https://kawas.co.ke** — the site should be live

---

## Step 7 — Verify Everything Works

| Check | URL |
|---|---|
| Home page | https://kawas.co.ke/ |
| Menu | https://kawas.co.ke/menu/ |
| Gallery | https://kawas.co.ke/gallery/ |
| Contact | https://kawas.co.ke/contact/ |
| Admin | https://kawas.co.ke/kawas_admin/ |
| Sitemap | https://kawas.co.ke/sitemap.xml |

---

## Step 8 — Test Image Uploads (Cloudinary)

1. Log into `/kawas_admin/`
2. Open **Menu Items** → choose any item → upload a photo → Save
3. Check your Cloudinary dashboard — the image should appear in `menu/`

---

## Database

The project uses **SQLite by default** (`db.sqlite3` in the project root).

> For shared hosting, SQLite is perfectly fine for a café website with this traffic level.
> If you later need MySQL/PostgreSQL (available on cPanel), update the `DATABASES` setting
> in `settings.py` and re-run `python manage.py migrate`.

---

## Email Configuration (Optional)

To send emails from `info@kawas.co.ke` via cPanel mail server, add to environment variables:

| Variable | Value |
|---|---|
| `EMAIL_HOST` | `mail.kawas.co.ke` |
| `EMAIL_PORT` | `587` |
| `EMAIL_HOST_USER` | `info@kawas.co.ke` |
| `EMAIL_HOST_PASSWORD` | `<your-email-password>` |
| `EMAIL_USE_TLS` | `True` |
| `DEFAULT_FROM_EMAIL` | `KAWA'S Café <info@kawas.co.ke>` |

---

## Troubleshooting

**500 error on first visit**
- Check the Passenger error log: cPanel → Error Logs
- Most common cause: missing environment variable or failed `pip install`

**Static files not loading (CSS/JS missing)**
- Run `python manage.py collectstatic --noinput` again
- Verify `staticfiles/` directory was created in your project root

**Admin shows unstyled page**
- Same as above — collectstatic must be run after every deployment

**Database errors**
- Run `python manage.py migrate` again

---

## Updating the Site After Changes

```bash
# SSH into server
cd ~/public_html
git pull origin main           # if using git

# After any code change:
python manage.py migrate       # if models changed
python manage.py collectstatic --noinput

# Restart the Python app
# cPanel → Setup Python App → Restart
```
