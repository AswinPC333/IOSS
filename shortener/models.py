from django.db import models
import string, random
from datetime import timedelta
from django.utils import timezone

class URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)  # 👈 expiry date

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(days=7)  # default 7 days
        super().save(*args, **kwargs)

    def generate_short_code(self, length=6):
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choice(chars) for _ in range(length))
            if not URL.objects.filter(short_code=code).exists():
                return code

    def is_expired(self):
        return self.expiry_date and timezone.now() > self.expiry_date

    def __str__(self):
        return f"{self.short_code} → {self.long_url}"
