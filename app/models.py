from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField

# Create your models here.

User = get_user_model()

class Author(models.Model):
	user    = models.OneToOneField(User,on_delete=models.CASCADE)
	profile = models.ImageField()

	def __str__(self):
		return self.user.username

class Category(models.Model):
	title      = models.CharField(max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name  		= 'Category'
		verbose_name_plural = 'Categories'

class Post(models.Model):
	title      = models.CharField(max_length=100)
	content    = HTMLField('Content') # content    = models.TextField()	
	timestamp  = models.DateTimeField(auto_now_add=True)
	views_count= models.IntegerField()
	comments   = models.IntegerField(default=0)
	thumbnail  = models.ImageField()
	author     = models.ForeignKey(Author, on_delete=models.CASCADE)
	categories = models.ManyToManyField(Category)
	featured   = models.BooleanField()

	def __str__(self):
		return self.title