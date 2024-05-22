CREATE TABLE professores (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255),
    email varchar(255),
    salario decimal(15, 2),
    departamento_id int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE departamentos (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255),
    chefe_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (chefe_id) REFERENCES professores(id)
);

CREATE TABLE cursos (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255),
    semestres int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE disciplinas (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255),
    curso_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE alunos (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255),
    email varchar(255),
    PRIMARY KEY (id)
);

CREATE TABLE alunos_cursou (
    aluno_id int NOT NULL,
    disciplina_id int NOT NULL,
    semestre int NOT NULL,
    ano int NOT NULL,
    nota int,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

CREATE TABLE disciplinas_ministradas (
    professor_id int NOT NULL,
    disciplina_id int NOT NULL,
    semestre int NOT NULL,
    ano int NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

CREATE TABLE alunos_tcc (
    aluno_id int NOT NULL,
    orientador_id int NOT NULL,
    grupo int,
    FOREIGN KEY (orientador_id) REFERENCES professores(id)
);

ALTER TABLE professores
ADD CONSTRAINT fk_professores_departamento FOREIGN KEY (departamento_id)
REFERENCES departamento(id);
