# Instruções:

- Tabela dim_produto
A partir da tabela normalizada, foi duplicada uma cópia, após isso,  Transformar dados/ Home/Group BY/Advanced selecionando as seguintes opções:

===================================
Nome da Coluna - Operação - Coluna
===================================
Contagem - SUM - Units sold
Valor mínimo de venda - MIN - Sale Price 
Valor máximo de venda - MAX - Sale Price
Média do valor de vendas - AVERAGE - Sale Price
Mediana do valor de vendas - MEDIAN - Sale Price
Média de manufatura - AVERAGE - Manufacturing Price

Após isso foi incluída uma coluna referindo-se ao índice de cada produto, para isto, basta ir até a aba
Add Column/ Index Column;


- Tabela dim_descontos
A partir da tabela normalizada, foi duplicada uma cópia, após isso, será necessário utilizar os ID's dos produtos classificados na tabela anterior, para isso, 
foi feita uma junção de tabelas e então retornando somente a coluna Index que nos interessa, para isto vá em Home/Merge Queries faça a relação através da coluna 'Product'
(nome do produto) após a junção, clique no ícone na nova coluna e selecione somente a coluna retornada da relação 'Index', renomeie ela de 'dim_produto.Index' para 'Index';


- Tabela dim_categoria
A partir da tabela normalizada, foi duplicada uma cópia, após isso, foram mantidas somente as colunas 'Segment' e 'Country', após isso, selecione somente as duas colunas
clique com o botão direito do mouse e selecione 'Remove Duplicates', após isso vá na aba Add Column e clique em Index Column;


- Tabela dim_produto_detalhes
A partir da tabela normalizada, foi duplicada uma cópia, após isso, foram mantidas somente as colunas 'Product', 'Discount Band', 'Units Sold', 'Manufacturing Price', 'Sale Price'.
, após isso vá na aba Add Column e clique em Index Column, será necessário retornar o índice de cada produto, para isto vamos utilizar o mesmo recurso anteriormente utilizado, 
'Merge Queries' deixando somente a coluna 'Index' de produtos, renomeie esta nova coluna para 'Index Produto' para evitar possíveis confusões;

- Tabela fato_produto
A partir da tabela normalizada, foi duplicada uma cópia, após isso, será necessário retornar o índice do produto, para isto vá 
'Merge Queries' seleciona a tabela produto, faça o cruzamento a partir do nome do produto, 
após esse processo, deixe somente a coluna 'Index' de produtos, renomeie esta nova coluna para 'Index Produto' para evitar possíveis confusões.
Adicione um index para cada registro de venda em Add Column e clique em Index Column, renomeie para 'SK_ID', remova as colunas desnecessárias:
'Manufacturing price', 'COGS' e 'Month number'.
Após isto deverá ser criada uma forte chave que identifique que cada transação é única, para isto, foi criada uma coluna de exemplo concatenando as seguintes colunas:
Product-Country-Segment-Sales;


- Tabela dim_desconto
A partir da tabela normalizada, foi duplicada uma cópia, e então foi criada uma chave única para servir como ID da venda, para isto foi criada uma coluna de exemplo
concatenando os seguintes campos: Product-Country-Segment-Sales, esta chave servirá como chave para cruzamento com a tabela 'fato_produto' podendo retornar o desconto
para uma exata transação, por isso a relação deverá ser de 1:1.




