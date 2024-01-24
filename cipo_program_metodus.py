from Cipo import Cipo

def pld_lista():

    peldany1 = Cipo("Nike", 42)
    peldany2 = Cipo("Adidas", 41)
    peldany3 = Cipo("Adidas", 45)
    peldany4 = Cipo("Jordan", 48)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    cipok.append(peldany4)

    return cipok


pld_lista()



def lista_kiir(lista):
    for i in range(0, len(lista), 1):
        nev: str = lista[i].nev
        meret: int = lista[i].meret
        print(f"{nev} ({meret})")




def osszegzes_tetel(cipok):
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret
#összegzés tétel
    atlag = ossz / len(cipok)
    print(round(atlag, 3))





def maximalis_tetel(cipok):
    print("melyik márka a legnagyobb? ", end="")
    helye: int = 0
    for i in range(1, len(cipok)):
        if cipok[i].meret > cipok[helye].meret:
            helye = i
    print(f"{cipok[helye].nev}")





def szamlalas(cipok):
    db: int = 0
    for i in range(len(cipok)):
        if cipok[i].nev == "Adidas":
            db += 1
    print(f"Ennyi db Adidas van: {db}")





def eldontes(cipok):
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True
#eldöntés tétel
    if van_nagyobb:
        print("Van Adidas ,ami nagyobb 42-nél")
    else:
        print("Nincs Adidas ,ami nagyobb 42-nél")


cipok_lista = pld_lista()

lista_kiir(cipok_lista)

osszegzes_tetel(cipok_lista)

maximalis_tetel(cipok_lista)

szamlalas(cipok_lista)

eldontes(cipok_lista)
