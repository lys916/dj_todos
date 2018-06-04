from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Todo(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	text = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text