from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
    
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('index')

def update(request, id):
    nota = Note.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        nota.title = title
        nota.content = content

        nota.save()
        return redirect('index')

    elif request.method == 'GET':
        return render(request, 'notes/update.html', {'note': nota})