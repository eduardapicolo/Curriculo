#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:29:50 2024

@author: duda
"""

num1 = 0
num2 = 0
num3 = 0
num4 = 0
soma = 0
nums_considerados = 0
nums_desconsiderados = 0
cont_num = 0
cont_zero = 0
print('Bem Vindo ao Zero Cancela')
regras = str(input('Gostaria de saber as regras do jogo? \n[Sim] [Não]\n'))
if(regras.lower() == 'sim'):
    print ('Regras do Jogo:')
    print ('digite números para o sistema somar;')
    print ('Digite "0" para desconsiderar o último número digitado;')
    print ('O usuário pode digitar apenas 3 vezes consecutivas o número "0" para desconsiderar os três últimos números digitados;')
    print ('A inserção é finalizada quando um número negativo é digitado.')
print ('Tudo pronto, digite um número para começar!')
while(num1>=0):
    num1 = int(input('Número: '))
    if(num1 == 0 and cont_zero >= 3):
        print('Só é permitido até 3 zeros consecutivos!!!') 
    if(num1>0):
        num4 = num3
        num3 = num2
        num2 = num1
        nums_considerados += 1
        soma += num1
        cont_num += 1
        cont_zero = 0
    if(num1 == 0 and cont_num > 0 and cont_zero < 3):
        cont_zero += 1
        if(num2 != 0):
            print (f' número {num2} desconsiderado, digite novamente')
            nums_desconsiderados += 1
            nums_considerados -= 1
            soma -= num2
            num2 = num3
            num3 = num4
            num4 = 0
        else:
            print('Não há números para serem apagados!')
    elif(num1 == 0 and cont_num <= 0):
        print('Não há números para serem apagados!') 
print(f'Soma dos números - {soma} \nNúmeros considerados - {nums_considerados} \nNúmeros desconsiderados - {nums_desconsiderados}')