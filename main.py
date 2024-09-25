from utilitarios import ( cadastrar_categorias, cadastrar_transacoes, saldo_total)


#categorias

categoria_receitas= cadastrar_categorias("Salário")
categoria_compras= cadastrar_categorias("Compras")
categoria_viagens= cadastrar_categorias =("Viagens")

# Transações

cadastrar_transacoes(
    descricao= "Salário JUL/2024",
    valor= 1700,
    categoria= categoria_receitas

)

cadastrar_transacoes(
    descricao = "Compras",
    valor = 2000,
    categoria = categoria_compras
)

total= saldo_total()
print(total)