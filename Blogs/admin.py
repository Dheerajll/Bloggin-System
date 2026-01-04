from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} # adding this generates the slug based on the title
    list_display = ['title','category','author','status','is_featured']
    search_fields = ('id','title','category__category_name','status') # search field that helps find particular blog in admin panel based on given parameters
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)