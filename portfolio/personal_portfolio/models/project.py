from django.db import models
from django.contrib.auth.models import User

STATUS = [
    (0, "DRAFT"),
    (1, "PUBLISHED"),
]

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    github_link = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title