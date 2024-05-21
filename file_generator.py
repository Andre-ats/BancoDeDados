from faker import Faker
import random

class Curso:
    def __init__(self, nome, semestres):
        self.nome = nome
        self.semestres = semestres

    def create(self):
        return f"INSERT INTO cursos (nome, semestres) VALUES (\"{self.nome}\", {self.semestres});\n"

class Professor:
    def __init__(self, nome, email, salario, departamento_id):
        self.nome = nome
        self.email = email
        self.salario = salario,
        self.departamento_id = departamento_id

    def create(self):
        return f"INSERT INTO professores (nome, email, salario, departamento_id) VALUES (\"{self.nome}\", \"{self.email}\", {self.salario:.2f}, {self.departamento_id});\n"

class Departamento:
    def __init__(self, nome, chefe_departamento):
        self.nome = nome
        self.chefe_departamento = chefe_departamento

    def create(self):
        return f"INSERT INTO departamentos (nome, chefe_id) VALUES (\"{self.nome}\", {self.chefe_departamento});\n"

class Disciplina:
    def __init__(self, nome, curso_id):
        self.nome = nome
        self.curso_id = curso_id

    def create(self):
        return f"INSERT INTO disciplinas (nome, curso_id) VALUES (\"{self.nome}\", {self.curso_id});\n"

class Aluno:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def create(self):
        return f"INSERT INTO alunos (nome, email) VALUES (\"{self.nome}\", \"{self.email}\");\n"

fake = Faker(['pt_BR'])

cursos = [
    Curso("Ciência da Computação", 8),
    Curso("Engenharia Elétrica", 10),
    Curso("Matemática", 8),
    Curso("Engenharia Mecânica", 11),
]

departamentos = [
    Departamento("Departamento Ciência da Computação", None),
    Departamento("Departamento Engenharia Elétrica", None),
    Departamento("Departamento Matemática", None),
    Departamento("Departamento Engenharia Mecânica", None),
]

professores = [Professor(fake.name(), fake.email(), random.uniform(3000.00, 12000.00), random.uniform(1, 4))]
for i in range(10):
    professores.append(Professor(fake.name(), fake.email(), random.uniform(3000.00, 12000.00), random.uniform(1, 4)))

alunos = [Aluno(fake.name(), random.randint(1, 4), fake.email()) for _ in range(20)]

disciplinas = [
    Disciplina("Banco de Dados", 1),
    Disciplina("Física II", 4),
    Disciplina("Mecânica dos Fluidos", 4),
    Disciplina("Física I", 4),
    Disciplina("Computação Movel", 1),
    Disciplina("Geometria Analitica", 3),
    Disciplina("Sistemas Digitais", 2),
    Disciplina("Redes", 2),
    Disciplina("Calculo I", 3),
    Disciplina("Engenharia de Software", 1),
    Disciplina("Engenheinharia de Tomadas", 2),
    Disciplina("Desenvolvimento WEB", 1),
    Disciplina("Sistemas Digitais II", 2),
    Disciplina("Calculo II", 3),
    Disciplina("Calculo III", 3),
]

with open("./seeder.sql", "w", encoding='utf-8') as f:
    for curso in cursos:
        f.write(curso.create())

    f.write("\n")

    for departamento in departamentos:
        f.write(departamento.create())

    f.write("\n")

    for professor in professores:
        f.write(professor.create())

    f.write("\n")

    for aluno in alunos:
        f.write(aluno.create())

    f.write("\n")

    for disciplina in disciplinas:
        f.write(disciplina.create())
