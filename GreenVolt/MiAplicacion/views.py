from django.shortcuts import render,HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("""
                          <h1> Hola mundo </h1>
                       """)

def pagina(request):
    return HttpResponse("""
                          <h1> Sitio web de Greenvolt </h1>
                          <h3>Energia inteligente para un planeta sostenible</h3>
                       """)
