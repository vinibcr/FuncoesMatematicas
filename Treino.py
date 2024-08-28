from datetime import datetime, timedelta


#importar funções de outra pagina

#from Atribuicao import Soma

#definição de funções
def Soma (a,b):
    return a+b
   
def paridade (numero):
    numero = int(input("digite um numero: "))
    if numero % 2 == 0:
        return "par" 
    else:
        return "Impar"
    
def ContarCaracteres(s):
    return len(s.replace(" ",""))

def maior(Lista):
    return max(Lista)

def menor(Lista):
    return min (Lista)

def substituir_palavra(palavra, nova_palavra):
    texto = "eu gosto de batata frita"
    novo_texto = texto.replace(palavra, nova_palavra)
    return novo_texto

def fibonacci(n):
    resultado = []
    a, b = 0, 1
    while len(resultado) < n:
        resultado.append(a)
        a, b = b, a + b
    return resultado

def PosteriorEAnterior(numero):
    numero = int(input('Informe um número inteiro qualquer: '))
    print(f'O antecessor do número {numero} é {numero - 1}, e o sucessor é {numero + 1}')

def DuasCasas(numero):
    numero = int(input('Informe um número inteiro qualquer: '))
    print(f'Este número com duas casas decimais fica assim: {numero:.2f}')


def Datas():
    data_atual = datetime.now()
    data_futura = data_atual + timedelta(2)
    print(data_futura)

def nome(nome):
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}, muito prazer.')

def Temperatura():
    temperaturas_celsius = [22.5, 40, 13, 29, 34]
    temperaturas_fahrenheit = list(map(lambda temp: round((9 / 5) * temp + 32, 1), temperaturas_celsius))
    print(temperaturas_fahrenheit)

#variaveis com o resultado da operação
resultado = Soma(5,2)
parouimpart = paridade(2)

#print com as informações necessárias
print(Soma(3,4))
print (paridade())
print (ContarCaracteres(" asd ad asd  das aaaaaaa"))
print ("o maximo é",maior(Lista=([4,5,6,7,8,89])))
print ("o menor numero é", menor(Lista=([2,6,7,8,9])), "<-----")
print (substituir_palavra("batata", "beterraba"))
print(fibonacci(100))
PosteriorEAnterior(numero=4)
DuasCasas(numero=4)
Datas()
nome("Vinicius")

