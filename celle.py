#celle

# i denne klassen lager vi metoder for å sette statusen til cellen til enten død
# eller levende. Vi har erLevende for å kunne si enten True eller False gitt statusen
# til cellen. Vi har en metode, hentStatusTegn, som oppgir enten O eller . hvis cellen
# er levende eller død. Og, for å gjøre om self._status til en streng og ikke en
# adresse har vi def __str__(self)
class Celle():
    def __init__(self):
        self._status = "død"

    def __str__(self):
        return self._status

    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hentStatusTegn(self):
        if self._status == "død":
            return "."
        else:
            return "O"
