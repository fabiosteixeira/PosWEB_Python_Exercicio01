#-*-coding:utf-8-*-
import os
# from sys import platform
import sys

clearCommand = "clear"
if sys.platform == "win32":
    clearCommand = "cls"

os.system(clearCommand)
print("--- EXERCICIO 01 ---")

print("\n--- Exemplo de SET --")
# SET é uma coleção desordenada e não indexada. Em Python, ela é escrita entre "Chaves":
frutas = {"maça", "banana", "abacate", "amora", "melancia", "abacaxi"}
print(frutas)

print("\n--- Exemplo de TUPLA --")
"""
TUPLA é uma lista imutável. O que diferencia uma lista de uma tupla é que a primeira pode ter elementos adicionados
a qualquer momento enquanto, no caso da tupla, após definida, não é permitida adição ou remoção de elementos
A essência das tuplas é serem sequências de dados heterogêneos.
"""
coordenadas = ("x", "y", 10, 20, "c")
print(coordenadas)
print("\n--- Interando uma TUPLA --")
for item in enumerate(coordenadas):
    print(item)


print("\n\nDigite 's' para rodar as demais simulações ou qualquer outro valor para finalizar a aplicação:")
text = input()

if text != 's':
    exit()

print("\n\n--- SIMULAÇÕES DIVERSAS ---")

def somar(a, b):
    c = a + b
    return c

#Declaração inline - Com utilização do ;
x = 3; y = 5

print("\n--- Utilizando a função somar:")
print("A soma é:", somar(x,y))

txt = "IDEAGRI"

#Operações com strings
#Total de caracteres
print("\n\n--- Operações com strings --")
print("- len:")
print(len(txt))
#Substring
print("- Substring:")
print("IDEAGRI"[3:5])
#Retorna arrays a partir do separador informado
print("- Split:")
print(txt.split("A"))
print(txt.split())
# Pega a string completa (: - posição inicial e : posição final) e inverte a leitura utilizando o -1
print("- Invertendo a leitura de uma lista ou string:")
print(txt[::-1])

# Declaração de objetos (dicionários)
print("\n\n--- Dicionários --")
dic = {"fabio":37, "alexa":18}
# Interando sobre dicionário
print("- Retornando valor do dicionário:")
print(dic["fabio"])
print("- Interando um dicionário:")
for i in dic:
    print(dic[i])
# Interando sobre dicionário acessando itens completos
print("- Interando sobre um dicionário buscando os itens completos:")
for item in dic.items():
    print(item)

# Representação de classe
print("\n\n--- Representação de clases --")
class Animal:
    tipo = "animal"
    # Declaração de atributos privados
    _planeta = "terra"

class Cachorro(Animal):
    especie = "canino"
    # O construtor é declado desse jeito:
    def __init__(self, name):
        self.name = name

# Instanciando classes e passando atributos a partir do construtor
d = Cachorro("Trambique")
print("- Exibindo classe Cachorro herdada da classe Animal")
print(d.name, d.tipo)

# List Enumerate - Retornando o dado e a posição
print("\n\n--- Enumerate --")
for i, dado in enumerate(dic):
    print("Posição", i, "contém", dado)

# List comprehension
print("\n\n--- Comprehension --")
lista1 = [1,2,4,5,3]
# Aplicando operação em todos os itens da lista 1
lista2 = [i**2 for i in lista1]
print("- Aplicando uma operação em todos os itens de uma lista:")
print(lista2)
# Aplicando operações matemáticas ao interar uma lista
print("- Aplicando uma operação matemática em todos os itens de uma lista:")
lista3=[i for i in lista1 if i%2 == 1]
print(lista3)

print("\n\n--- Map --")
def func(a):
    return a**2
# O map aplica uma função a todos os itens de uma determinada lista
print("- Aplicando uma função a todos os itens de uma lista utilizando o map")
# Como o retorno é um objeto genérico, é necessário fazer a conversão explícia para a lista:
lista4 = list(map(func, lista3))
print(lista4)
