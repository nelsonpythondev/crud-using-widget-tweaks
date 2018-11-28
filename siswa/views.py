from django.shortcuts import render, redirect
from .models import Siswa
from .forms import SiswaForm

def index(request):

    return render(request, 'home.html', {})

def siswa_view(request):
    title = 'List of Siswa'
    siswas = Siswa.objects.order_by('id')

    return render(request, 'siswa.html', {'siswas': siswas, 'title': title})

def add_siswa(request):
    title = 'Add Siswa'
    form = SiswaForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        male = form.cleaned_data['male']
        address = form.cleaned_data['address']

        Siswa.objects.create(name=name, male=male, address=address).save()

        return redirect('list-siswa')


    return render(request, 'form-siswa.html', {'form': form, 'title': title})

def edit_siswa(request, id=None):
    title = 'Edit Siswa'
    siswaSingle = Siswa.objects.get(id=id)
    form = SiswaForm(request.POST or None)
    edit = True

    if form.is_valid():
        siswaSingle.name = form.cleaned_data['name']
        siswaSingle.male = form.cleaned_data['male']
        siswaSingle.address = form.cleaned_data['address']

        siswaSingle.save()

        return redirect('list-siswa')

    return render(request, 'form-siswa.html', {'title': title, 'siswaSingle': siswaSingle, 'form': form, 'edit': edit})

def delete_siswa(request, id=None):
    siswaSingle = Siswa.objects.get(id=id)

    siswaSingle.delete()
    return redirect('list-siswa')
