--Apresente a query para listar os códigos das vendas identificadas como deletadas. 
--Apresente o resultado em ordem crescente.

SELECT * FROM tbvendas t 

SELECT cdven
from tbvendas t 
WHERE deletado = 1
ORDER BY cdven ASC; 