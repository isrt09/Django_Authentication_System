from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Author(models.Model):
	user    = models.OneToOneField(User, on_delete=models.CASCADE)
	photo   = models.ImageField()

	def __str__(self):
		return self.user.username

class Category(models.Model):
	title  = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Post(models.Model):
	title     	   = models.CharField(max_length=100)
	content   	   = models.TextField()
	timestamp 	   = models.DateField(auto_now_add=True)
	comment_counts = models.IntegerField(default=0)
	thumnail       = models.ImageField()
	author		   = models.ForeignKey(Author,        on_delete=models.CASCADE)
	category	   = models.ManyToManyField(Category)
	featured 	   = models.BooleanField()

	def __str__(self):
		return self.title