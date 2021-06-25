from django.shortcuts import render, redirect

# Create your views here.
from petstagram_django.pets.forms import PetForm
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
    pet_to_like = Pets.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()
    return redirect('pet details', pet_to_like.id)


def create_pets(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm()
        
    context = {
        'form': form
    }

    return render(request, 'resources/pet_create.html', context)
