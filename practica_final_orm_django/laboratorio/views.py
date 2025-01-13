from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Laboratorio
from .forms import LaboratorioForm

def lista_laboratorios(request):
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/lista_laboratorios.html', {'laboratorios': laboratorios, 'visit_count': visit_count})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/form_laboratorio.html', {'form': form})

def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.nombre = request.POST.get('nombre')
        laboratorio.ciudad = request.POST.get('ciudad')
        laboratorio.pais = request.POST.get('pais')
        laboratorio.save()
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/editar_laboratorio.html', {'laboratorio': laboratorio})

def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('lista_laboratorios')
    return render(request, 'laboratorio/confirmar_eliminar.html', {'laboratorio': laboratorio})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


