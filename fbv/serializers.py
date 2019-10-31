from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','checked', 'title', 'due_date']
        # serializers - checked, title, due_date 만 해도 괜찮은가?