from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'book'
router = DefaultRouter()
router.register(r'book', views.BookViewsets, basename=None)
urlpatterns = [

              ] + router.urls
