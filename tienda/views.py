from django.shortcuts import render
from .models import Producto   


# Create your views here.
def productos(request):
    productos = Producto.objects.filter(cantidad__gt = 0)
    return render(request, 'productos.html', {})
    # return HttpResponse("Hola Johnsito")