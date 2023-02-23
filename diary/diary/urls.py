from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('add_task', views.add_task),
    path('delete_task', views.delete_task),
    path('clear_tasks', views.clear_tasks),
    path('get_result', views.get_result),
    path('admin/', admin.site.urls),
    path('', views.index),
]
