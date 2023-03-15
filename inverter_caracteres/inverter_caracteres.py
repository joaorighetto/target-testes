string = input("Digite o que quer inverter: ")

lista_de_caracteres = [char for char in string]

ultimo_indice = len(lista_de_caracteres) - 1

resultado = [lista_de_caracteres[i] for i in range(ultimo_indice, -1, -1)]

print("".join(resultado))

