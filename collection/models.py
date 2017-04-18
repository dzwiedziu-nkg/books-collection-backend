from django.db import models
from django.db.models import *


class Config(models.Model):
    KEY_VALUES = (
        ('BRAND_TITLE', 'BRAND_TITLE'),
        ('ROOM_COLS', 'ROOM_COLS')
    )

    KEY_VALUES_DEFAULTS = (
        ('BRAND_TITLE', 'Kolekcja książek'),
        ('ROOM_COLS', '2'),
    )

    key = CharField(max_length=50, primary_key=True, choices=KEY_VALUES, verbose_name='Opcja')
    value = CharField(max_length=255, verbose_name='Wartość')

    def __str__(self):
        return '%s = %s' % (self.key, self.value)

    @staticmethod
    def init_defaults():
        for d in Config.KEY_VALUES_DEFAULTS:
            o = Config.objects.filter(key=d[0])
            if o.count() == 0:
                c = Config()
                c.key = d[0]
                c.value = d[1]
                c.save()

    class Meta:
        verbose_name = 'Opcja'
        verbose_name_plural = 'Opcje'
        ordering = ['key']


class Language(models.Model):
    name = CharField(max_length=50, verbose_name='Język książki')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Język książki'
        verbose_name_plural = 'Języki książek'
        ordering = ['name']


class Print(models.Model):
    name = CharField(max_length=50, verbose_name='Wydawnictwo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wydawnictwo'
        verbose_name_plural = 'Wydawnictwa'
        ordering = ['name']


class Room(models.Model):
    name = CharField(max_length=50, verbose_name='Pokój')
    position = IntegerField(default=0)
    cols = IntegerField(default=2)
    colspan = IntegerField(default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            max = self.position = Room.objects.all().aggregate(Max('position'))
            if max and 'position__max' in max:
                self.position = max['position__max'] + 1
            else:
                self.position = 0
        super(Room, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Pokój'
        verbose_name_plural = 'Pokoje'
        ordering = ['name']


class Furniture(models.Model):
    name = CharField(max_length=50, verbose_name='Mebel')
    room = ForeignKey(Room, verbose_name='Pokój')
    position = IntegerField(default=0)
    cols = IntegerField(default=4)
    colspan = IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mebel'
        verbose_name_plural = 'Meble'
        ordering = ['room', 'name']


class Shelf(models.Model):
    name = CharField(max_length=50, verbose_name='Półka')
    furniture = ForeignKey(Furniture, verbose_name='Mebel')
    position = IntegerField(default=0)
    cols = IntegerField(default=4)
    colspan = IntegerField(default=1)

    def __str__(self):
        return '%s - %s - %s' % (self.furniture.room.name, self.furniture.name, self.name)

    class Meta:
        verbose_name = 'Półka'
        verbose_name_plural = 'Półki'
        ordering = ['furniture', 'position']


class Book(models.Model):
    title = CharField(max_length=200, verbose_name='Tytuł')
    original_title = CharField(max_length=200, verbose_name='Tytuł oryginału')
    author = CharField(max_length=200, verbose_name='Autor')
    language = ForeignKey(Language, verbose_name='Język')
    year = IntegerField(verbose_name='Rok wydania')
    print = ForeignKey(Print, verbose_name='Wydawnictwo')
    isbn = CharField(max_length=20, verbose_name='ISBN')
    translator = CharField(max_length=50, verbose_name='Tłumacz')
    image = ImageField(upload_to='uploads/', verbose_name='Okładka')
    shelf = ForeignKey(Shelf, verbose_name='Półka', help_text='Na której lerzy książka')
    dedication = BooleanField(default=False, verbose_name='Dedykacja')
    position = IntegerField(default=0)

    def __str__(self):
        return '\"%s\" %s' % (self.title, self.author)

    class Meta:
        verbose_name = 'Książka'
        verbose_name_plural = 'Książki'
        ordering = ['title']
