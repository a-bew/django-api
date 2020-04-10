from rest_framework import serializers
from courses.models import Course

# Create your models here.
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'language', 'price')
