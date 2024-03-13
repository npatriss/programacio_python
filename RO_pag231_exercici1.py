#RO_pag231_exercici1.py

def articles(n):
    preus = []
    print("Introdueix els preus dels", n, "artcles:")
    for i in range(n):
        preu = float(input("Preu de l'article: "))
        preus.append(preu)

    diners = float(input("Ingresa la cantitat de diners disponibles: "))

    print("a) Articles que pots comprar:")
    for i in range(n):
        if preus[i] <= diners:
            print("Article", i + 1)

    print("b) Unitats que pots comprar de cada article:")
    for i in range(n):
        if preus[i] < diners:
            unitats = diners // preus[i]
            print("Pots comprar", unitats, "unitats de l'article", i + 1)

n = int(input("Ingresa la cantitat d'articles: "))
articles(n)