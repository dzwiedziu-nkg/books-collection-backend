from rest_framework import serializers
from collection.models import *


class ConfigSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(source='get_id')

    def get_id(self, obj):
        return obj.key

    class Meta:
        model = Config
        fields = ['id', 'value']


class RoomSerializer(serializers.ModelSerializer):
    furniture_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    shelf_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Furniture
        fields = '__all__'


class ShelfSerializer(serializers.ModelSerializer):
    book_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Shelf
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Print
        fields = '__all__'
