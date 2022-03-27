from django.shortcuts import redirect, render
from .forms import AutorForm
from .forms import EditoraForm
from .forms import LivroForm
from .models import Autor
from .models import Editora
from .models import Livro


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


def viewEditora(request):
    editoras = Editora.objects.all()

    context = {
        'editoras': editoras
    }
    return render(request, 'portal/editora.html', context)


def viewEditoraAdd(request):
    form = EditoraForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')

    context = {
        'form': form
    }
    return render(request, 'portal/editora_add.html', context)


def viewEditoraEdit(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)

    form = EditoraForm(request.POST or None, instance=editora)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')

    context = {
        'form': form,
        'editora': editora.id
    }
    return render(request, 'portal/editora_edit.html', context)
    
    
def viewEditoraDelete(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)
    editora.delete()

    return redirect('editora')


def viewLivro(request):
    livros = Livro.objects.all()

    context = {
        'livros': livros
    }
    return render(request, 'portal/livro.html', context)


def viewLivroAdd(request):
    form = LivroForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livro')

    context = {
        'form': form
    }
    return render(request, 'portal/livro_add.html', context)


def viewLivroEdit(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)

    form = LivroForm(request.POST or None, instance=livro)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livro')

    context = {
        'form': form,
        'livro': livro.id
    }
    return render(request, 'portal/livro_edit.html', context)
    
    
def viewLivroDelete(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()

    return redirect('livro')