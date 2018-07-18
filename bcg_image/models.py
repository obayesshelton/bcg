from django.db import models
import os

class Image(models.Model):

  image = models.FileField(blank=False, null=False)
  name = models.CharField(max_length=120)
  extension = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):

    if self.image.name.endswith(".jpg"):
      self.extension = 'jpg'

    elif self.image.name.endswith(".png"):
      self.extension = 'png'

    elif self.image.name.endswith(".pdf"):
      self.extension = 'pdf'

    return super(Image, self).save(*args, **kwargs)
