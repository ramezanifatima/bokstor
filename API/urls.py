from django.urls import path
from . import views
urlpatterns =[
    path('list', views.CustomerListView.as_view(), name='CustomerList'),
    path('detaillist/<int:pk>/', views.BookDetailView.as_view(), name='CustomerList'),
]