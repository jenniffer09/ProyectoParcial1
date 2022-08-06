from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTESssss',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def planCuentas(request):
    data={
        'titulo': 'Plan de Cuentas'
    }
    return render(request, 'planCuentas/planCuentas.html', data)

def cuentas(request):
    data={
        'titulo': 'Gestión de Cuentas',
        'crear_url': '/crearCuenta',
    }
    return render(request, 'planCuentas/cuentas.html', data)

def crearCuenta(request):
    data={
        'titulo': 'Administrador de cuentas',
        'crear_url':'/crearCuenta',
        'action': 'add',
    }
    return render(request, 'planCuentas/formCuentas.html', data)

def tipocuenta(request):
    data={
        'titulo': 'TIPO DE CUENTAS',
        'crear_url': '/crearTipoCuenta',
        'action': 'add'
    }
    return render(request, 'planCuentas/tipocuenta.html', data)

def crearTipoCuenta(request):
    data={
        'titulo': 'Cuentas Contables Clasificadas',
        'action':'add'
    }
    return render(request, 'planCuentas/formTipoCuenta.html', data)

def nivel(request):
    data={
        'titulo': 'Niveles',
        'crear_url': ' /crearNiveles',
    }
    return render(request, 'planCuentas/nivel.html', data)

def crearNiveles(request):
    data={
        'titulo': 'Administrar Nivel',
        'action' : 'add',
    }
    return render(request, 'planCuentas/formNivel.html', data)
