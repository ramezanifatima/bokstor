from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'API'
router = DefaultRouter()
router.register(r'Book', views.BookViewsets, basename=None)
urlpatterns = [

]+router.urls
