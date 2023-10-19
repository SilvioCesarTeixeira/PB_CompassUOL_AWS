Considerando a base de dados Biblioteca apresentada na Seção 3, realize a exportação de dados (em formato .CSV)
através do cliente SQL de sua preferência (DBeaver, VSCode...).  O layout dos arquivos, bem como os critérios de
coleta de dados estão definidos em cada uma das questões da atividade.

Perguntas dessa tarefa
Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. 
Utilizar o caractere ; (ponto e vírgula) como separador. 
Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e 
seus respectivos nomes de cabeçalho que listamos abaixo:

CodLivro Titulo CodAutor NomeAutor Valor CodEditora NomeEditora

WITH dez as (SELECT l.cod, l.titulo, a.codautor, a.nome , l.valor, l.editora
FROM livro as l
LEFT JOIN autor as a
	ON a.codautor = l.autor)
SELECT dez.cod as CodLivro,
	dez.titulo as Titulo,
	dez.codautor as CodAutor,
	dez.nome as NomeAutor,
	dez.valor as Valor,
	dez.editora as CodEditora,
	e.nome as NomeEditora
FROM dez
LEFT JOIN editora as e
	ON dez.editora = e.codeditora
ORDER BY dez.valor DESC 
LIMIT 10;

Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub. 
Abaixo (na caixa de envio), gentileza nos enviar o link do arquivo .csv que colocou no seu github.
exemplo de envio (resposta):

Segue abaixo link do arquivo no formato .csv (referente a query dos 10 livros mais caros) conforme solicitado:
https://github.com/aasouzaconsult/programabolsas/blob/main/arquivo1.csv


Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na
biblioteca para um arquivo CSV. Utilizar o caractere | (pipe) como separador. 
Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e
seus respectivos nomes de cabeçalho que listamos abaixo:

CodEditora NomeEditora QuantidadeLivros

SELECT l.editora as CodEditora, 
	e.nome as NomeEditora, 
	count(l.editora) as QuantidadeLivros
FROM livro as l 
LEFT JOIN editora as e
	ON e.codeditora = l.editora
GROUP BY l.editora
LIMIT 5;



Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub. 
Abaixo (na caixa de envio), gentileza nos enviar o link do arquivo .csv que colocou no seu github.
exemplo de envio (resposta):

Segue abaixo link do arquivo no formato .csv (referente a query das 5 editoras
com maior quantidade de livros na biblioteca) conforme solicitado:
https://github.com/aasouzaconsult/programabolsas/blob/main/arquivo2.csv