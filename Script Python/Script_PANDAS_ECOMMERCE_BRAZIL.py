import pandas as pd

#==================== Carregamento de dados ====================

payments = pd.read_csv("olist_order_payments_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")
translation = pd.read_csv("product_category_name_translation.csv")

#==================== Tratamento de dados ====================

# Agrupar pela modalidade de pagamento e somar os valores
total_pagamento_modalidade2 = (
    payments
    .groupby(["payment_type"])  #Nome da coluna contendo ID do pedido e método de pagamento
    ["payment_value"]         #Nome da coluna que contém o valor da transação 
    .sum()
    .round(2)
    .reset_index()
)

#Total de vendedores por Cidade e Estado
vendedores_por_local= (
    sellers
    .groupby(["seller_state","seller_city"])
    ["seller_id"]
    .nunique()  #Contagem distinta
    .reset_index(name="total_vendedores")
    .sort_values(by="total_vendedores", ascending=False)
)

#Total de produtos por categoria
categoria_produtos = (
    products
    .groupby(["product_category_name"])  # <-- COLOQUE AQUI O NOME REAL DA COLUNA DA CATEGORIA
    ["product_id"]
    .nunique()
    .reset_index(name="total_produtos")
)

#Cidade/Estado com maior e menor Nº de compradores
compradores_por_cidade = (
    customers
    .groupby("customer_city")  
    ["customer_unique_id"]            
    .nunique()
    .reset_index()
)

compradores_por_cidade.columns = ["cidade", "total_compradores"]  #Váriavel usada para renomear as novas colunas com os devidos valores 

# cidade com MAIS compradores
cidade_mais_compradores = compradores_por_cidade.sort_values(
    by="total_compradores",
    ascending=False
).head(1)

# cidade com MENOS compradores
cidade_menos_compradores = compradores_por_cidade.sort_values(
    by="total_compradores",
    ascending=True
).head(1)

#Tips:"False"=Decrescente , "True"=Crescente  / "head(1)"= O 1º valor

# CONTAGEM DE COMPRADORES POR ESTADO
compradores_por_estado = (
    customers
    .groupby("customer_state")  
    ["customer_unique_id"]          
    .nunique()
    .reset_index()
)

compradores_por_estado.columns = ["estado", "total_compradores"]   #Váriavel usada para renomear as novas colunas com os devidos valores 

# estado com MAIS compradores
estado_mais_compradores = compradores_por_estado.sort_values(
    by="total_compradores",
    ascending=False
).head(1)

# estado com MENOS compradores
estado_menos_compradores = compradores_por_estado.sort_values(
    by="total_compradores",
    ascending=True
).head(1)

#Resultados

print("Cidade com mais compradores:")
print(cidade_mais_compradores)

print("\nCidade com menos compradores:")
print(cidade_menos_compradores)

print("\nEstado com mais compradores:")
print(estado_mais_compradores)

print("\nEstado com menos compradores:")
print(estado_menos_compradores)



#========== Principais Insights ==========
#Merge de tabelas:

# produtos + categorias traduzidas
products_translation = pd.merge(
    products,
    translation,
    on="product_category_name",
    how="left"
)

# order_items + produtos
items_products = pd.merge(
    order_items,
    products_translation,
    on="product_id",
    how="left"
)

#Tips: "on"=Coluna que conecta as duas tabelas,"how": Quais dados de qual tabela devem prevalecer mesmo que não haja correspondências
#Os merges foram feitos em etapas pois não existe 1 coluna que conecta as 3 tabelas ao mesmo tempo
#O dataframe "items_products" contém as 3 tabelas relacionadas

#Faturamento p/ categoria
vendas_categoria2 = (
    items_products
    .groupby("product_category_name")["price"]
    .sum()
    .round(2)
    .reset_index(name="faturamento_total")
)

top_categorias2 = vendas_categoria2.sort_values(
    by="faturamento_total",
    ascending=False
).head(10)


#==================== Salvando os Dataframes ==================== 
total_pagamento_modalidade2.to_csv(
    "pagamento_por_modalidade2.csv",
    sep=";",       # separador de colunas
    decimal=",",   # separador decimal
    index=False
)

vendedores_por_local.to_csv("vendedores_por_localizacao.csv", index=False)

categoria_produtos.to_csv("produtos_por_categoria.csv", index=False)

cidade_mais_compradores.to_csv("cidade_com_mais_compradores.csv", index=False)

cidade_menos_compradores.to_csv("cidade_com_menos_compradores.csv", index=False)

vendas_categoria2.to_csv(
    "faturamento_por_categoria2.csv",
    sep=";",       # separador de colunas
    decimal=",",   # separador decimal
    index=False
)

top_categorias2.to_csv("top_10_categorias_faturamento2.csv",
    sep=";",       # separador de colunas
    decimal=",",   # separador decimal
    index=False
)
