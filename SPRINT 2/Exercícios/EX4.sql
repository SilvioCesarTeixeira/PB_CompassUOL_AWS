select*
from livro l 

select nome, codautor, nascimento, count(*) as quantidade --nome, codautor, nasci, qtde
from autor as a
left join livro as l
	on a.codautor = l.autor 
group by nome;
ORDER by nome;
