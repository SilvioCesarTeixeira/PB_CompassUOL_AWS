Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

SELECT cdcli, nmcli, 
SUM (qtd * vrunt) AS gasto
from tbvendas t 
where status = 'Concluído'
group by nmcli
order by gasto desc
LIMIT 1;
