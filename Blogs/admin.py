from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} # adding this generates the slug based on the title


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)