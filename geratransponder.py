import random as rd

lista_removidos = [1000,2000,7000,7500,7600,7700]
codigos_transponder = []

for numero in range(1,7778):
    if "8" in str(numero):
        continue
    elif "9" in str(numero):
        continue
    else:
        if len(str(numero)) == 4:
            codigos_transponder.append(numero)
        else:
            codigos_transponder.append("0"*(4 - len(str(numero)))+str(numero))

for remover in lista_removidos:
    codigos_transponder.remove(remover)

print(f"O seu código transponder será {codigos_transponder[rd.randint(0,len(codigos_transponder))]}")

