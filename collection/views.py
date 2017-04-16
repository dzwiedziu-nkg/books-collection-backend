from rest_framework import viewsets
from collection.serializers import *


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    search_fields = ('name',)


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    filter_fields = ('room',)
    search_fields = ('name',)


class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    filter_fields = ('furniture',)
    search_fields = ('name',)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('shelf',)
    search_fields = ('name',)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PrintViewSet(viewsets.ModelViewSet):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer
    search_fields = ('name',)
