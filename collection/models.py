from django.db import models
from django.db.models import *


class Language(models.Model):
    name = CharField(max_length=50, verbose_name='Język książki')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Język książki'
        verbose_name_plural = 'Języki książek'


class Print(models.Model):
    name = CharField(max_length=50, verbose_name='Wydawnictwo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wydawnictwo'
        verbose_name_plural = 'Wydawnictwa'


class Room(models.Model):
    name = CharField(max_length=50, verbose_name='Pokój')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pokój'
        verbose_name_plural = 'Pokoje'


class Furniture(models.Model):
    name = CharField(max_length=50, verbose_name='Mebel')
    room = ForeignKey(Room, verbose_name='Pokój')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mebel'
        verbose_name_plural = 'Meble'


class Shelf(models.Model):
    name = CharField(max_length=50, verbose_name='Półka')
    furniture = ForeignKey(Furniture, verbose_name='Mebel')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Półka'
        verbose_name_plural = 'Półki'


class Book(models.Model):
    title = CharField(max_length=200, verbose_name='Tytuł')
    author = CharField(max_length=200, verbose_name='Autor')
    language = ForeignKey(Language, verbose_name='Język')
    year = IntegerField()
    print = ForeignKey(Print, verbose_name='Wydawnictwo')
    isbn = CharField(max_length=20, verbose_name='ISBN')
    translator = CharField(max_length=50, verbose_name='Tłumacz')
    image = ImageField(upload_to='uploads/', verbose_name='Okładka')
    shelf = ForeignKey(Shelf, verbose_name='Półka', help_text='Na której lerzy książka')

    def __str__(self):
        return '\"%s\" %s' % (self.title, self.author)

    class Meta:
        verbose_name = 'Książka'
        verbose_name_plural = 'Książki'
