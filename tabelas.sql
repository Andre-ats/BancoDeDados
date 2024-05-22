CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    salario DECIMAL(15, 2),
    departamento_id INT NOT NULL
);

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    chefe_id INT,
    FOREIGN KEY (chefe_id) REFERENCES professores(id)
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    semestres INT NOT NULL
);

CREATE TABLE disciplinas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    curso_id INT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE alunos_cursou (
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    semestre INT NOT NULL,
    ano INT NOT NULL,
    nota INT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

CREATE TABLE disciplinas_ministradas (
    professor_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    semestre INT NOT NULL,
    ano INT NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

CREATE TABLE alunos_tcc (
    aluno_id INT NOT NULL,
    orientador_id INT NOT NULL,
    grupo INT,
    FOREIGN KEY (orientador_id) REFERENCES professores(id)
);

ALTER TABLE professores
ADD CONSTRAINT fk_professores_departamento FOREIGN KEY (departamento_id)
REFERENCES departamentos(id);
