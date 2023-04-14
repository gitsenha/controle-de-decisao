''# Elabore um algoritimo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

n = int(input("Dijite sua idade:"))

if n < 5:
    print(f"Você é menor de idade, não pode participar")
elif n >= 5 and n <= 7:
    print(f"A idade do nadador é", n, "anos, esta classificado para a Infantil A.")
elif n >= 8 and n <= 10:
    print(f"A idade do nadador é", n, "anos, esta classificado para a Infantil B.")
elif n >= 11 and n <= 13:
    print(f"A idade do nadador é", n, "anos, esta classificado para a Juvenil A.")
elif n >= 14 and n <= 17:
    print(f"A idade do nadador é", n, "anos, esta classificado para a Juvenil B.")
else:
    n > 18
    print(f"A idade do nadador é", n, "anos, esta classificado como Adulto.")
