from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
import uuid

from PIL import Image

class Books(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  cover = models.ImageField(upload_to='covers/', blank=True)
  cover_url = models.URLField(max_length=200, blank=True, null=True)

  class Meta:
    verbose_name_plural = "Books"
    permissions = [
      ('special_status', 'Can read all books')
    ]

  def __str__(self):
    return self.title

  # def save(self, *args, **kwargs):
  #   super(Books, self).save(*args, **kwargs)
    
  #   img = Image.open(self.cover.path)  # opens the image of current instance
    
  #   if img.height > 250 and img.width > 100:
  #     output_size = (250, 100)
  #     img.thumbnail(output_size)
  #     img.save(self.cover.path)

  def get_absolute_url(self):
      return reverse("book_detail", args=[str(self.id)])
  
  

class Review(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
  review = models.CharField(max_length=255)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
      return self.review
    

