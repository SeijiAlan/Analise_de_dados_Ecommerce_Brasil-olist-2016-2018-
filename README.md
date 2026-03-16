# Analise_de_dados_Ecommerce_Brasil-olist-2016-2018-

Análise Exploratória de Marketplace Brasileiro – Dataset Olist

1.Introdução

   Este projeto realiza uma análise exploratória detalhada de um marketplace brasileiro utilizando o dataset público disponibilizado pela Olist. O objetivo principal foi transformar uma grande quantidade de dados brutos relacionados a pedidos, pagamentos, clientes e vendedores em informações estratégicas capazes de apoiar decisões de negócio. A proposta do projeto foi simular um fluxo de trabalho real de análise de dados, combinando programação para tratamento e preparação dos dados (Python/Pandas) com POWER BI para modelagem analítica e construção de visualizações interativas.

2.Tecnologias Utilizadas

O projeto foi desenvolvido utilizando ferramentas amplamente utilizadas no mercado de análise de dados:

2.1 Python (Pandas) – limpeza, transformação e agregação dos dados

2.2 Power BI – modelagem relacional e desenvolvimento do dashboard

2.3 DAX (Data Analysis Expressions) – criação de métricas analíticas

2.4 Git / GitHub – versionamento e documentação do projeto


3.Tratamento de Dados com Python

   Na etapa inicial do projeto foi desenvolvido um script em Python responsável pelo carregamento e tratamento das bases de dados. Ao todo foram utilizadas sete tabelas contendo informações sobre pedidos, itens vendidos, clientes, vendedores, pagamentos e categorias de produtos. Durante esse processo foram realizadas diversas operações de transformação e consolidação dos dados, garantindo que as informações estivessem estruturadas de forma adequada para análise posterior.As novas tabelas geradas se tratam de tabelas agregadas, portanto não participaram da modelagem relacional com as tabelas originais, foram utilizadas apenas para cálculo e visualização de dados. Ressalta-se que o dataset contém poucos registros sobre o ano de 2016, já em 2017 observou-se um grande aumento de registros, razão pela qual a % de crescimento ficou com um valor extremamente alto. 

Entre as principais tarefas executadas durante o tratamento dos dados estão:

3.1 Agregação e sumarização: agrupamento das transações para identificar faturamento por modalidade de pagamento e volume de produtos vendidos por categoria.

3.2 Engenharia de dados: realização de merges entre as tabelas de itens do pedido, produtos e tradução de categorias, consolidando as informações necessárias para análise de vendas.

3.3 Análise geográfica: cálculo da densidade de compradores e vendedores por cidade e estado, permitindo identificar os principais polos de atividade comercial.

Após a conclusão dessas etapas, os dados tratados foram exportados em arquivos CSV estruturados, com padronização de separadores e formatação numérica adequada para importação eficiente no Power BI.

4.Modelagem e Métricas Analíticas

  Com os dados previamente tratados em Python, a etapa de modelagem no Power BI tornou-se mais organizada e eficiente. Foram estabelecidas relações entre as tabelas principais do modelo e criada uma tabela calendário para permitir análises temporais mais robustas.
Durante essa etapa também foram desenvolvidas diversas medidas analíticas utilizando DAX, responsáveis por calcular indicadores fundamentais para análise do desempenho do marketplace.

Entre as principais métricas criadas (KPIs) estão:

-Faturamento total da plataforma

-Ticket médio por pedido

-Volume de itens vendidos

-Quantidade de vendedores por categoria

-Crescimento anual do faturamento (Year over Year)

   Um ponto importante da modelagem foi a construção do cálculo de ticket médio real, obtido a partir da divisão entre o faturamento total e a contagem distinta de pedidos. Essa abordagem garante que o valor médio represente corretamente o gasto por transação, evitando distorções causadas pela presença de múltiplos itens dentro de um mesmo pedido.

Métricas DAX desenvolvidas:
```DAX
Crescimento Último Ano (YoY) =   
VAR UltimoAno = MAX(Calendario[Ano])

RETURN

CALCULATE(
    [Crescimento YoY %],
    Calendario[Ano] = UltimoAno
) 
```

```DAX
Ticket Médio Categoria = 

DIVIDE(SUM(olist_order_items_dataset[price]),
DISTINCTCOUNT(olist_order_items_dataset[order_id]),2

)
```

```DAX
Total de pedidos realizados = DISTINCTCOUNT(olist_orders_dataset[order_id])
```

```Dax
Faturamento = SUM(olist_order_payments_dataset[payment_value])
```

5. Análise e Principais Observações

O dashboard foi estruturado com foco na clareza visual e na geração de insights estratégicos. Entre as visualizações desenvolvidas estão gráficos que mostram a evolução do faturamento ao longo do tempo, o crescimento anual da plataforma, o ranking das categorias com maior volume de vendas e a distribuição geográfica de compradores.Uma das análises mais relevantes do projeto foi o cruzamento entre o volume de vendas e a quantidade de vendedores por categoria. Essa abordagem permitiu avaliar simultaneamente o nível de demanda e o grau de concorrência dentro do marketplace.
A análise revelou padrões interessantes no comportamento do mercado. Categorias como Cama, Mesa e Banho apresentam grande volume de vendas, indicando forte demanda dentro da plataforma. Em contraste, a categoria Relógios Presentes demonstrou características de nicho estratégico, apresentando faturamento relevante e ticket médio elevado mesmo com um número relativamente reduzido de vendedores. Já o setor de Beleza e Saúde mostrou-se altamente competitivo, com grande concentração de vendedores atuando no mesmo segmento.A análise geográfica também revelou padrões importantes.

A região Sudeste concentrou a maior parte das transações do marketplace, consolidando-se como o principal polo de atividade comercial. Além disso, algumas categorias apresentaram valores médios significativamente superiores à média geral do marketplace, frequentemente ultrapassando faixas entre R$500 e R$1.000 por pedido. Em alguns casos, variações regionais sugerem que fatores logísticos e diferenças na demanda local influenciam diretamente o valor final dos produtos.

6.Conclusão

A análise demonstrou que o marketplace apresentou crescimento aproximado de 20% no faturamento entre 2017 e 2018. Esse crescimento foi impulsionado principalmente pelo aumento no volume de pedidos realizados na plataforma, enquanto o ticket médio geral permaneceu relativamente estável, situando-se em torno de R$161 por pedido. Outro ponto relevante identificado foi a predominância do cartão de crédito como principal método de pagamento, facilitando transações de maior valor e contribuindo para o aumento do faturamento total. De forma geral, este projeto demonstra como técnicas de tratamento de dados, modelagem analítica e visualização interativa podem transformar dados brutos em informações estratégicas. A análise permitiu identificar categorias com maior volume de vendas, nichos com menor concorrência, padrões regionais de consumo e oportunidades potenciais de mercado dentro do ambiente de e-commerce.
