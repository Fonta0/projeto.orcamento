from categoria import Categoria
from transacao import Transacao

lista_categorias= []
lista_transacoes=[]

def cadastrar_categorias(nome):
    nova_categoria = Categoria(nome = nome )
    lista_categorias.append(nova_categoria)

    return nova_categoria


def cadastrar_transacoes(descricao, valor, categoria ):
    nova_transacao= Transacao(
        descricao= descricao, 
        valor= valor,
        categoria= categoria)
    lista_transacoes.append(nova_transacao)

    return nova_transacao

def saldo_total():
    total = 0 
    for t in lista_transacoes:
        total = total + t.valor

    return total




