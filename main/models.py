from django.db import models
# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    date = models.DateField()
    img_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    review = models.TextField()
    img_url = models.URLField(null=True)

    def __str__(self):
        return self.name