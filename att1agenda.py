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

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

# Adiciona um compromisso a agenda. Um compromisso tem no minimo
# uma descrição. Adicionalmente, pode ter, em caráter opcional, uma
# data (formato DDMMAAAA), um horário (formato HHMM), uma prioridade de A a Z, 
# um contexto onde a atividade será realizada (precedido pelo caractere
# '@') e um projeto do qual faz parte (precedido pelo caractere '+'). Esses
# itens opcionais são os elementos da tupla "extras", o segundo parâmetro da
# função.
#
# extras ~ (data, hora, prioridade, contexto, projeto)
#
# Qualquer elemento da tupla que contenha um string vazio ('') não
# deve ser levado em consideração. 
def adicionar(descricao, extras):

   
  if descricao  == '':                                              #Caso não houver uma descrição, a função não será utilizada,
    return False                                                    #Se houver uma descrição uma variável receberá a nova atividade
  else:                                                             #o arquivo é aberto no modo a, para não sobrescrever, e são 
    novaAtividade = ""                                              #feitas as verificaçãoes de validação para as partes das tarefas
    todo = open("todo.txt", "a")                                    #e posteriormente adicionadas a varaivél novaAtividade se forem
    if dataValida(extras[0]) == True:                               #validadas
      novaAtividade = novaAtividade + extras[0] + " "
    if horaValida(extras[1]) == True:
      novaAtividade = novaAtividade + extras[1] + " "
    if prioridadeValida(extras[2].upper()) == True:
      novaAtividade = novaAtividade + extras[2] + " "
    if descricao != '':
      novaAtividade = novaAtividade + descricao + " "
    if contextoValido(extras[3]) == True:
      novaAtividade = novaAtividade + extras[3] + " "
    if projetoValido(extras[4]) == True:
      novaAtividade = novaAtividade + extras[4]
    todo.close()

  ################ COMPLETAR


  # Escreve no TODO_FILE. 
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  return True


# Valida a prioridade.
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


# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil, ao invés
# de dois blocos de 12 (AM e PM), como nos EUA.
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

# Valida datas. Verificar inclusive se não estamos tentando
# colocar 31 dias em fevereiro. Não precisamos nos certificar, porém,
# de que um ano é bissexto. 
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

# Valida que o string do projeto está no formato correto. 
def projetoValido(proj):    #Verifica se o tamanho da str não é menor que 2
  if len(proj) >= 2:        #Caso não, retorna False
    if proj[0] == "+":      #Se tamanho não é menor que 2, verifica se o primeiro char é "+"
      return True           #Se sim devolve True, caso não devolve False
    else:
      return False    
  else:
    return False

# Valida que o string do contexto está no formato correto. 
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


# Dadas as linhas de texto obtidas a partir do arquivo texto todo.txt, devolve
# uma lista de tuplas contendo os pedaços de cada linha, conforme o seguinte
# formato:
#
# (descrição, prioridade, (data, hora, contexto, projeto))
#
# É importante lembrar que linhas do arquivo todo.txt devem estar organizadas de acordo com o
# seguinte formato:
#
# DDMMAAAA HHMM (P) DESC @CONTEXT +PROJ
#
# Todos os itens menos DESC são opcionais. Se qualquer um deles estiver fora do formato, por exemplo,
# data que não tem todos os componentes ou prioridade com mais de um caractere (além dos parênteses),
# tudo que vier depois será considerado parte da descrição.  


linhas = ""
def organizar(linhas):                        
  todo = open("todo.txt", "r")                 #Variavel que abre o arquivo no modo de leitura,depois o adiciona a uma var
  arquivo = todo.read()                        #Depois a variavel linhas recebe esse arquivo em forma de listas, com cada linha
  linhas = arquivo.splitlines()                #um elemento da mesma                          
  todo.close()
  
  
                                              #Usando a função organizar, a mesma recebe essa lista de linhas
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

        
    # Processa os tokens um a um, verificando se são as partes da atividade.
    # Por exemplo, se o primeiro token é uma data válida, deve ser guardado
    # na variável data e posteriormente removido a lista de tokens. Feito isso,
    # é só repetir o processo verificando se o primeiro token é uma hora. Depois,
    # faz-se o mesmo para prioridade. Neste ponto, verifica-se os últimos tokens
    # para saber se são contexto e/ou projeto. Quando isso terminar, o que sobrar
    # corresponde à descrição. É só transformar a lista de tokens em um string e
    # construir a tupla com as informações disponíveis. 

    ################ COMPLETAR

    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens


# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados). 
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém. 
def listar():
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)
  todo.close()
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  #print(ordenacao)
  i = 0
  while i < len(ordenacao):
    saida = ""
    if ordenacao[i][1][0] != '':
      a = ordenacao[i][1][0]
      saida = saida + a[0]+a[1]+"/"+a[2]+a[3]+"/"+a[4]+a[5]+a[6]+a[7] + " "
    if ordenacao[i][1][1] != '':
      h = ordenacao[i][1][1]
      saida = saida + h[0]+h[1]+"h"+h[2]+h[3]+"m"
      
    if ordenacao[i][1][2] == "(a)" or ordenacao[i][1][2] == "(A)":
      print(BOLD + YELLOW + str(str(i) + " " + saida +  " " + ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]))
    if ordenacao[i][1][2] == "(b)" or ordenacao[i][1][2] == "(B)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RED)
    if ordenacao[i][1][2] == "(c)" or ordenacao[i][1][2] == "(C)":
      printCores(str(str(i) + " " + saida + " "  +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), BLUE)
    if ordenacao[i][1][2] == "(d)" or ordenacao[i][1][2] == "(D)":
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), CYAN)
    if ordenacao[i][1][2] == '':
      printCores(str(str(i) + " " + saida + " " +  ordenacao[i][1][2] + " " + ordenacao[i][0] + " " + ordenacao[i][1][3] + " " + ordenacao[i][1][4]), RESET)
    i = i + 1     
  return

"""def checardata(itens):           #Função que faz a checagem da data, se a data de cada tupla for um str vazio,
  listaaux = []                  #adiciona essa tupla para a lista auxiliar, e remove essa tupla de da lista geral(itens)     
  i = 0                          #Depois de rodar toda a lista itens, a variavél po(ponto ótimo) recebe o tamanho da lista 
  while i < len(itens):          #com os que não tem data removidos, e no final a lista itens vai receber ela mesma 
    if itens[i][1][0] == "":     #mais a listaaux com as tuplas que não tem data, assim movendo as tuplas sem datas 
      listaaux.append(itens[i])  #pro final, e devolvendo a lista de itens e o po para ser usado na função 
      itens.pop(i)               #OrdenarPorDataHora
      i = i - 1   
    i = i + 1
  po = len(itens)
  itens = itens + listaaux  
  return (itens,po)



def ordenarHora(itens):          #Usa o bubble sort para ordenar as tuplas por hora caso as datas das tarefas sejam iguais 
  #print("ITENS ANTERIOR:", itens)
  for i in range(0,len(itens)):
    for x in range(0,len(itens) - 1):
      if int(itens[i][1][0][4:] + itens[i][1][0][2:4] + itens[i][1][0][0:2]) == int(itens[x][1][0][4:] + itens[x][1][0][2:4] + itens[x][1][0][0:2]):
        if (itens[i][1][1] == "" and  itens[x][1][1] != "") or (itens[i][1][1] < itens[x][1][1]):
          #print("OK!")
          #print(itens[i])
          #print(itens[x])
          itenstmp = itens[x]    #Se as datas do anterior e do próximo são iguais , 
          itens[x] = itens[i]    #se a hora do anterior é str vazio e do posterior não é ou se o anterior é menor que o posterior, inverte eles de 
          itens[i] = itenstmp    #posição que o bubble sorte devolve esses itens ordenados
  return itens     

def ordenarPorDataHora(itens):      #A função principal para a ordenação pro data e hora, utiliza primeiro a função checar data
  tuplaaux = checardata(itens[:])   #adiconando a var tuplaaux a devolução de checagem da data com uma copia de itens(segurança)
  itens = tuplaaux[0]               #e adiciona a itens o valor da primeira devolução de checardata e a po a segunda devolução 
  po = tuplaaux[1]
  
  for i in range(0, po):            #depois utiliza o bubble sort para organizar essas tuplas de acordo com suas datas utilizando a visão de 
    for x in range(0, po - 1):      #que ao inverter essas datas para AAAAMMDD elas podem ser comparadas entre maior e menor
      if int(itens[i][1][0][4:] + itens[i][1][0][2:4] + itens[i][1][0][0:2]) < int(itens[x][1][0][4:] + itens[x][1][0][2:4] + itens[x][1][0][0:2]):
        itenstmp = itens[x]
        itens[x] = itens[i]
        itens[i] = itenstmp  
  #if int(itens[i][1][0][4:] + itens[i][1][0][2:4] + itens[i][1][0][0:2]) == int(itens[x][1][0][4:] + itens[x][1][0][2:4] + itens[x][1][0][0:2]):
  itens = ordenarHora(itens[:po]) + itens[po:]    #Depois utiliza a função ordenarHora para fazer essa ordenação se datas são iguais
                                                  #dando como parametro os itens do começo até o po(qeu são as que tem data)  
                                                  #concatenado com os itens do po até o final e dps adicionando isso a itens

  return itens"""
  
def ordenarPorDataHora(itens):      #A função principal para a ordenação pro data e hora, utiliza primeiro a função checar data
  listaaux = []
  listacomdata = []
  for w in itens:
    if w[1][0] == "":
      listaaux.append(w)
    elif w[1][0] != "":
      listacomdata.append(w)
  #print(listaaux)
  #print(listacomdata)

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
  #print("LISTAAUX",listaaux)
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
  #print("LISTAPORHORA", listacomhora)      
  semiordenadas = listacomhora + listasemdataehora
  ordenadas = listacomdata + semiordenadas
  #for x in ordenadas:
    #print(x)
  return ordenadas
  
def ordenarPorPrioridade(itens):
  listasempri = []
  listacompri = []
  for i in itens:
    if i[1][2] == '':
      listasempri.append(i)
    elif i[1][2] != '':
      listacompri.append(i)
  #print(listacompri)
  #print(listasempri)
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
  #print("LISTAORDEPRI",listacompri)
  ordefinal = listacompri + listasempri
  #for x in ordefinal:
    #print(x)

  return ordefinal  

"""def checarprioridade(itens):
  priaux = []
  i = 0
  while i < len(itens):
    if itens[i][1][2] == "":
      priaux.append(itens[i])
      itens.pop(i)
      i = i - 1
    i = i + 1
  po = len(itens)
  itens = itens + priaux
  return (itens, po)

def checapriiguais(itens):
  for i in range(0,len(itens)):
    for x in range(0,len(itens) - 1):
      if itens[i][1][2] == itens[x][1][2]:
        #print(itens[i][1][2])
        #print(itens[x][1][2])
        ordenarPorDataHora(itens)
  return itens  


#itens = ordenarPorDataHora(organizar(linhas))
def ordenarPorPrioridade(itens):
  tuplaaux = checarprioridade(itens[:])
  itens = tuplaaux[0]
  po = tuplaaux[1]
  for i in range(0, po):
    for x in range(0, po - 1):
      if itens[i][1][2] < itens[x][1][2]:
        itenstmp = itens[x]
        itens[x] = itens[i]
        itens[i] = itenstmp
  itens = checapriiguais(itens)      
  return itens"""

def fazer(num):
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)
  todo.close()
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  if int(num) <= len(ordenacao):
    tarefafeita = ordenacao[int(num)]
    done = open("done.txt", "a")
    ftarefa = tarefafeita[1][0] + " " + tarefafeita[1][1] + " " + tarefafeita[1][2] + " " + tarefafeita[0] + " " + tarefafeita[1][3] + " " + tarefafeita[1][4]
    done.write(ftarefa)
    done.close()
    del ordenacao[int(num)]
    print(ordenacao)
    todo = open("todo.txt", "w") 
    for i in ordenacao:
      tarefa = ""
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
    fp.write(ftarefa + "\n")
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
  if int(numero) <= len(ordenacao) - 1:
    ordenacao.pop(int(numero))
    todo = open("todo.txt", "w") 
    for i in ordenacao:
      tarefa = ""
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
    #print(ordenacao)
    #print("ok")
    todo.close()
  
  
  
  
  
  
  else:
    print("Número de tarefa não encontrado!")

  return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(num, prioridade):
  todo = open("todo.txt", "r")    #Pega o arquivo em modo leitura adicionando ele a uma variável, e depois
  arquivo = todo.read()           #adiciona a variável listastr essa variavel com o arquivo lido e dá um splitlines
  listastr = arquivo.splitlines() #separando o mesmo, depois usa a função organizar com o parametro listastr
  itens = organizar(listastr)
  todo.close()
  listagem = ordenarPorDataHora(itens)
  ordenacao = ordenarPorPrioridade(listagem)
  if int(num) <= len(ordenacao) - 1:
    #print(ordenacao[15][1][2])
    #print("desc aq", ordenacao[int(num)][0])
    tupleaux = (ordenacao[int(num)][0], (ordenacao[int(num)][1][0], ordenacao[int(num)][1][1], prioridade.upper() , ordenacao[int(num)][1][3], ordenacao[int(num)][1][4]))
    ordenacao[int(num)] = tupleaux
    #print(tupleaux)
    #print(ordenacao)    
    todo = open("todo.txt", "w") 
    for i in ordenacao:
      tarefa = ""
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
    ################ COMPLETAR

  elif comandos[1] == REMOVER:
    if soDigitos(comandos[2]) == True:
      remover(comandos[2])
    
    return     


  elif comandos[1] == FAZER:
    if soDigitos(comandos[2]) == True:  
      fazer(comandos[2])
    return    

    

  elif comandos[1] == PRIORIZAR:
    if soDigitos(comandos[2]) == True and prioridadeValida("("+ comandos[3] + ")" ) == True:
      priorizar(comandos[2], "("+ comandos[3] + ")")
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

#OK
"""  10052018 1200 (d) Fazer algo amanhã @cin
10052018 1100 (c) Pegar livro de calculo @bibliotecactg +ma026
20052017 2100 (b) Ir para casa @Timbauba
10072017 Fazer algo produtivo
21052017 2300 (a) Fazer algo hoje
10072017 2100 (d) Amistoso do time de futsal do cin @quadraNefd
22052017 1100 (b) Amistoso do time de futsal do cin @quadraNefd
1100 Ir pra casa
0900 Ir a praia         """
