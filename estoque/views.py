from django.shortcuts import render, HttpResponse
from .models import Categoria, Produto
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

def estoque(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        produtos = Produto.objects.all()
        return render(request, 'estoque/estoque.html', {'categorias': categorias, 'produtos':produtos})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = int(request.POST.get('quantidade'))
        custo_producao = float(request.POST.get('custo_producao'))
        valor_venda = float(request.POST.get('valor_venda'))
    
        produto = Produto(nome=nome, categoria_id=categoria, quantidade=quantidade, 
                          custo_producao=custo_producao, valor_venda=valor_venda)
        
        produto.save()

        return redirect(reverse('estoque'))