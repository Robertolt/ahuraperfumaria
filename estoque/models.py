from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=40, )

    def __str__(self) -> str:
        return self.titulo
    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null = True)
    quantidade = models.IntegerField()
    custo_producao = models.FloatField() #ver colocar binário
    valor_venda = models.FloatField()

    def __str__(self) -> str:
        return self.nome
    
    def gerar_desconto(self, desconto):
        return self.valor_venda - (self.valor_venda * desconto) / 100

    def lucro(self):
        lucro_em_reais = self.valor_venda - self.custo_producao
        lucro_em_porcentagem = (self.valor_venda - self.custo_producao)*100 / self.custo_producao
        return lucro_em_reais and lucro_em_porcentagem