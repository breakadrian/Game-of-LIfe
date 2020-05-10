#Først importerer jeg klassen Celle og randint som brukes i metoden _generer
from celle import Celle
from random import randint

# i konstruktøren lager jeg tre instansvariabler, og ved hjelp av en nøstet for-løkke
# fyller jeg den ene instansvariablen som er en liste med flere lister likt antallet
# rader. Disse fyller jeg igjen med Celler, altså med klassen Celle, likt antallet
# kolonner. Jeg kaller så på metodene _generer og tegnBrett for å gi status til
# cellene og for å skrive ut rutenettet mitt.
class Spillbrett():
    def __init__(self, rad, kol):
        self._rader = rad
        self._kolonner = kol
        self._rutenett = []
        for j in range(rad):
            self._rutenett.append([])
            for i in range(kol):
                self._rutenett[j].append(Celle())
        self._generer()
        self.tegnBrett()

# i denne metoden ber lager jeg en nøstet for-løkke som leser kjører et antall ganger
# likt antallet rader og kolonner. Jeg tar så å definererer variabelen tall som et
# tilfeldig tall mellom 0 og 2, for så å si at hvis variabelen ble lik 2 skal den
# nåværende cellen i rutenettet bli gjort levende ved hjelp av metoden fra Celle().
# Ettersom cellene er i utgangspunktet døde, som definert i Celle(), blir 1/3 gjort
# levende. Til slutt returnerer jeg rutenettet.
    def _generer(self):
        for j in range(len(self._rutenett)):
            for i in range(len(self._rutenett[j])):
                tall = randint(0,2)
                if tall == 2:
                    self._rutenett[j][i].settLevende()
        return self._rutenett

# i denne metoden ber jeg igjen om at vi looper likt antallet rader. Jeg definerer
# så en variabel som en tom streng. i neste løkke looper jeg likt antallet kolonner,
# og legger til hver enkelt celle, gjort om til et tegn, til i variabelen min.
# Til slutt skriver jeg ut variablen. Jeg lager denne variabelen så jeg får skrevet ut
# hver rad med tegn på sin egen rad.
    def tegnBrett(self):
        for j in range(len(self._rutenett)):
            skriv_ut = ""
            for i in range(len(self._rutenett[j])):
                skriv_ut += self._rutenett[j][i].hentStatusTegn()
            print(skriv_ut)

# i denne metoden lager jeg en liste, og ved hjelp av en nøstet for-løkke definerer
# jeg j og i som -1, 0 og 1. Ved å gjøre dette, samt å kalle på raden og kolonnen
# får jeg muligheten til å lage to variabler som defineres som alle cellene rundt
# den vi befinner oss på. Jeg definerer deretter gyldig som True, og sier med flere
# if kommandoer, at hvis vi befinner oss på den cellen vi står på gjelder det ikke.
# Vi sier også at det er ugyldig hvis naborad er større eller lik instansvariabelen
# for rader, eller hvis naborad er mindre enn 0. Vi spør om det samme for kolonnene.
# Dette gjør vi for å sjekke at vi ikke er utenfor rutenettet. Hvis gyldig er tilfelle,
# altså at den er True, legger vi til cellen i nabolisten vår, for så å returnere listen.
    def finnNaboer(self, rad, kolonne):
        naboListe = []
        for x in range(-1 , 2):
            for y in range(-1, 2):
                naboRad = rad + x
                naboKol = kolonne + y
                gyldig = True
                if naboRad == rad and naboKol == kolonne:
                    gyldig = False
                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False
                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False
                if gyldig:
                    naboListe.append(self._rutenett[naboRad][naboKol])
        return naboListe

# i denne metoden lager vi først to tomme lister. Deretter, ved hjelp av en for-løkke,
# sier vi at hvis cellen vi befinner oss på er levende, og hvis de andre cellene rundt
# er enten større enn 3 eller mindre enn 2, så legger vi cellen til i listen som skal dø
# Vi spør deretter om cellen er død, og hvis dette er tilfelle legges den i listen
# over dem som skal bli gjenopplivet. Etter dette dreper vi og gjenoppliver cellene i
# de respektive listene.
    def oppdatering(self):
        doedTilLevende = []
        LevendeTilDoed = []
        for j in range(len(self._rutenett)):
            for i in range(len(self._rutenett[j])):
                teller_1 = 0
                teller_2 = 0
                if self._rutenett[j][i].erLevende():
                    for a in self.finnNaboer(j,i):
                        if a.erLevende():
                            teller_1 += 1
                    if teller_1 > 3 or teller_1 < 2:
                        LevendeTilDoed.append(self._rutenett[j][i])
                elif self._rutenett[j][i].erLevende() == False:
                    for b in self.finnNaboer(j,i):
                        if b.erLevende():
                            teller_2 += 1
                    if teller_2 == 3:
                        doedTilLevende.append(self._rutenett[j][i])
        for i in doedTilLevende:
            i.settLevende()
        for element in LevendeTilDoed:
            element.settDoed()

# I denne metoden leter vi igjennom rutenettet ved hjelp av en nøstet for-løkke
# og øker telleren vår, antall, med 1 hvis vi finner levende celler.
    def finnAntallLevende(self):
        antall = 0
        for j in range(len(self._rutenett)):
            for i in range(len(self._rutenett)):
                if self._rutenett[j][i].erLevende():
                    antall += 1
        return antall
