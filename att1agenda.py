import sys
import string

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

def adicionar(descricao, extras):

   
  if descricao  == '':                                              #Caso não houver uma descrição, a função não será utilizada,
    return False                                                    #Se houver uma descrição uma variável receberá a nova atividade
  else:                                                             #o arquivo é aberto no modo a, para não sobrescrever, e são 
    novaAtividade = ""                                              #feitas as verificaçãoes de validação para as partes das tarefas
                                                                    #e posteriormente adicionadas a varaivél novaAtividade se forem
    if dataValida(extras[0]) == True:                               #validadas
      novaAtividade = novaAtividade + extras[0] + " "               #Prioridade é coloca maiscula, para ficar padronizado e facilitar 
    if horaValida(extras[1]) == True:                               #a ordenação
      novaAtividade = novaAtividade + extras[1] + " "
    if prioridadeValida(extras[2]) == True:
      novaAtividade = novaAtividade + extras[2].upper() + " "
    if descricao != '':
      novaAtividade = novaAtividade + descricao + " "
    if contextoValido(extras[3]) == True:
      novaAtividade = novaAtividade + extras[3] + " "
    if projetoValido(extras[4]) == True:
      novaAtividade = novaAtividade + extras[4]

  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  return True


def prioridadeValida(pri):                 #Verifica se o tamanho da str é diferente de 3, se for devolve FALSE
  if len(pri) != 3:                        #Caso for igual a 3, verifica se o primeiro e o terceiro char são os parenteses
    return False                           #Depois usa esse método para adicionar a "letras" uma lista com elementos de A a Z
  else:                                    #Depois verifica com um for se o elemento medio da prioridade é igual a um letra de A a Z
    if pri[0] == "(" and pri[2] == ")":    #tanto minuscula quanto maiuscula, se for satisfeito devolve TRUE, caso não devolve False
      letras = list(string.ascii_lowercase)
      a = "b"
      for i in letras:      
        if i.upper() == pri[1] or i.lower() == pri[1]:
          a = True    
      if a == True:
        return True
      else:
        return False
    else:
      return False 


def horaValida(horaMin) :
  if len(horaMin) != 4 or not soDigitos(horaMin): #Verifica se o tamanho da hora não é 4 e se não tem só digitos
    return False                                  #Se isso for verdade devolva FALSE
  else:                                        
    tupla1 = int(horaMin[0]),int(horaMin[1])      #Caso contrário roda um for pela tupla dos 2 primeiros nums
    doisPdig = ""                                 #E depois pela tupla dos 2 ultimos nums 
    for i in tupla1:                              #Adicionando a uma variavel o que já tem nela e os elementos da tupla
      doisPdig = doisPdig + str(i)                #Depois compara se os dois primeiros digitos estão no intervalo
    tupla2 = int(horaMin[2]), int(horaMin[3])     #E se os dois segundos digito estão no intervalo
    doisSdig = ""                                 #Se sim devolva TRUE, caso não devolva FALSE
    for i in tupla2:
      doisSdig = doisSdig + str(i)    
    if (int(doisPdig) >= 00 and int(doisPdig) <= 23) and (int(doisSdig) >= 00 and int(doisSdig) <= 59):    
      return True
    else:
      return False


def dataValida(data):
  if len(data) != 8 or not soDigitos(data):  #No mesmo estilo da horaValida devolve falso caso data n tem 8 digitos 
    return False                             #e se n são só digitos, caso isso for falso, vai pro else e faz o procedimento de  
  else:                                      #guardar os dias, meses e anos como na horaValida
    tupla1 = int(data[0]),int(data[1])
    dias = ""
    for i in tupla1:
      dias = dias + str(i)

    tupla2 = int(data[2]),int(data[3])
    mes = ""
    for i in tupla2:
      mes = mes + str(i)

    tupla3 = int(data[4]), int(data[5]), int(data[6]), int(data[7])
    ano = ""
    for i in tupla3:
      ano = ano + str(i)

    if int(mes) >= 1 and int(mes) <= 12:        #Depois começa as condições para validação, primeiro focando se os meses estão 
      if int(mes) == 2:                         #no parametro, logo em seguida verificando se os dias estão correspondentes aos meses, 
        if int(dias) >= 1 and int(dias) <= 29:  #no caso fevereiro até 29, alguns meses até 30 e outros até 31, se tudo estiver correto
          return True                           #Devolve TRUE, caso não devolve False
        else:                                   #Obs: Ao coverter o mes em int, ele tira o 0 antes do numero, ex:int(03) devolve 3.
          return False                          
      if int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12:
        if int(dias) >= 1 and int(dias) <= 31:
          return True
        else:
          return False
      if int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
        if int(dias) >= 1 and int(dias) <= 30:
          return True
        else:
          return False

    else:
      return False

 
def projetoValido(proj):    #Verifica se o tamanho da str não é menor que 2
  if len(proj) >= 2:        #Caso não, retorna False
    if proj[0] == "+":      #Se tamanho não é menor que 2, verifica se o primeiro char é "+"
      return True           #Se sim devolve True, caso não devolve False
    else:
      return False    
  else:
    return False

def contextoValido(cont):   #Verifica se o tamanho da str não é menor que 2
  if len(cont) >= 2:        #Caso não, retorna False
    if cont[0] == "@":      #Se tamanho não é menor que 2, verifica se o primeiro char é "@"
      return True           #Se sim devolve True, caso não devolve False
    else:           
      return False
  else:
    return False

# Valida que a data ou a hora contém apenas dígitos, desprezando espaços
# extras no início e no fim.
def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True


fp = open(TODO_FILE,"a")                     #Caso o arquivp não exista, o mesmo é criado, se já existir 
fp.close()                                   #o mesmo permanece do mesmo jeito
todo = open("todo.txt", "r")                 #Variavel que abre o arquivo no modo de leitura,depois o adiciona a uma var
arquivo = todo.read()                        #Depois a variavel linhas recebe esse arquivo em forma de listas, com cada linha
linhas = arquivo.splitlines()                #um elemento da mesma                          
todo.close()
def organizar(linhas):                        #Usando a função organizar, a mesma recebe essa lista de linhas
                                              #Depois percorre essa lista, e trata cada indice retirando espaços em branco e "\n"
  itens = []                                  #no inicio e final das frases, e depois separa cada frase em uma lista de palavras
                                              #na váriavel tokens, depois roda vários "for's" nessa var em busca de analisar    
  for l in linhas:                            #se existem datas, horas, prioridades, contextos, projetos e descrições no parametro                                  
    check = False                             #utlizando as funções de validação anteriormente criadas, e também tratando de 
    check2 = False                            #jogar as partes das tarefas para a descrição caso as anteriores falhem na validação
    data = ''                                 #usando as variáveis booleanas check e check2    
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip() 
    tokens = l.split() 
    
    for i in tokens:                          #For para verificação se as funções de validação são satisfeitas
      if soDigitos(i) == True:                #adicionando a variável correspondente esses dados, e depois removendo o que fica, e 
        if data == '':                        #assim sucessivamente para as demais funções
          if dataValida(i) == True:           #Em seguida adiciona a lista itens a tupla com essas informações devidamente
            data = data + i                   #organizadas                      
            tokens.remove(i)                
            check = True  
    for i in tokens:
      if soDigitos(i) == True:
        if hora == '':
          if data == '' or check == True:
            if horaValida(i) == True:
              check2 = True
              hora = hora + i
              tokens.remove(i)
 
    for i in tokens:
      if (hora == '' or check2 == True) or data == '':
        if prioridadeValida(i) == True:
          pri = pri + i
          tokens.remove(i) 

    for i in tokens:
      if contextoValido(i) == True:
        if contexto == '':
          contexto = contexto + i
          tokens.remove(i)

    for i in tokens:
      if projetoValido(i) == True:
        if projeto == '': 
          projeto = projeto + i
          tokens.remove(i)

    for i in tokens:
      if contextoValido(i) == True:
        if contexto != '':
          tokens.remove(i)

    for i in tokens:
      if projetoValido(i) == True:
        if projeto != '':
          tokens.remove(i)
  
    for i in tokens:
      desc = desc + i + " "
    desc = desc.strip()


    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens


def listar():
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)     #Depois utiliza as funções de ordenação para organizar as tuplas de acordo
  todo.close()                    #com data e hora e prioridade
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  i = 0
  while i < len(ordenacao):       #Usa um while para percorrer a lista ordenação cuja lista estão as tuplas
    saida = ""                    #E através de verificações formata as datas e horas com os separadores
    if ordenacao[i][1][0] != '':  #Depois vai verificando as partes das tuplas e printando com cores de acordo
      a = ordenacao[i][1][0]      #com sua prioridade usando printCores 
      saida = saida + a[0]+a[1]+"/"+a[2]+a[3]+"/"+a[4]+a[5]+a[6]+a[7] + " "
    if ordenacao[i][1][1] != '':
      h = ordenacao[i][1][1]
      saida = saida + h[0]+h[1]+"h"+h[2]+h[3]+"m"
      
    if ordenacao[i][1][2] == "(a)" or ordenacao[i][1][2] == "(A)":
      printCores(str(str(i) + " " + saida +  " " + ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), YELLOW + BOLD)
    if ordenacao[i][1][2] == "(b)" or ordenacao[i][1][2] == "(B)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), YELLOW)
    if ordenacao[i][1][2] == "(c)" or ordenacao[i][1][2] == "(C)":
      printCores(str(str(i) + " " + saida + " "  +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), BLUE)
    if ordenacao[i][1][2] == "(d)" or ordenacao[i][1][2] == "(D)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), CYAN)
    if ordenacao[i][1][2] == '':
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RESET)
    if ordenacao[i][1][2] == "(e)" or ordenacao[i][1][2] == "(E)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)  
    if ordenacao[i][1][2] == "(f)" or ordenacao[i][1][2] == "(F)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(g)" or ordenacao[i][1][2] == "(G)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(h)" or ordenacao[i][1][2] == "(H)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(i)" or ordenacao[i][1][2] == "(I)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(j)" or ordenacao[i][1][2] == "(J)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(k)" or ordenacao[i][1][2] == "(K)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), GREEN)
    if ordenacao[i][1][2] == "(l)" or ordenacao[i][1][2] == "(L)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(m)" or ordenacao[i][1][2] == "(M)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(n)" or ordenacao[i][1][2] == "(N)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(o)" or ordenacao[i][1][2] == "(O)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(p)" or ordenacao[i][1][2] == "(P)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(q)" or ordenacao[i][1][2] == "(Q)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(r)" or ordenacao[i][1][2] == "(R)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(s)" or ordenacao[i][1][2] == "(S)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(t)" or ordenacao[i][1][2] == "(T)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(u)" or ordenacao[i][1][2] == "(U)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(v)" or ordenacao[i][1][2] == "(V)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(w)" or ordenacao[i][1][2] == "(W)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(x)" or ordenacao[i][1][2] == "(X)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(y)" or ordenacao[i][1][2] == "(Y)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(z)" or ordenacao[i][1][2] == "(Z)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    
    i = i + 1     
  return

def ordenarPorDataHora(itens):      #A função recebe a lista de tuplas e usa uma listas auxiliares para fazer a separação 
  listaaux = []                     #primeiro se tem data ou não, separando ambas em listas diferentes, depois utiliza o 
  listacomdata = []                 #bubble sort para ordenar na lista que tem datas, por ordem crescente usando o slice 
  for w in itens:                   #para comparar a data ao contrario(ANOMESDIA) e depois utiliza o bubble
    if w[1][0] == "":               #novamente para verificar se as datas forem iguais e horas vazia e a proxima n
      listaaux.append(w)            #troca-las de posiçao, depois usa um for na listaaux para separar em
    elif w[1][0] != "":             #lista sem data e hora , e lista com hora, depois utilizando outro
      listacomdata.append(w)        #bubble sort na lista com tuplas que tem hora, ordena crescentemente
                                    #Depois concatena as listas com hora e sem data e hora em uma var
                                    #e depois concatena essa var com a lista com as datas
  for i in range(0,len(listacomdata)):
    for x in range(0,len(listacomdata)-1):
      if int(listacomdata[x][1][0][4:] + listacomdata[x][1][0][2:4] + listacomdata[x][1][0][0:2]) > int(listacomdata[x+1][1][0][4:] + listacomdata[x+1][1][0][2:4] + listacomdata[x+1][1][0][0:2]): 
        itenstmp = listacomdata[x+1]
        listacomdata[x+1] = listacomdata[x]
        listacomdata[x] = itenstmp
  #print(listacomdata)
  for i in range(0,len(listacomdata)):
    for x in range(0,len(listacomdata)-1):
      if int(listacomdata[x][1][0]) == int(listacomdata[x+1][1][0]):
        if (listacomdata[x][1][1]== '' and listacomdata[x+1][1][1] != ''): #or (int(listacomdata[x][1][1]) > int(listacomdata[x+1][1][1])):
          itenstmp = listacomdata[x+1]
          listacomdata[x+1] = listacomdata[x]
          listacomdata[x] = itenstmp
  listasemdataehora = []
  listacomhora = []
  for s in listaaux:
    if s[1][1] == '':
      listasemdataehora.append(s)
    elif s[1][1] != '':
      listacomhora.append(s)
  for i in range(0,len(listacomhora)):
    for x in range(0,len(listacomhora)-1):
      if listacomhora[x][1][1] > listacomhora[x+1][1][1]:
        itenstmp = listacomhora[x+1]
        listacomhora[x+1] = listacomhora[x]
        listacomhora[x] = itenstmp
  semiordenadas = listacomhora + listasemdataehora
  ordenadas = listacomdata + semiordenadas
  return ordenadas
  
def ordenarPorPrioridade(itens):  #Utilizando os mesmos métodos da ordenacao das datas e horas
  listasempri = []                #Verificando se há prioridades ou nao, depois utilizando um bubble
  listacompri = []                #para ordenar as prioridades na lista que tem as tuplas com pri
  for i in itens:                 #depois verifica se há tuplas com pri iguais com um while, e concatena 
    if i[1][2] == '':             #a lista com prioridades com a lista que n tem prioridades
      listasempri.append(i)       
    elif i[1][2] != '':           
      listacompri.append(i)       
                                  
  for i in range(0,len(listacompri)):
    for x in range(0,len(listacompri)-1):
      if listacompri[x][1][2] > listacompri[x+1][1][2]:
        itenstmp = listacompri[x+1]
        listacompri[x+1] = listacompri[x]
        listacompri[x] = itenstmp
        
  z = 0
  while z < len(listacompri):
    if listacompri[x][1][2] == listacompri[x+1][1][2]:
      ordenarPorDataHora(listacompri)
    z = z + 1
  ordefinal = listacompri + listasempri

  return ordefinal  

def fazer(num):
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)     #Ordena a função por data e hora, e depois por prioridade
  todo.close()                    
  listagem = ordenarPorDataHora(itens)  
  ordenacao = ordenarPorPrioridade(listagem)  
  if int(num) <= len(ordenacao):      #Depois verifica se a tarefa desejada existe, se sim adiciona a mesma
    tarefafeita = ordenacao[int(num)] #a tarefafeita, abre o arquivo done, formata a tarefa feita e a escreve
    done = open("done.txt", "a")      #no arquivo done e apaga a tupla da tal tarefa do arquivo todo
    ftarefa = tarefafeita[1][0] + " " + tarefafeita[1][1] + " " + tarefafeita[1][2] + " " + tarefafeita[0] + " " + tarefafeita[1][3] + " " + tarefafeita[1][4]
    done.write(ftarefa)
    done.close()
    del ordenacao[int(num)]
    #print(ordenacao)
    todo = open("todo.txt", "w") 
    for i in ordenacao:              #Após isso usa um for para reescrever o arquivo novamente, sem
      tarefa = ""                    #aquela tarefa retirada anteriormente
      if dataValida(i[1][0]) == True:
        tarefa = tarefa + " " + i[1][0]
      if horaValida(i[1][1]) == True:
        tarefa = tarefa + " " + i[1][1]
      if prioridadeValida(i[1][2]) == True:
        tarefa = tarefa + " " + i[1][2]
      if i[0] != '':
        tarefa = tarefa + " " + i[0]
      if contextoValido(i[1][3]) == True:
        tarefa = tarefa + " " + i[1][3]
      if projetoValido(i[1][4]) == True:
        tarefa = tarefa + " " + i[1][4]
      todo.write(tarefa  + "\n")
    todo.close()

  try: 
    fp = open(ARCHIVE_FILE, 'a')
    fp.write("" + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + ARCHIVE_FILE)
    print(err)
    return False
  


  return 

def remover(numero):
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)
  todo.close()
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  if int(numero) <= len(ordenacao) - 1: #Verifica se a tarefa existe, com -1, pq as tarefas começam do 0
    ordenacao.pop(int(numero))          #retira a tarefa daquele numero desejado, e depois usa um for
    todo = open("todo.txt", "w")        #para reescrever o arquivo sem aquela tarefa removida
    for i in ordenacao:                 #adicionando cada linha da tarefa a uma var e escrevendo a mesma
      tarefa = ""                       #no arquivo, caso n tenha a tarefa, printa o numero n foi encontrado
      if dataValida(i[1][0]) == True:
        tarefa = tarefa + " " + i[1][0]
      if horaValida(i[1][1]) == True:
        tarefa = tarefa + " " + i[1][1]
      if prioridadeValida(i[1][2]) == True:
        tarefa = tarefa + " " + i[1][2]
      if i[0] != '':
        tarefa = tarefa + " " + i[0]
      if contextoValido(i[1][3]) == True:
        tarefa = tarefa + " " + i[1][3]
      if projetoValido(i[1][4]) == True:
        tarefa = tarefa + " " + i[1][4]
      todo.write(tarefa  + "\n")
    todo.close()
  
  else:
    print("Número de tarefa não encontrado!")

  return

 
def priorizar(num, prioridade):
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)
  todo.close()
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  if int(num) <= len(ordenacao) - 1:
    tupleaux = (ordenacao[int(num)][0], (ordenacao[int(num)][1][0], ordenacao[int(num)][1][1], prioridade.upper() , ordenacao[int(num)][1][3], ordenacao[int(num)][1][4]))
    ordenacao[int(num)] = tupleaux
    todo = open("todo.txt", "w")          #Usa uma tupla auxiliar para pegar a linha com as partes antigas
    for i in ordenacao:                   #e a prioridade nova, e adiciona essa tupla para a lista ordenacao
      tarefa = ""                         #e do mesmo metodo das funções anteriores reescreve as tarefas
      if dataValida(i[1][0]) == True:     #no arquivo, caso n tenha essa tarefa printa que a tarefa n foi 
        tarefa = tarefa + " " + i[1][0]   #encontrada
      if horaValida(i[1][1]) == True:
        tarefa = tarefa + " " + i[1][1]
      if prioridadeValida(i[1][2]) == True:
        tarefa = tarefa + " " + i[1][2]
      if i[0] != '':
        tarefa = tarefa + " " + i[0]
      if contextoValido(i[1][3]) == True:
        tarefa = tarefa + " " + i[1][3]
      if projetoValido(i[1][4]) == True:
        tarefa = tarefa + " " + i[1][4]
      todo.write(tarefa  + "\n")
    todo.close()
  else:
    print("Número de tarefa não encontrado!")
  
  

  return 

# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos. 
def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
  
  elif comandos[1] == LISTAR:
    listagem = listar()
    return listagem    

  elif comandos[1] == REMOVER:    
    if soDigitos(comandos[2]) == True:  #Verifica se o numero digitado para remoção é um digito
      remover(comandos[2])              #se for usa a função remover , se não printa erro
    else:
      print("Número do comando inválido")
    return     


  elif comandos[1] == FAZER:
    if soDigitos(comandos[2]) == True:  #Mesmo modo da função remover, se for chama a função fazer
      fazer(comandos[2])
    return    

    

  elif comandos[1] == PRIORIZAR:  #Verifica se o num é um digito e se o comando 3 é uma pri valida, e chama priorizar
    if soDigitos(comandos[2]) == True and prioridadeValida("("+ comandos[3] + ")" ) == True:
      priorizar(comandos[2], "("+ comandos[3] + ")")
    else:
      print("Comando de priorização inválida")
    return    

    

  else :
    print("Comando inválido.")
    
  
# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#
# ['agenda.py', 'a', 'Mudar', 'de', 'nome']
processarComandos(sys.argv)
