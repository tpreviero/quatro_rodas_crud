from django.db import models

class Produto(models.Model):
    
    nome = models.CharField('Nome', max_length=50, blank=False)
    descricao = models.CharField('Descrição do Produto', max_length=128, blank=False)
    preco = models.DecimalField('Preço', max_digits=18, decimal_places=2, blank=False)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50, blank=False)
    email = models.EmailField('Email', unique=True, blank=False)
    telefone = models.CharField('Telefone', max_length=11)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Pedido(models.Model):

    id = models.AutoField('Pedido', primary_key=True)
    cliente = models.ForeignKey('app.Cliente', on_delete=models.CASCADE)
    produto = models.ManyToManyField('app.Produto')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def list_produtos(self):
        return ', '.join([ produto.nome for produto in self.produto.all()[:5] ])
    list_produtos.short_description = 'Produtos'
    list_produtos.allow_tags = True

    class Meta:
        ordering = ['id']

    def __str__(self):
        return 'Pedido {}'.format(self.id)
    