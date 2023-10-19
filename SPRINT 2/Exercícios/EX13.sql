--Apresente a query para listar os 10 produtos menos vendidos pelos canais
--de E-Commerce ou Matriz (Considerar apenas vendas concluídas).
--As colunas presentes no resultado devem ser cdpro, nmcanalvendas,
--nmpro e quantidade_vendas.

SELECT cdpro, 
	nmcanalvendas, 
	nmpro,
	SUM (qtd) as quantidade_vendas
FROM tbvendas
WHERE status = 'Concluído' AND 
	  nmcanalvendas in ('Matriz', 'Ecommerce')
group BY nmcanalvendas, nmpro
ORDER by quantidade_vendas;



