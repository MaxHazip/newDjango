from newApp import views
from django.urls import path

urlpatterns = [
    path('main-page/', views.Page.as_view()),
    path('author/<int:pk>', views.Author.as_view()),
]