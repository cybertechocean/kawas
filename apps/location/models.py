import uuid
from django.db import models


class OpeningHours(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.PositiveSmallIntegerField(choices=DAY_CHOICES, unique=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_closed = models.BooleanField(default=False)
    note = models.CharField(max_length=100, blank=True, help_text="e.g. 'Closes at Midnight on Weekends'")

    class Meta:
        ordering = ['day']
        verbose_name = "Opening Hours"
        verbose_name_plural = "Opening Hours"

    def __str__(self):
        if self.is_closed:
            return f"{self.get_day_display()}: Closed"
        return f"{self.get_day_display()}: {self.open_time.strftime('%I:%M %p')} – {self.close_time.strftime('%I:%M %p')}"
