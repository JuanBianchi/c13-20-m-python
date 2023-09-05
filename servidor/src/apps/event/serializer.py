from rest_framework import serializers
from .models import Event, Category
from django.shortcuts import get_object_or_404

# Categoria Seriliazer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Event
        fields = ('id','eventHost','name','description','capacity','date','created_at','virtual','state','ticketPrice','event_images','categories','location')
        read_only_fields = ('created_at', 'eventHost',) 

    def create(self, validated_data):

        validated_data['eventHost'] = self.context['request'].user
        
        # Toma las categorías a partir de los IDs que vienen del request
        category_ids = validated_data.pop('categories', [])  # Obtén la lista de IDs directamente

        categories = [get_object_or_404(Category, id=category_id) for category_id in category_ids]

        event = Event.objects.create(**validated_data)
        event.categories.set(categories)
        event.save()
        return event


# Evento detalle sin categorias con id y nombre
class EventDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        exclude = ['created_at']
        read_only_fields = ('id','eventHost')

