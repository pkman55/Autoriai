class Autorius:
    def __init__(self, vardas, pavarde, pavadinimas, metai, reitingas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pavadinimas = pavadinimas
        self.metai = metai
        self.reitingas = reitingas

    def isvesti(self):
        print(self.vardas, self.pavarde, self.pavadinimas, self.metai, self.reitingas)

a1 = Autorius("Alberas", "Kamiu", "Svetimas", 1942, 9.5)
a2 = Autorius("Alberas", "Kamiu", "Maras", 1947, 8.7)
a3 = Autorius("Francas", "Kafka", "Metamorfoze", 1915, 9.1)
a4 = Autorius("Francas", "Kafka", "Procesas", 1925, 8.2)


a = [a1, a2, a3, a4]

for item in a:
    item.isvesti()
