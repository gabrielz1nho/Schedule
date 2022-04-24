from django.shortcuts import render
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('-id')
    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request,'contatos/index.html',{
        'contatos': contatos

    })


def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id = contato_id)
        return render(request,'contatos/ver_contato.html',{
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()
