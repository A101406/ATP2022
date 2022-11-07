import csv

def lerAlunos(file):
    file = open(file,encoding="UTF8")
    csv_file = csv.reader(file,delimiter=",")
    file.readline()
    lista = []
    for aluno in csv_file:
        lista.append(tuple(aluno))
    return lista

def distribCurso(alunos):
    distrib = {}
    for _,_,curso,*_ in alunos:
        if curso not in distrib:
            distrib[curso] = 1
        else: 
            distrib[curso] += 1
    return distrib

def mediaNotas(alunos):
    lista = []
    for aluno in alunos:
        id,nome,curso,tpc1,tpc2,tpc3,tpc4 = aluno
        media = ((int(aluno[3])+int(aluno[4])+int(aluno[5])+int(aluno[6]))/4)
        aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media
        lista.append(aluno_novo)
    return lista
        
def escaloesNotas(alunos):
    lista = []
    for aluno in alunos:
        id,nome,curso,tpc1,tpc2,tpc3,tpc4,media = aluno
        if int(media) in range (0,5):
            escalao = "E"
            aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            lista.append(aluno_novo)
        if int(media) in range (5,9):
            escalao = "D"
            aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            lista.append(aluno_novo)
        if int(media) in range (9,13):
            escalao = "C"
            aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            lista.append(aluno_novo)
        if int(media) in range (13,17):
            escalao = "B"
            aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            lista.append(aluno_novo)
        if int(media) in range (17,21):
            escalao = "A"
            aluno_novo = id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            lista.append(aluno_novo)
    return lista

def distribEscalao(alunos):
    distrib={}
    for _,_,_,_,_,_,_,_,escalao in alunos:
        if escalao not in distrib:
            distrib[escalao]=1
        else:
            distrib[escalao] +=1
    return distrib

def grafico(alunos):
    import matplotlib.pyplot as plt
    print("""       (1) - Distribuição de alunos por curso;
        (2) - Distribuição de alunos por escalão.
             
    Escolha uma das opções acima.                           """)

    distribuiçao = int(input("Qual o tipo de distribuição? "))
    
    if distribuiçao == 1:
        distrib = distribCurso(alunos) 
        eixoXx = distrib.keys()
        eixoXy = distrib.values()
        plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
        plt.title("Distribuição de alunos por Curso")
        plt.xlabel("Cursos", color ="blue")
        plt.ylabel("Número de alunos", color = "blue")
        plt.show()
    elif distribuiçao == 2:
        distrib = distribEscalao(alunos) 
        eixoXx = distrib.keys()
        eixoXy = distrib.values()
        plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
        plt.title("Distribuição de alunos por Escalão")
        plt.xlabel("Escalões", color = "blue")
        plt.ylabel("Número de alunos", color = "blue")
        plt.show()
    else:
        print("Opção inválida.")

def tabela(alunos):
    print("""       (1) - Distribuição de alunos por curso;
        (2) - Distribuição de alunos por escalão.
             
    Escolha uma das opções acima.                

    ----------------------------------------------------
    """)

    distribuiçao = int(input("Qual o tipo de distribuição? "))
    
    if distribuiçao == 1:
        distrib = distribCurso(alunos) 
        print(" Tabela de distribuição de alunos por Curso:")
        print("")
        print(f" Curso   |   Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7}")
    elif distribuiçao == 2:
        distrib = distribEscalao(alunos) 
        valores = distrib.values()
        chaves = distrib.keys()
        print(" Tabela de distribuição de alunos por Escalão:")
        print("")
        print(f" Escalão |  Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7} ")
    else:
        print("Opção inválida.")

def menu(alunos,alunos_novo,listaAlunos):
    opçao = -1
    while opçao != 0:
        print(""" Menu:
                    ->(1) Ver informação do dataset inicial;
                    ->(2) Ver informação do dataset com média das notas de cada aluno;
                    ->(3) Ver informação do dataset com média e escalão dos alunos;
                    ->(4) Ver distribuição dos alunos por curso;
                    ->(5) Ver distribuição dos alunos pelos seguintes escalões, relativamente às notas: 
                        E [1-4], D [5-8], C [9-12], B [13-16], A [17-20];
                    ->(6) Ver distribuições na forma de gráfico de linha;
                    ->(7) Ver distribuições na forma de uma tabela;
                    ->(0) Sair.

                Escolha uma das opções acima.
                ----------------------------------------------------------------------------------------------------""")
        opçao = int(input("Escolha a opção pretendida: "))
        if opçao == 1:
            print(alunos)
        elif opçao == 2:
            print(alunos_novo)
        elif opçao == 3:
            print(listaAlunos)
        elif opçao == 4:
            distribCurso(listaAlunos)
        elif opçao == 5:
            distribEscalao(listaAlunos)
        elif opçao == 6:
            grafico(listaAlunos)
        elif opçao == 7:
            tabela(listaAlunos)
    print("Saiu do programa.")

    return

        

        
        