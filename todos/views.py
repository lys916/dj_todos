from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.
class TodoView(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	def get_queryset(self):
		print('PRINT user', self.request.user)
		user = self.request.user

		if user.is_anonymous:
			return Todo.objects.none()
		else:
			return Todo.objects.filter(user=user)