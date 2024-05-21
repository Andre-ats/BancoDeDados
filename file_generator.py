from faker import Faker
import random

class Curso:
    def __init__(self, nome, semestres):
        self.nome = nome
        self.semestres = semestres

    def create(self):
        return f"INSERT INTO cursos (nome, semestres) VALUES (\"{self.nome}\", {self.semestres});\n"

class Professor:
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario

    def create(self):
        return f"INSERT INTO professores (nome, email, salario) VALUES (\"{self.nome}\", \"{self.email}\", {self.salario:.2f});\n"

class Departamento:
    def __init__(self, nome, chefe_departamento, curso):
        self.nome = nome
        self.chefe_departamento = chefe_departamento
        self.curso = curso

    def create(self):
        return f"INSERT INTO departamentos (nome, chefe_departamento, curso) VALUES (\"{self.nome}\", {self.chefe_departamento}, {self.curso});\n"

fake = Faker(['pt_BR'])

cursos = [
    Curso("Ciência da Computação", 8),
    Curso("Engenharia Elétrica", 10),
    Curso("Matemática", 8),
    Curso("Engenharia Mecânica", 11),
]

professores = [Professor(fake.name(), fake.email(), random.uniform(3000.00, 12000.00))]
for i in range(10):
    professores.append(Professor(fake.name(), fake.email(), random.uniform(3000.00, 12000.00)))

departamentos = [
    Departamento("Departamento Ciência da Computação", random.randint(1, len(professores)), 1),
    Departamento("Departamento Engenharia Elétrica", random.randint(1, len(professores)), 2),
    Departamento("Departamento Matemática", random.randint(1, len(professores)), 3),
    Departamento("Departamento Engenharia Mecânica", random.randint(1, len(professores)), 4),
]

with open("./seeder.sql", "w", encoding='utf-8') as f:
    for curso in cursos:
        f.write(curso.create())

    f.write("\n")

    for professor in professores:
        f.write(professor.create())

    f.write("\n")

    for departamento in departamentos:
        f.write(departamento.create())