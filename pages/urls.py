from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('edit/<int:id>', views.edit, name='edit'),
    
]
