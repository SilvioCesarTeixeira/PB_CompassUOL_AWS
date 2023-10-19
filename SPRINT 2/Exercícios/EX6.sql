Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select a.codautor, a.nome, 
	count(publicacao) as quantidade_publicacoes
from livro as l
left join autor as a
	on a.codautor = l.autor 
group by autor
order by quantidade_publicacoes desc
limit 1;
