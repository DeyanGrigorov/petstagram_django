from django.urls import path

from petstagram_django.common import views

urlpatterns = [
    path('', views.landing_page, name='landing page')
]
