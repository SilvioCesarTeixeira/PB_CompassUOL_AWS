Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

with contagem as (SELECT tvn.cdvdd, tvr.nmvdd, COUNT(tvn.cdven) as quantidade 
from tbvendas as tvn
left join tbvendedor as tvr
	on tvn.cdvdd = tvr.cdvdd 
where status = 'Concluído'
group by tvn.cdvdd
order by quantidade desc
limit 1)
select cdvdd, nmvdd
from contagem;
