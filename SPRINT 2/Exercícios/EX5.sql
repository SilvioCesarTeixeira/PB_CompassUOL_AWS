--Apresente a query para listar o nome dos autores que publicaram livros através 
--de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna
--nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

SELECT DISTINCT a.nome 
FROM autor as a
left join livro as l
	on l.autor = a.codautor 
WHERE l.editora = (SELECT e.codeditora 
	from editora as e 
	inner join endereco as en 
		on e.endereco = en.codendereco
	where en.estado NOT IN ('PARANÁ','RIO GRANDE DO SUL','SANTA CATARINA'))
order by a.nome;
	