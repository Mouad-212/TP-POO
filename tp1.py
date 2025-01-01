# Exercice 1
print("Bonjour")


# Exercice 2
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
print("Le produit des deux nombres est :", a * b)


# Exercice 3
a = int(input("Entrez le premier entier (A) : "))
b = int(input("Entrez le deuxième entier (B) : "))
a, b = b, a
print("Après échange : A =", a, ", B =", b)


# Exercice 4
n = int(input("Entrez un nombre entier : "))
if n % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

# Exercice 5
a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))
c = int(input("Entrez le troisième entier : "))
print("Le plus grand nombre est :", max(a, b, c))

# Exercice 6
note = float(input("Entrez une note (entre 0 et 20) : "))
if 0 <= note <= 20:
    if note >= 10:
        print("Validé")
    else:
        print("Non validé")
else:
    print("Note invalide, veuillez entrer une note entre 0 et 20.")

# Exercice 7
m = float(input("Entrez le premier nombre : "))
n = float(input("Entrez le deuxième nombre : "))
produit = m * n
if produit > 0:
    print("Le produit est positif.")
elif produit < 0:
    print("Le produit est négatif.")
else:
    print("Le produit est nul.")
          
# Exercice 8
n = int(input("Entrez un entier : "))
valeur_absolue = abs(n)-
print("La valeur absolue de", n, "est :", valeur_absolue)

# Exercice 9
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
c = float(input("Entrez le troisième nombre : "))
moyenne = (a + b + c) / 3
print("La moyenne est :", moyenne)

# Exercice 10
prix_HT = float(input("Entrez le prix total HT : "))
if prix_HT > 200:
    prix_HT *= 0.85  # Application de la réduction de 15%
prix_TTC = prix_HT * 1.2  # Application de la TVA à 20%
print("Le montant TTC est :", round(prix_TTC, 2))

# Exercice 11
nb_photos = int(input("Entrez le nombre de photocopies : "))
if nb_photos <= 10:
    facture = nb_photos * 0.25
elif nb_photos <= 30:
    facture = 10 * 0.25 + (nb_photos - 10) * 0.20
else:
    facture = 10 * 0.25 + 20 * 0.20 + (nb_photos - 30) * 0.10
print("Le montant total de la facture est :", round(facture, 2), "DH")

# Exercice 12
age = int(input("Entrez l'âge de l'enfant : "))
if 6 <= age <= 7:
    print("Catégorie : poussin")
elif 8 <= age <= 9:
    print("Catégorie : pupille")
elif 10 <= age <= 11:
    print("Catégorie : minime")
elif age >= 12:
    print("Catégorie : cadet")
else:
    print("Âge non catégorisé.")

# Exercice 13
mois_num = int(input("Entrez le numéro du mois (1-12) : "))
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
if 1 <= mois_num <= 12:
    print("Le mois correspondant est :", mois[mois_num - 1])
else:
    print("Numéro invalide. Veuillez entrer un nombre entre 1 et 12.")

