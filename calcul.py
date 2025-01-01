

print("Bienvenue ! Ceci est une calculatrice simple.")
print("Choisissez une opération :")
print("1 : Addition")
print("2 : Soustraction")
print("3 : Multiplication")
print("4 : Division")
operation = input("Entrez le numéro de l'opération (1/2/3/4) : ")
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
if operation == "1":
    resultat = nombre1 + nombre2
    print("Le résultat est : ", resultat)
elif operation == "2":
    resultat = nombre1 - nombre2
    print("Le résultat est : ", resultat)
elif operation == "3":
    resultat = nombre1 * nombre2
    print("Le résultat est : ", resultat)
elif operation == "4":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        print("Le résultat est : ", resultat)
    else:
        print("Erreur : Division par zéro impossible.")
else:
    print("Choix invalide. Veuillez réessayer.")

