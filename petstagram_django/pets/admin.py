from django.contrib import admin

# Register your models here.
from petstagram_django.pets.models import Pets


class PetsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age', 'likes_count']

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Pets, PetsAdmin)
