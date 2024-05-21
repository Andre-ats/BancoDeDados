CREATE TABLE cursos (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	semestres int NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE disciplina (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	PRIMARY KEY (id)
);

CREATE TABLE alunos (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	ra varchar(15),
	curso int NOT NULL,
	email varchar(255),
	PRIMARY KEY (id),
	FOREIGN KEY (curso) REFERENCES cursos(id)
);

CREATE TABLE professores (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	email varchar(255),
	salario decimal(15,2),
	PRIMARY KEY (id)
);

CREATE TABLE departamentos (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	chefe_departamento int NOT NULL,
	curso int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (chefe_departamento) REFERENCES professores(id),
	FOREIGN KEY (curso) REFERENCES cursos(id)
);
