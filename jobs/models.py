from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    posted = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)  # store as comma-separated string
    link = models.URLField(unique=True)  # prevent duplicates
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
