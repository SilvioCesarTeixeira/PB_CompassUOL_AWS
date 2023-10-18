Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

SELECT a.nome 
	from autor as a
WHERE a.codautor not in (select distinct autor from livro)
order by a.nome;
