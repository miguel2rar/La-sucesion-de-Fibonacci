"""ESCRIBE UN PROGRAMA QUE ESCRIBA LOS 50 PRIMEROS NUMEROS DE LA SUCESION DE FIBONACCI EMPEZANDO EN
0

-LA SERIE DE FIBONACCI SE COMPONE POR UNA SUCESION DE NUMEROS EN LA QUE EL SIGUIENTE SIEMPRE ES LA
SUMA DE LOS DOS ANTERIORES
0, 1, 1, 2, 3, 5, 8, 13..."""


lista3 = [0,1]

for e in range (0, 48):
    a3= lista3[e]+lista3[e+1]
    lista3.append(a3)
    if e == 47:
        for u in range (0, len(lista3)):
            print(lista3[u])