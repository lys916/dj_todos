from rest_framework import serializers
from .models import Todo

# serialize Todo model / turn the fiels to json format
#  serializers.HyperlinkedModelSerializer ?? ModelSerializer
class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'text', 'user')

		