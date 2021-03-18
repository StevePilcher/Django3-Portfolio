from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True, blank=False)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='projects/media/images/',
                              height_field=None,
                              width_field=None,
                              max_length=100)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

