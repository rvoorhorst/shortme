from django.db import models


class URLData(models.Model):
    original_url = models.URLField(max_length=250)
    hash = models.CharField(max_length=30, unique=True)
    times_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def increase_times_used(self):
        self.times_used += 1
        self.save()

    def __str__(self):
        if len(self.original_url) < 45:
            return f"{self.original_url}"
        else:
            return f"{self.original_url[:45]}..."
