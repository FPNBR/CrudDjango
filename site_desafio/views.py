from django.shortcuts import redirect, render
from .forms import AutorForm
from .models import Autor


def viewHome(request):
    return render(request, 'portal/home.html')
    

def viewAutor(request):
    autores = Autor.objects.all()

    context = {
        'autores': autores
    }
    return render(request, 'portal/autor.html', context)


def viewAutorAdd(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form
    }
    return render(request, 'portal/autor_add.html', context)


def viewAutorEdit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form,
        'autor': autor.id
    }
    return render(request, 'portal/autor_edit.html', context)
    
    
def viewAutorDelete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()

    return redirect('autor')


