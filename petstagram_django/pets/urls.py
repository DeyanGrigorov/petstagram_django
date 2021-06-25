from django.urls import path

from petstagram_django.pets.views import list_pets, pet_details, like_pet, create_pets

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='list pets'),
    path('create/', create_pets, name='create pets'),
]