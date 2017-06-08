"""def horaValida(horaMin) :
  if len(horaMin) != 4: #or not soDigitos(horaMin):
    return False
  else:
    tupla1 = int(horaMin[0]),int(horaMin[1])
    doisPdig = ""
    for i in tupla1:
      doisPdig = doisPdig + str(i)
    tupla2 = int(horaMin[2]), int(horaMin[3])
    doisSdig = ""
    for i in tupla2:
      doisSdig = doisSdig + str(i)    
    if (int(doisPdig) >= 00 and int(doisPdig) <= 23) and (int(doisSdig) >= 00 and int(doisSdig) <= 59):    
      return True
    else:
      return False

def horaValida(horamin):
  e = int(horamin[0]),int(horamin[1])
  d = "" 
  for i in e:
    d = d + str(i)
  return int(d)  
 """ 
"""  
def dataValida(data):
  if len(data) != 8: # or not soDigitos(data):
    return False
  else:
    tupla1 = int(data[0]),int(data[1])
    dias = ""
    for i in tupla1:
      dias = dias + str(i)

    tupla2 = int(data[2]),int(data[3])
    mes = ""
    for i in tupla2:
      mes = mes + str(i)
    #print(mes)
    tupla3 = int(data[4]), int(data[5]), int(data[6]), int(data[7])
    ano = ""
    for i in tupla3:
      ano = ano + str(i)

    if int(mes) >= 1 and int(mes) <= 12:
      #return True       
      if int(mes) == 2:
        if int(dias) >= 1 and int(dias) <= 29:
          return True
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
    #return True      
"""

"""def projetoValido(proj):
  if len(proj) >= 2:
    if proj[0] == "+":
      return True
    else:
      return False    
  else:
    return False
"""


"""def contextoValido(cont):
  if len(cont) >= 2:
    if cont[0] == "@":
      return True
    else:
      return False
  else:
    return False    
"""

import string
def prioridadeValida(pri):
  if len(pri) != 3:
    return False
  else:
    if pri[0] == "(" and pri[2] == ")":
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
"""
import string
letras = list(string.ascii_lowercase)
print (letras)

for i in letras:
  print(i.upper())
  if i == "a":
    print("aQUI SEU I" , i)
"""
































  



