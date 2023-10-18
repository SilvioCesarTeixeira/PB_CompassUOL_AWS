Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

with vdrmenor as (SELECT cdvdd,
(SUM(qtd * vrunt)) as tbr_vendas
from tbvendas t 
where status = 'Concluído'
group by cdvdd
order by tbr_vendas
LIMIT 1)
select cddep, nmdep, dtnasc, tbr_vendas as valor_total_vendas
from tbdependente as tdp
left join vdrmenor as vdm
	on tdp.cdvdd = vdm.cdvdd
where vdm.cdvdd = tdp.cdvdd; 
