from __future__ import unicode_literals

from django.db import models

import datetime

# Set up the database 

# Creates a db table with two columns:
# First column is auto generated unique integer id
# And a 250 VARCHAR column called "title". 
# This column is unique to insure no duplication of tasks

class List(models.Model):
	title = models.CharField(maxlength=250, unique=True)
	# Return to do list title by calling the objects __str__ method
	def __str__(self):
		return self.title
	# Set options in the "Meta" class e.g. the db is ordered by title
	class Meta:
		ordering = ['title']
	# Set options for Django's admin interface, pass uses default settings
	class Admin:
		pass

PRIORITY_CHOICES = (
	(1, 'low'),
	(2, 'Normal'),
	(3, 'High'),

)
# The item's priority is stored as an integer but uses the PRIORITY_CHOICES list to specify
# names that correspond to each value

# created_date is a DATETIME column in the db which will return the current date and time
class Item(models.Model):
	title = models.CharField(maxlength=250)
	created_date = models.DateTimeField(default=datetime.datetime.now)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
	completed = models.BooleanField(default=False)
	todo_list = models.ForeignKey(list)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-priority', 'title']
	class Admin:
		pass
























