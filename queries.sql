/* histórico escolar de qualquer aluno, retornando o código e nome da disciplina, semestre e ano que a disciplina foi cursada e nota final */
SELECT alunos_cursou.disciplina_id, disciplinas.nome, alunos_cursou.semestre, alunos_cursou.ano, alunos_cursou.nota
FROM alunos_cursou
INNER JOIN disciplinas ON alunos_cursou.disciplina_id = disciplinas.id
WHERE alunos_cursou.aluno_id = 1;

/* histórico de disciplinas ministradas por qualquer professor, com semestre e ano */
SELECT professores.nome, disciplinas.nome, disciplinas_ministradas.semestre, disciplinas_ministradas.ano
FROM disciplinas_ministradas
INNER JOIN professores ON disciplinas_ministradas.professor_id = professores.id
INNER JOIN disciplinas ON disciplinas_ministradas.disciplina_id = disciplinas.id;

/* listar alunos que já se formaram (foram aprovados em todos os cursos de uma matriz curricular) em um determinado semestre de um ano */
SELECT DISTINCT  alunos.nome AS formados
FROM alunos_cursou
INNER JOIN alunos ON alunos_cursou.aluno_id = alunos.id
WHERE alunos_cursou.nota >= 5 AND EXISTS (SELECT 1 FROM alunos_tcc WHERE alunos_tcc.aluno_id = alunos.id)
AND alunos_cursou.ano = 2020 AND alunos_cursou.semestre = 2;

/* listar todos os professores que são chefes de departamento, junto com o nome do departamento */
SELECT departamentos.nome AS departamento, professores.nome AS chefe
FROM departamentos
INNER JOIN professores ON departamentos.chefe_id = professores.id;

/* saber quais alunos formaram um grupo de TCC e qual professor foi o orientador */
SELECT alunos.nome AS aluno, professores.nome AS orientador, alunos_tcc.grupo
FROM alunos_tcc
INNER JOIN alunos ON alunos_tcc.aluno_id = alunos.id
INNER JOIN professores ON alunos_tcc.orientador_id = professores.id;
