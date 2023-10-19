--A comissão de um vendedor é definida a partir de um percentual sobre
--o total de vendas (quantidade * valor unitário) por ele realizado.
--O percentual de comissão de cada vendedor está armazenado na coluna perccomissao,
--tabela tbvendedor. 

--Com base em tais informações, calcule a comissão de todos os vendedores,
--considerando todas as vendas armazenadas na base de dados com status concluído.

--As colunas presentes no resultado devem ser vendedor,
--valor_total_vendas e comissao. O valor de comissão deve
--ser apresentado em ordem decrescente arredondado na segunda casa decimal.

with tot_vendas as (SELECT tvr.nmvdd as vendedor, 
tvr.perccomissao, 
SUM (qtd * vrunt) as valor_total_vendas
from tbvendas as tvn
left join tbvendedor as tvr
on tvn.cdvdd = tvr.cdvdd
where tvn.status = 'Concluído'
group by nmvdd)
SELECT vendedor,
valor_total_vendas,
ROUND ((valor_total_vendas * perccomissao)/100, 2) as comissao
from tot_vendas
group by vendedor
order by comissao DESC;


SELECT status from tbvendas t 

select cdvdd, perccomissao, (perccomissao * 1) / 100 from tbvendedor t2 


