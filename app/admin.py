from django.contrib import admin
from app.models import *

class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'descricao', 'preco']
    search_fields = ['nome', 'descricao', 'preco']

class ClienteAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'email', 'telefone']
    search_fields = ['nome', 'email', 'telefone']

class PedidoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'cliente', 'list_produtos', 'created')
    search_fields = ['produto__nome', 'cliente__nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)