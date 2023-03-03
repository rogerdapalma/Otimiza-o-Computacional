import re #expressao regular (regular expression)

nomesVariaveis = {} #dicionario com o nome das variaveis

def insereVariavel(variavel):
  if variavel not in nomesVariaveis:
    nomesVariaveis[variavel]='sim'

def separaCoef_var(termo):
  coef = ''
  variavel = ''
  indice=0
  for letra in termo:
    if(letra.isdigit()):
      coef=coef+letra
      indice+=1 #incrementa o indice
    else:
      if indice==0:#a primeira letra nao eh numero
        coef='1'
      variavel = termo[indice:]
      break #sai do for
  return coef,variavel


def abre_arquivo(nomeArquivo):
  dados = open(nomeArquivo)
  for linha in dados:#percorre linha a linha o arquivo
    print(linha)
    elementos = linha.split('=')#quebra a linha no igual
    le = elementos[0]
    ld = elementos[1]
    #print('LE:',le,'LD:',ld)
    #iremos quebrar o lado esquerdo pelos simbolos + e -
    if le.find('-')>=0 and le.find('+')>=0:
      termos = re.split('-|\+',le)
      for termo in termos:
        print('***',termo)
      continue #sai do iteracao
    if le.find('+')>0:#busco o sinal de + no le
      variaveisP = le.split('+')
      print('Variaveis (+)->',variaveisP[0],'|',variaveisP[1])
      c,v = separaCoef_var(variaveisP[0])
      insereVariavel(v)
      c,v = separaCoef_var(variaveisP[1])
      insereVariavel(v)
    if le.find('-')>=0:#busco o sinal de - no le
      variaveisN = le.split('-')
      #print('num de -:',len(variaveisN))
      if len(variaveisN)==2:
        print('Variaveis (-)->',variaveisN[0],'|',variaveisN[1])
        c,v = separaCoef_var(variaveisN[0])
        insereVariavel(v)
        c,v = separaCoef_var(variaveisN[1])
        insereVariavel(v)
      elif len(variaveisN)==3:
        
        print('Variaveis (-)->',variaveisN[1],'|',variaveisN[2])
        c,v = separaCoef_var(variaveisN[1])
        insereVariavel(v)
        c,v = separaCoef_var(variaveisN[2])
        insereVariavel(v)
    print(nomesVariaveis.keys())

abre_arquivo('/content/drive/MyDrive/otimização/equacoes.txt')#muda com o caminho correto
c,v = separaCoef_var('x1')
print('Coeficiente: ',c,'Variavel:',v)