from django.contrib import admin
from collection.models import *
import nested_admin


class ShelfInline(nested_admin.NestedTabularInline):
    model = Shelf
    extra = 0
    sortable_field_name = 'position'


class FurnitureInline(nested_admin.NestedStackedInline):
    model = Furniture
    inlines = [ShelfInline]
    extra = 0


@admin.register(Room)
class RoomAdmin(nested_admin.NestedModelAdmin):
    inlines = [FurnitureInline]


admin.site.register(Language)
admin.site.register(Print)
admin.site.register(Book)
