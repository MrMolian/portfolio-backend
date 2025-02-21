from rest_framework import serializers
from . import models
class ProjectSerializer(serializers.ModelSerializer):
		#column1_name = serializers.UUIDField(read_only=True) #so you don't have to put it as entry
		class Meta:
				model = models.Project
				fields = '__all__'
					
				