--Apresente a query para listar o gasto médio por estado da federação. 
--As colunas presentes no resultado devem ser estado e gastomedio. 
--Considere apresentar a coluna gastomedio arredondada na segunda casa decimal
--e ordenado de forma decrescente.

--Observação: Apenas vendas com status concluído.

select * from tbvendas t 

WITH vendas_estado AS (SELECT 
	count(cdven) as qtdevendas, 
	estado, 
	ROUND (SUM(qtd * vrunt), 2) AS totvendas
	FROM tbvendas
	WHERE status = 'Concluído'
	GROUP BY estado)
SELECT estado,
ROUND((totvendas / qtdevendas), 2) as gastomedio
FROM vendas_estado
GROUP BY estado
ORDER BY gastomedio DESC;

--2ª solucao:
SELECT 
	estado, 
	(ROUND ((ROUND (SUM (qtd * vrunt), 2)) /  (count(cdven)), 2)) AS gastomedio
	FROM tbvendas
	WHERE status = 'Concluído'
	GROUP BY estado
	ORDER BY gastomedio DESC;
