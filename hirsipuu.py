import random as r
from sanat import sanat

aakkoset = ["a","b","c","d","e","f","g","h","i",
            "j","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z","å","ä","ö"]

def hirsipuu():
    sana = r.choice(sanat)
    sanan_kirjaimet = set(sana)
    #kirjaimet, jotka pelaaja on jo arvannut
    veikatut_kirjaimet = set()
    kirjaimet = set(aakkoset)
    elamat = 6

    #jatkaa looppia niin kauan kunnes sana on oikein tai elamat loppuu
    while len(sanan_kirjaimet) > 0 and elamat > 0:
        print("Elämät:",elamat,", käytetyt kirjaimet: ", ",".join(veikatut_kirjaimet))
        #lista jossa oikein arvatut kirjaimet oikeilla paikoilla ja muut -
        lista = [kirjain if kirjain in veikatut_kirjaimet else "-" for kirjain in sana]
        print("Sana: ", " ".join(lista))
        veikkaus = input("Arvaa kirjain: ").lower()
        #jos veikattu kirjain on kirjain, jota ei ole arvattu
        if veikkaus in kirjaimet - veikatut_kirjaimet:
            veikatut_kirjaimet.add(veikkaus)
            if veikkaus in sanan_kirjaimet:
                sanan_kirjaimet.remove(veikkaus)
            #jos kirjain väärin, yksi elämä vähemmän
            else:
                elamat -= 1
                print("Sanassa ei ole kirjainta {} :(".format(veikkaus))
        elif veikkaus in veikatut_kirjaimet:
            print("Olet jo yrittänyt tätä kirjainta.")
        else:
            print("Tuo ei ole kirjain hupsu!")

    #jos elamat loppuu, häviö
    if elamat == 0:
        print("Hävisit pelin :( Sana oli {}".format(sana))
        valikko()
    else:
        print("Onneksi olkoon!! Arvasit sanan {} oikein!!".format(sana))
        valikko()

def valikko():
    while True:
        valinta = input("Pelaa uudestaan valitsemalla U tai poistu valitsemalla E: ").lower()
        if valinta == "u":
            hirsipuu()
        elif valinta == "e":
            print("Heippa!")
            break
        else:
            print("Valitse U tai E kiitos")

if __name__ == "__main__":
    print("Tervetuloa pelaamaan hirsipuuta!!")
    hirsipuu()