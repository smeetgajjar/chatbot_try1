from __future__ import unicode_literals

from django.db import models
import django.utils.timezone

# Create your models here.
class chats(models.Model):

	chat_id = models.CharField(max_length=200)
	text = models.CharField(max_length=200, null=True, blank=True)
	created_date = models.DateTimeField(default=django.utils.timezone.now)



	def __unicode__(self):
		return self.text + ' ' + self.chat_id
