from Cipo import Cipo

peldany1 = Cipo("Nike", 42)
peldany2 = Cipo("Adidas", 41)
peldany3 = Cipo("Adidas", 45)
peldany4 = Cipo("Jordan", 48)

cipok = []
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)
cipok.append(peldany4)

for i in range(0, len(cipok), 1):
    nev: str = cipok[i].nev
    meret: int = cipok[i].meret
    print(f"{nev} ({meret})")


def meret_atlag():
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret
#összegzés tétel
    atlag = ossz / len(cipok)
    print(round(atlag, 3))


meret_atlag()
#maximum ki választása


def melyik_legnagyobb_marka():
    print("melyik márka a legnagyobb? ", end="")
    helye: int = 0
    for i in range(1, len(cipok)):
        if cipok[i].meret > cipok[helye].meret:
            helye = i
    print(f"{cipok[helye].nev}")


melyik_legnagyobb_marka()


def hany_db_adidas_van():
    db: int = 0
    for i in range(len(cipok)):
        if cipok[i].nev == "Adidas":
            db += 1
    print(f"Ennyi db Adidas van: {db}")


hany_db_adidas_van()


def nagyobb_42_adidas():
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True
#eldöntés tétel
    if van_nagyobb:
        print("Van Adidas ,ami nagyobb 42-nél")
    else:
        print("Nincs Adidas ,ami nagyobb 42-nél")


nagyobb_42_adidas()
