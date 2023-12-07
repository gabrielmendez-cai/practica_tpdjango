from datetime import date

from django.shortcuts import redirect, render
from . import models
from .forms import ClienteBuscarForm




def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)


def crearClientesVarios(request):
    p1 = models.Pais(nombre="Paraguay")
    p2 = models.Pais(nombre="México")
    p3 = models.Pais(nombre="Uruguay")
    p4 = models.Pais(nombre="Chile")
    p5 = models.Pais(nombre="Argentina")
    p1.save()
    p2.save()
    p3.save()
    p4.save()
    p5.save()
    c1 = models.Cliente(nombre="Almendra", apellido="Ruiseñor", sexo = "femenino" ,nacimiento=date(2015, 1, 1), pais_origen=p1)
    c2 = models.Cliente(nombre="Giordana", apellido="Tapello", sexo = "femenino", nacimiento=date(2005, 2, 2), pais_origen=p2)
    c3 = models.Cliente(nombre="Macarena", apellido="Lito", sexo = "femenino", nacimiento=date(1990, 1, 1), pais_origen=p3)
    c4 = models.Cliente(nombre="Jorge", apellido="Perez", sexo = "masculino", nacimiento=date(2005, 1, 1), pais_origen=None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:index")



def busqueda(request):
    # búsqueda por nombre que contenga "dana"
    cliente_nombre = models.Cliente.objects.filter(nombre__contains="dana")

    # nacimientos mayores a 2000
    cliente_nacimiento = models.Cliente.objects.filter(nacimiento__gt=date(2000, 1, 1))

    # país de origen vacío (null - None)
    cliente_pais = models.Cliente.objects.filter(pais_origen=None)
    
    cliente_sexo = models.Cliente.objects.filter(sexo= "masculino")

    context = {
        "cliente_nombre": cliente_nombre,
        "cliente_nacimiento": cliente_nacimiento,
        "cliente_pais": cliente_pais,
        "cliente_sexo": cliente_sexo,
    }
    return render(request, "cliente/busqueda.html", context)

def cliente_sexo_view(request):
    if request.method == "GET":
        form = ClienteBuscarForm()
        return render (request,"cliente/busqueda.html",context={"form":form})
    else:
        pass
 
from . import forms
from .forms import ClienteForm, EstudioForm 

def crear(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        form_estudio = EstudioForm(request.POST)
        if form_cliente.is_valid() and form_estudio.is_valid():
            cliente = form_cliente.save()
            estudio = form_estudio.save(commit=False)
            estudio.cliente = cliente  # Asocia el cliente al estudio
            estudio.save()
            return redirect("cliente:index")  # Ajusta la ruta a la que deseas redirigir después de guardar
    else:
        form_cliente = ClienteForm()
        form_estudio = EstudioForm()

    return render(request, "cliente/crear.html", {"form_cliente": form_cliente, "form_estudio": form_estudio})