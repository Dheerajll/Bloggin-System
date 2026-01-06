from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    #category crud
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_categories,name='add_categories'),
    path('categories/edit/<int:pk>',views.edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>',views.del_categories,name='del_categories'),

    #blog crud
    path('posts/',views.posts,name='posts'),
    path('posts/add',views.add_posts,name='add_posts'),
    path('posts/edit/<int:pk>',views.edit_posts,name='edit_posts'),
    path('posts/delete/<int:pk>',views.del_posts,name='del_posts'),
]
