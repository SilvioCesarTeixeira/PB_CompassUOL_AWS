SELECT *
FROM editora e

SELECT *
FROM livro l 


select e.nome, count(*) as quantidade, en.estado, en.cidade
from livro as l
left join editora as e
	on e.codeditora = l.editora
LEFT JOIN endereco as en
	on en.codendereco = e.endereco 
group by editora
LIMIT 5;
