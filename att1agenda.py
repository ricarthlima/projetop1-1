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
  

# Adiciona um compromisso aa agenda. Um compromisso tem no minimo
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

  # não é possível adicionar uma atividade que não possui descrição. 
  if descricao  == '' :
    return False
  

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
        else:                      
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
def organizar(linhas):
  itens = []

  for l in linhas:
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras

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

  ################ COMPLETAR
  return 

def ordenarPorDataHora(itens):

  ################ COMPLETAR

  return itens
   
def ordenarPorPrioridade(itens):

  ################ COMPLETAR

  return itens

def fazer(num):

  ################ COMPLETAR

  return 

def remover():

  ################ COMPLETAR

  return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(num, prioridade):

  ################ COMPLETAR

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
    return    
    ################ COMPLETAR

  elif comandos[1] == REMOVER:
    return    

    ################ COMPLETAR    

  elif comandos[1] == FAZER:
    return    

    ################ COMPLETAR

  elif comandos[1] == PRIORIZAR:
    return    

    ################ COMPLETAR

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
