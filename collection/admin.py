from django.contrib import admin
from collection.models import *
import nested_admin


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_editable = ['value']
    list_display = ['key', 'value']


class ShelfInline(nested_admin.NestedTabularInline):
    model = Shelf
    extra = 0
    sortable_field_name = 'position'


class FurnitureInline(nested_admin.NestedStackedInline):
    model = Furniture
    sortable_field_name = 'position'
    inlines = [ShelfInline]
    extra = 0


class BookInline(nested_admin.NestedTabularInline):
    model = Book
    extra = 0
    sortable_field_name = 'position'


@admin.register(Room)
class RoomAdmin(nested_admin.NestedModelAdmin):
    inlines = [FurnitureInline]


@admin.register(Shelf)
class ShelfAdmin(nested_admin.NestedModelAdmin):
    inlines = [BookInline]

admin.site.register(Language)
admin.site.register(Print)
#admin.site.register(Book)
#admin.site.register(Shelf)
