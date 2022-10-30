# Modelo = [(nome,desc,período,ano...)]

import csv

def lerObras(filename):
    file=open(filename,encoding="UTF8")   #encoding informa o windows para ler o ficheiro com o algoritmo "UFT8"
    csv_file=csv.reader(file,delimiter=";") # delimiter serve para obrigar a ler o ficheiro e separar a informação pelas ;
    file.readline()
    lista = []
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista

def tamanhoObras(obras):
    return len(obras)

def imprime(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome,desc,ano,_,comp,*_ in obras: 
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano[:8]:8} | {comp[:15]:15} |")

def ordem1(tuplo):
    return tuplo[0]

def ordem2(tuplo):
    return tuplo[1]

def titAno1(obras):
    lista=[]
    for nome,_,ano,*_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=ordem1)
    return lista

def titAno2(obras):
    lista=[]
    for nome,_,ano,*_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=ordem2)
    return lista

def titporAno(obras):
    dic = {}
    for nome,_,ano,*_ in obras:
        if ano in dic.keys():
            dic[ano].append(nome)
        else:
            dic[ano] = [nome]
    return dic 

def ordenaComp(obras):
    lista = []
    for _,_,_,_,comp,*_ in obras:
        if comp not in lista:
            lista.append(comp)
    lista.sort()
    return lista
    
def distPeriodo(obras):
    dic = {}
    for _,_,_, periodo,*_ in obras:
        if periodo in dic.keys():
            dic[periodo]= dic[periodo] + 1
        else:
            dic[periodo]= 1
    return dic

def distAno(obras):
    dic = {}
    for _,_,ano,*_ in obras:
        if ano in dic.keys():
            dic[ano]= dic[ano] + 1
        else:
            dic[ano]= 1
    return dic

def distComp(obras):
    dic = {}
    for _,_,_,_,Comp,*_ in obras:
        if Comp in dic.keys():
            dic[Comp]= dic[Comp] + 1
        else:
            dic[Comp]= 1
    return dic

def grafico(obras):
    import matplotlib.pyplot as plt 
    print("""Tipos de distribuições:
          ->(1) Distribuição das obras por período;
          ->(2) Distribuição das obras por ano;
          ->(3) Distribuição das obra por compositor. """)

    distrib = int(input("Qual a distribuição pretendida? 1,2 ou 3."))

    if distrib ==1:
        distribperiodos = distPeriodo(obras)
        x = [x for x in range(1, len(distribperiodos)+1)]
        periodos = list(distribperiodos.keys())
        y = []
        for i in periodos:
            y.append(distribperiodos[i])
        plt.bar( x, y, tick_label = periodos, color = ['red'])
        plt.xticks(rotation = 90)
        plt.title('Distribuição da obras por Período') 
        plt.xlabel('Períodos')
        plt.ylabel('Número de Obras')
        plt.show()
    
    if distrib==2:
        distribanos = distAno(obras)
        x = [x for x in range(1, len(distribanos)+1)]
        anos = list(distribanos.keys())
        y = []
        for i in anos:
            y.append(distribanos[i])
        plt.bar( x, y, tick_label = anos, width=0.5,color = ['green'])
        plt.title('Distribuição da obras por Ano') 
        plt.xlabel('Anos')
        plt.ylabel('Número de Obras')
        plt.show()
    
    if distrib==3:
        distribcomp = distComp(obras)
        x = [x for x in range(1, len(distribcomp)+1)]
        comps = list(distribcomp.keys())
        y = []
        for i in comps:
            y.append(distribcomp[i])
        plt.bar( x, y, tick_label = comps, width=0.5,color = ['blue'])
        plt.xticks(rotation = 90)
        plt.title('Distribuição da obras por Compositores') 
        plt.xlabel('Compositores')
        plt.ylabel('Número de Obras')
        plt.show()
    return 

def compObras(obras):
    dic = {}
    listaComp = ordenaComp(obras)
    for i in listaComp:
        dic[i]=[]
        for nome,_,_,_,comp,*_ in obras:
            if comp==i:
                dic[i].append(nome)
    diclist =[]
    for i in dic:
        x = (i,dic[i])
        diclist.append(x)
    
    return diclist
                
def menu(obras):
    
    opçao = -1
        
    while opçao != 0:
        print("""Menu:
                ->(1) Ver número de obras catalogadas no dataset;
                ->(2) Ver tabela com os dados do dataset;
                ->(3) Ver lista de tuplos (título, ano), ordenada alfabeticamente por título;
                ->(4) Ver lista de tuplos (título, ano), ordenada crescentemente por ano;
                ->(5) Ver dicionário em que cada ano tem a ele associado a lista de títulos a ele associado;
                ->(6) Ver lista ordenada dos compositores;
                ->(7) Ver distribuição das obras por período;
                ->(8) Ver distribuição das obras por ano;
                ->(9) Ver distribuição das obras por compositor;
                ->(10) Desenhar um gráfico das distribuições anteriores;
                ->(11) Ver lista dos compositores em que cada compositor tem a ele associado uma lista dos títulos das obras que compôs; 
                ->(0) Sair 
                
                Escolha uma das opções acima. 
                """)

        opçao = int(input("Escolha uma das opções apresentadas no menu:"))

        if opçao==1:
            print("O número de obras catalogadas é ", tamanhoObras(obras))

        if opçao==2:
            print("--------------------------------------------------------------------")
            imprime(obras)
        
        if opçao==3:
            print("--------------------------------------------------------------------")
            print(titAno1(obras))

        if opçao==4:
            print("---------------------------------------------------------------------")
            print(titAno2(obras))

        if opçao==5:
            print("---------------------------------------------------------------------")
            print(titporAno(obras))

        if opçao==6:
            print("---------------------------------------------------------------------")
            print(ordenaComp(obras))

        if opçao==7:
            print("---------------------------------------------------------------------")
            print(distPeriodo(obras))

        if opçao==8:
            print("---------------------------------------------------------------------")
            print(distAno(obras))

        if opçao==9:
            print("---------------------------------------------------------------------")
            print(distComp(obras))

        if opçao==10:
            print("---------------------------------------------------------------------")
            print(grafico(obras))

        if opçao==11:
            print("---------------------------------------------------------------------")
            print(compObras(obras))

    print("Saiu do programa.")
    return

