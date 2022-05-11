from django.contrib import admin
from django.forms import SlugField

from bloggy.models import phone, phoneCategory

# Register your models here.

@admin.register(phoneCategory)
class phoneCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)



@admin.register(phone)
class phoneAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ( "name", )}