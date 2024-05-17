CREATE TABLE cursos (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	semestres int NOT NULL,
);

CREATE TABLE alunos (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	ra varchar(15),
	curso int NOT NULL,
	email varchar(255),
	username varchar(255),
	senha varchar(255),
	PRIMARY KEY (id),
	FOREIGN KEY (curso) REFERENCES cursos(id)
);

CREATE TABLE professores (
	id int NOT NULL AUTO_INCREMENT,
	nome varchar(255),
	email varchar(255),
	username varchar(255),
	senha varchar(255),
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
