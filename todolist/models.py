from django.db import models
from datetime import datetime
from django.conf import settings

PRIORITY_CHOICES = (
	("URGENT","Urgent"),
	("NORMAL","Normal"),
)
FINISHED_CHOICES = (
	("COMPLETE","Complete"),
	("INCOMPLETE","Incomplete"),
)
class Item(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=100)
	text = models.TextField()
	begin = models.DateTimeField(default=datetime.now,blank=True)
	end = models.DateTimeField(default=datetime.now)
	priority = models.CharField(max_length=6,choices=PRIORITY_CHOICES,default="NORMAL")
	finished = models.CharField(max_length=10,choices=FINISHED_CHOICES,default="INCOMPLETE")
	
	def __unicode__(self):
		return self.title
# Create your models here.
