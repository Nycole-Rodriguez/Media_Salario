# Ler Salario_base e Gratificacao

Salario_base = float(input("Digite Salario_base:"))
Gratificacao = float(input("Digite Gratificacao:"))

#Calcular o Salario_bruto
Salario_bruto = Salario_base + Gratificacao

#calcular Imposto_de_Renda
if Salario_bruto < 1000:

    Imposto_Imposto_de_rendade_renda = Salario_bruto * 15/100
else:
    Imposto_renda = Salario_bruto * 20/100

    #Calcular o Salario_Liquido
    Salario_Liquido = Salario_bruto - Imposto_renda

    #Exibir o Salario_Liquido
    print(f" O salario líquido é: {Salario_Liquido}")
