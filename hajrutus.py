class cal():  # Määratleb klassi nimega 'cal'
    def __init__(self, a, b):  # Klassil on konstruktor, mis võtab kaks argumenti: a ja b.
        self.a = a  # Salvestab argument a klassi atribuuti self.a
        self.b = b  # Salvestab argument b klassi atribuuti self.b

    def liitmine(self):  # Meetod liitmise teostamiseks
        return self.a + self.b  # Tagastab self.a ja self.b summa

    def lahutamine(self):  # Meetod lahutamise teostamiseks
        return self.a - self.b  # Tagastab self.a ja self.b vahe

    def korrutamine(self):  # Meetod korrutamise teostamiseks
        return self.a * self.b  # Tagastab self.a ja self.b korrutise

    def jagamine(self):  # Meetod jagamise teostamiseks
        if self.b == 0:  # Kontrollib, kas jagaja (self.b) on null
            return "Jagamine nulliga ei ole lubatud!"  # Tagastab teate, kui jagaja on null
        return self.a / self.b  # Tagastab self.a jagatuna self.b

    def jaak(self):  # Meetod jäägi leidmiseks
        if self.b == 0:  # Kontrollib, kas jagaja (self.b) on null
            return "Jäägi leidmine nulliga ei ole lubatud!"  # Tagastab teate, kui jagaja on null
        return self.a % self.b  # Tagastab self.a ja self.b jäägi

    def ruutjuur(self):  # Meetod ruutjuure leidmiseks
        return self.a ** 0.5  # Tagastab self.a ruutjuure (a tõstetud 0.5-ndasse)


a = int(input("Sisesta esimene number: "))  # Küsib kasutajalt esimest täisarvu ja muundab selle täisarvuks
b = int(input("Sisesta teine number: "))  # Küsib kasutajalt teist täisarvu ja muundab selle täisarvuks

kalk = cal(a, b)  # Loob uue 'cal' objekti, kasutades kasutaja sisestatud arve a ja b

while True:  # Algatab lõpmatu tsükli
    def menu():  # Funktsioon menüü kuvamiseks
        # Menüü valikute tekst
        x = (
            '1. Liitmine \n2. Lahutamine\n3. Korrutamine\n4. Jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n0. Väljumine')
        print(x)  # Printib menüü valikud ekraanile


    menu()  # Kutsutakse välja menüü funktsioon
    valik = int(input('Sisesta üks valikutest: '))  # Küsib kasutajalt valiku numbrit ja muundab selle täisarvuks

    if valik == 1:  # Kui kasutaja valik on 1
        print("Vastus: ", kalk.liitmine())  # Väljastab liitmise vastuse

    elif valik == 2:  # Kui kasutaja valik on 2
        print("Vastus: ", kalk.lahutamine())  # Väljastab lahutamise vastuse

    elif valik == 3:  # Kui kasutaja valik on 3
        print("Vastus: ", kalk.korrutamine())  # Väljastab korrutamise vastuse

    elif valik == 4:  # Kui kasutaja valik on 4
        print("Vastus: ", kalk.jagamine())  # Väljastab jagamise vastuse

    elif valik == 5:  # Kui kasutaja valik on 5
        print("Vastus: ", kalk.jaak())  # Väljastab jäägi vastuse

    elif valik == 6:  # Kui kasutaja valik on 6
        print("Vastus: ", kalk.ruutjuur())  # Väljastab ruutjuure vastuse

    elif valik == 0:  # Kui valik on 0, siis väljub programmist
        print('Programm lõpetatud.')  # Teade programm kaotamisest
        break  # Katkestab tsükli

    else:  # Kui valik ei vasta ühelegi eelnevale valikule
        print("Palun vali kehtiv valik!")  # Teade, et sisestatud valik ei kehti