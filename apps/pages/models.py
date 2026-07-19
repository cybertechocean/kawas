import uuid
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class FAQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=300)
    answer = CKEditor5Field(config_name='default')
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordering', 'created_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question[:80]


class PrivacyPolicy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = CKEditor5Field(config_name='extends')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"

    def __str__(self):
        return "Privacy Policy"

    def save(self, *args, **kwargs):
        self.pk = self.pk or uuid.uuid4()
        super().save(*args, **kwargs)


class TermsOfService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = CKEditor5Field(config_name='extends')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Terms of Service"
        verbose_name_plural = "Terms of Service"

    def __str__(self):
        return "Terms of Service"
