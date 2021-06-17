from django.shortcuts import render, redirect

# Create your views here.
from petstagram_django.pets.models import Pets, Like


def list_pets(request):
    all_pets = Pets.objects.all()

    context = {
        'pets': all_pets
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pets.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count

    context = {
        'pet': pet
    }

    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet = Pets.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()
    return redirect('list pets')
