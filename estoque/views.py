from django.shortcuts import render, HttpResponse
from .models import Categoria, Produto

# Create your views here.

def estoque(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'estoque/estoque.html', {'categorias': categorias})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = int(request.POST.get('quantidade'))
        custo_producao = float(request.POST.get('custo_producao'))
        valor_venda = float(request.POST.get('valor_venda'))
    
        produto = Produto(nome=nome, categoria_id=categoria, quantidade=quantidade, 
                          custo_producao=custo_producao, valor_venda=valor_venda)
        
        produto.save()

        return HttpResponse('rolou hein ')