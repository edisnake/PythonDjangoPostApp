# URL file created to config 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('details/<int:post_id>', views.details, name='post_details'),
    path('new', views.create, name='create_post'),
    path('update/<int:post_id>', views.update, name='update_post'),
    path('delete/<int:post_id>', views.delete, name='delete_post')
]
