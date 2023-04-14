from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

options = {
    ('draft','Draft'),
    ('publish','Publish'),
}

class ProductDestination (models.Model):
    title = models.CharField(max_length=500, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=500, unique=True)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images' )
    offer = models.BooleanField()
    option = models.CharField(max_length=100, choices=options, default='draft')
    
    def __str__(self):
        return self.title