from faker import Faker
import random

class Curso:
    def __init__(self, nome, semestres):
        self.nome = nome
        self.semestres = semestres

    def create(self):
        return f"INSERT INTO cursos (nome, semestres) VALUES (\'{self.nome}\', {self.semestres});\n"

class Professor:
    def __init__(self, nome, email, salario, departamento_id):
        self.nome = nome
        self.email = email
        self.salario = salario
        self.departamento_id = departamento_id

    def create(self):
        return f"INSERT INTO professores (nome, email, salario, departamento_id) VALUES (\'{self.nome}\', \'{self.email}\', {self.salario:.2f}, {self.departamento_id});\n"

class Ministra:
    def __init__(self, disciplina_id, professor_id, semestre, ano):
        self.disciplina_id = disciplina_id
        self.professor_id = professor_id
        self.semestre = semestre
        self.ano = ano

    def create(self):
        return f"INSERT INTO disciplinas_ministradas (professor_id, disciplina_id, semestre, ano) VALUES ({self.professor_id}, {self.disciplina_id}, {self.semestre}, {self.ano});\n"

class Departamento:
    def __init__(self, nome, chefe_departamento):
        self.nome = nome
        self.chefe_departamento = chefe_departamento

    def create(self):
        return f"INSERT INTO departamentos (nome, chefe_id) VALUES (\'{self.nome}\', {self.chefe_departamento});\n"

    def set_boss(self, chefe_id, id):
        return f"UPDATE departamentos SET chefe_id = {chefe_id} WHERE id = {id};\n"

class Disciplina:
    def __init__(self, nome, curso_id):
        self.nome = nome
        self.curso_id = curso_id

    def create(self):
        return f"INSERT INTO disciplinas (nome, curso_id) VALUES (\'{self.nome}\', {self.curso_id});\n"

class Aluno:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def create(self):
        return f"INSERT INTO alunos (nome, email) VALUES (\'{self.nome}\', \'{self.email}\');\n"

class Cursou:
    def __init__(self, aluno_id, disciplina_id, semestre, ano, nota):
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id
        self.semestre = semestre
        self.ano = ano
        self.nota = nota

    def create(self):
        return f"INSERT INTO alunos_cursou (aluno_id, disciplina_id, semestre, ano, nota) VALUES ({self.aluno_id}, {self.disciplina_id}, {self.semestre}, {self.ano}, {self.nota:.2f});\n"

class Tcc:
    def __init__(self, aluno_id, orientador_id, grupo):
        self.aluno_id = aluno_id
        self.orientador_id = orientador_id
        self.grupo = grupo

    def create(self):
        return f"INSERT INTO alunos_tcc (aluno_id, orientador_id, grupo) VALUES ({self.aluno_id}, {self.orientador_id}, {self.grupo});\n"

fake = Faker(['pt_BR'])

cursos = [
    Curso('Ciência da Computação', 8),
    Curso('Engenharia Elétrica', 10),
    Curso('Matemática', 8),
    Curso('Engenharia Mecânica', 11),
]

departamentos = [
    Departamento('Departamento Ciência da Computação', 'null'),
    Departamento('Departamento Engenharia Elétrica', 'null'),
    Departamento('Departamento Matemática', "null"),
    Departamento('Departamento Engenharia Mecânica', 'null'),
]

professores = [Professor(fake.name(), fake.email(), random.uniform(3000.00, 12000.00), random.randint(1, 4)) for _ in range(16)]

alunos = [Aluno(fake.name(), fake.email()) for _ in range(20)]

disciplinas = [
    Disciplina('Banco de Dados', 1),
    Disciplina('Física II', 4),
    Disciplina('Mecânica dos Fluidos', 4),
    Disciplina('Física I', 4),
    Disciplina('Computação Movel', 1),
    Disciplina('Geometria Analitica', 3),
    Disciplina('Sistemas Digitais', 2),
    Disciplina('Redes', 2),
    Disciplina('Calculo I', 3),
    Disciplina('Engenharia de Software', 1),
    Disciplina('Engenheinharia de Tomadas', 2),
    Disciplina('Desenvolvimento WEB', 1),
    Disciplina('Sistemas Digitais II', 2),
    Disciplina('Calculo II', 3),
    Disciplina('Calculo III', 3),
]

ministram = [Ministra(i, i, random.randint(1, 2), random.randint(2000, 2024)) for i in range(1, 16)]

cursaram = [Cursou(i, random.randint(1, 15), random.randint(1, 2), random.randint(2000, 2024), random.uniform(0.0, 10.0)) for i in range(1, 21)]
for i in range(0, 20):
    aluno = random.randint(1, 21)
    disciplina = random.randint(1, 15)

    if aluno == cursaram[i].aluno_id and disciplina == cursaram[i].disciplina_id:
        continue

    cursaram.append(Cursou(aluno, disciplina, random.randint(1, 2), random.randint(2000, 2024), random.uniform(0.0, 10.0)))

tccs = []
professor = 1
for i in range(1, 21):
    tccs.append(Tcc(i, professor, random.randint(1, 5)))

    if professor == 16:
        professor = 0

    professor += 1

def preenche_chefe(chefes: list):
    chefe = random.randint(1, 17)

    if chefe not in chefes:
        chefes.append(chefe)
    else:
        preenche_chefe(chefes)

    return chefes

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

    f.write("\n")

    for ministra in ministram:
        f.write(ministra.create())

    f.write("\n")

    for cursou in cursaram:
        f.write(cursou.create())

    f.write("\n")

    for tcc in tccs:
        f.write(tcc.create())

    f.write("\n")

    chefes = []
    for i, departamento in enumerate(departamentos):
        preenche_chefe(chefes)

    for i, departamento in enumerate(departamentos):
        f.write(departamento.set_boss(chefes[i], i + 1))
