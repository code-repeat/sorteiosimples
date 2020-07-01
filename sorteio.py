#  importing modules
from random import choices

#  Program cover
print("*"*50)
print("-------------SORTEIO SIMPLES----------------------")
print("*"*50)

#  Verify if the user only types a integer number
quant_names = ''
while type(quant_names) != int:
    print("Quantos nomes você deseja adcionar na lista? ")
    quant_names = input()
    try:
        int(quant_names)
        break
    except ValueError:
        print("SOMENTE NÚMEROS")

box_itens = []

#  This code below runs according to the user answer
for i in range(int(quant_names)):
    item = input(f"Item {i}: ")
    box_itens.append(item)

draw_numbers = int(input("Quantos itens você deseja sortear? "))

if draw_numbers > len(box_itens):
    print("Digite um valor menor")
else:
    selected = choices(box_itens, k=int(draw_numbers))
    print(', '.join(selected))




