from django.db import models
from django.contrib.auth.models import User
#DataFlair Models

class Book(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	author=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
	email = models.EmailField(blank = True)
	describe = models.TextField(default = 'DataFlair Django tutorials')

	def __str__(self):
		return self.name
