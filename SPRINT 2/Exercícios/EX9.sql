Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

with contagem as (SELECT t.cdpro , t.nmpro, COUNT(cdpro) as qtde  
from tbvendas as t
where status = 'Concluído'and 
	dtven BETWEEN '2014-02-03' and '2018-02-02'
group by t.nmpro
order by qtde desc
LIMIT 1)
Select cdpro, nmpro 
FROM contagem;
