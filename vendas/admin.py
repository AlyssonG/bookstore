from django.contrib import admin
from .models import Categoria, Produto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Categoria, CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria', 'preco', 'estoque', 'disponivel', 'data_cadastramento', 'data_atualizacao']
    list_filter = ['disponivel', 'data_cadastramento', 'categoria']
    list_editable = ['preco', 'estoque', 'disponivel']
    search_fields = ['nome', 'categoria', 'disponivel', 'data_cadastramento']
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('data_cadastramento',)


admin.site.register(Produto, ProdutoAdmin)
