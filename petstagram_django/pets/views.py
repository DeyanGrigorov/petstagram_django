from django.shortcuts import render, redirect

# Create your views here.
from petstagram_django.common.forms import CommentForm
from petstagram_django.common.models import Comment
from petstagram_django.pets.forms import PetForm, EditPetForm
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
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),

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
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm()

    context = {
        'form': form
    }

    return render(request, 'resources/pet_create.html', context)


def pet_comment(request, pk):
    pet = Pets.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['comment'],
            pet=pet,
        )
        comment.save()
    return redirect('pet details', pet.id)


def edit_pets(request, pk):
    pet = Pets.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = PetForm(instance=pet)

    context = {
        'form': form
    }

    return render(request, 'resources/pet_edit.html', context)


def delete_pets(request, pk):
    pet = Pets.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')

    else:
        context = {
            'pet': pet,
        }
        return render(request, 'resources/pet_delete.html', context)
