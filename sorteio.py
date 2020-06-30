#  Módulo(s) necessário(s)
from random import choices

#  Capa do Programa
print("*"*50)
print("-------------SORTEIO SIMPLES----------------------")
print("*"*50)

quant_names = int(input("Quantos itens deseja adcionar na caixa de sorteio? "))
box_itens = []

for i in range(quant_names):
    item = input(f"Item {i}: ")
    box_itens.append(item)

draw_numbers = int(input("Quantos itens você deseja sortear? "))
if draw_numbers > len(box_itens):
    print("Digite um valor menor")
else:
    selected = choices(box_itens, k=int(draw_numbers))
    print(', '.join(selected))




