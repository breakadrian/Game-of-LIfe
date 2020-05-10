#main.py

# Her importerer jeg spillbret-klassen, men ikke celle, for den har jeg allerede
# importert i spillbrett-klassen
from spillbrett import Spillbrett

# i prosedyren under ber jeg om input fra brukeren til både antall rader og kolonner
def main():
    rad = int(input(
    "Hei og velkommen til Game of Life! Oppgi hvor mange rader du ønsker å spille med:\n> "))
    kolonne = int(input("Og hvor mange kolonner ønsker du? \n> "))

# deretter oppretter jeg spill_1 som et spillbrettobjekt, en generasjons-teller, og en
# variabel, avslutt, som jeg bruker til å avslutte/fortsette while-løkken. I denne
# løkken øker jeg generasjon med 1 for hver gjennomgang, kaller på metoden finnAntallLevende
# fra spillbrett(), og spør om spillet skal fortsette. Gjør det det kaller jeg på oppdatering
# metoden, masse linjeskift og så tegner jeg rutenettet ut på nytt.
    spill_1 = Spillbrett(rad, kolonne)
    generasjon = 0
    avslutt = ""
    while avslutt != "q":
        generasjon += 1
        print("Generasjon: " , generasjon , "- Antall levende celler:", spill_1.finnAntallLevende() )
        avslutt = input(
        "Ønsker du å fortsette trykk ENTER. Ønsker du å avslutte tast q og så ENTER:\n")
        if avslutt == "q":
            exit()
        else:
            spill_1.oppdatering()
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            spill_1.tegnBrett()

main()
