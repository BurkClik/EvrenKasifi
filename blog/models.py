from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image

class Post(models.Model):
    CATEGORIES = (
        ('TR', 'TRAVEL'),
        ('MT', 'MOVIE-SERIES'),
        ('BK', 'BOOK'),
        ('GM', 'GAME'),
        ('CD', 'CODING'),
        ('AV', 'AVIATION'),
    )
    title = models.CharField(max_length=100, verbose_name='Başlık')
    cover_pic = models.ImageField(default='cover-default.jpg', upload_to='cover_pics')
    content = RichTextField(verbose_name="İçerik")
    categories = models.CharField(max_length=2, choices=CATEGORIES, default='TR', verbose_name='Kategoriler')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.cover_pic.path)
        if img.height > 720 or img.width > 1280:
            output_size = (720, 1280)
            img.thumbnail(output_size)
            img.save(self.cover_pic.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
