from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=36)
	# blank = True, null=False, unique=True, default='', choices='' -> one of possible options
	descriptions = models.TextField(max_length=256, blank=True)
	prices = models.DecimalField(default=0, max_digits=4, decimal_places=2)
	published = models.DateField(auto_now=True)
	covers = models.ImageField(upload_to='covers/', blank=True)


