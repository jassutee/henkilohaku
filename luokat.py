class Henkilö:
    def __init__(self, lista):
        self.__nimi = lista[1]
        self.__huone = lista[0]
        self.__puhnro = lista[2]

    def tulosta(self):
        print(self.__huone, self.__nimi, self.__puhnro, sep=",")

    def kuka(self, kuka):
        pieninimi = self.__nimi.lower()
        kuka = kuka.lower()
        if kuka == pieninimi:
            self.tulosta()
            return True

    def etsihuone(self, huonenro):
        if huonenro == self.__huone:
            self.tulosta()
            return True

def ajo(henkilöt):
    while True:
        rivi = input("komento> ")

        if rivi == "":
            break

        osat = rivi.split()
        käsky = osat[0]
        loput = " ".join(osat[1:])

        if käsky == "nimi" and len(osat) >= 2:
            for henkilö in henkilöt:
                henkilö = henkilö.kuka(loput)
                if henkilö:
                    break
            if not henkilö:
                print("Virhe: organisaatiossa ei ole henkilöä nimeltä", loput)


        elif käsky == "huone" and len(osat) == 2:
            löytö = False
            for rivi in henkilöt:
                huone = rivi.etsihuone(loput)
                if huone:
                    löytö = True
            if not löytö:
                print("Virhe: organisaatiossa ei ole työhuonetta", loput)

        elif käsky == "tulosta" and len(osat) == 1:
            for henkilö in henkilöt:
                henkilö.tulosta()

        else:
            print("Virhe: väärä syöte, yritä uudelleen")


def main():
    tiedostonnimi = input("Syötä organisaatiotiedoston nimi: ")
    try:
        tiedosto = open(tiedostonnimi, "r")
        henkilöt = []
        for rivi in tiedosto:
            lista = rivi.rstrip().split(";")
            lista[1] = Henkilö(lista)
            henkilöt.append(lista[1])
        tiedosto.close()

        ajo(henkilöt)
    except IOError:
        print("Virhe: tiedostoa ei saa luettua")

main()