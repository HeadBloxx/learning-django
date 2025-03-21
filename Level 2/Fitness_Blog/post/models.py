from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name="tags")
    text = models.TextField()
    creation_date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        print(self.slug)
        return reverse("post-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

