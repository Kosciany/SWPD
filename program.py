import pyknow
import easygui

tytuł_okna = "Baza wiedzy materiałów" #tytuł okna interfejsu graficznego

def zwroc_odpowiedz(pytanie,możliwe_odpowiedzi):
    #funkcja, która otwira okienko z pytaniem podanym w argumencie "pytanie" i przyciskami z odpowiedziami zawartymi
    #w liście możliwe odpowiedzi. Buttonbox zwraca wybraną odpowiedź. Funkcja zwraca wybraną odpowiedź.
    zwrot=easygui.buttonbox(pytanie, title=tytuł_okna, choices=możliwe_odpowiedzi)
    print(zwrot)
    return zwrot
def zakoncz_program(silnik_wiedzy,nazwa_materialu):
    silnik_wiedzy.declare(pyknow.Fact(rezultat = nazwa_materialu))
    if nazwa_materialu is not 'Nie ma materiału spełniającego podane kryteria':
        tekst = "Wybrano " + nazwa_materialu
    else:
        tekst = nazwa_materialu
    easygui.msgbox(tekst, title=tytuł_okna)


class Baza_wiedzy_materialow(pyknow.KnowledgeEngine):
    @pyknow.DefFacts()
    def zdefiniuj_fakty(self):
        #użyto dekorator pyknow.DefFacts, funkcja odpalana po wywołaniu metory .run() obiektu
        yield pyknow.Fact(wytrzymalosc=zwroc_odpowiedz("Wymagana wytrzymałość materiału", ["Podwyższona", "Normalna"])) #generowanie kolejnych faktów)
        yield pyknow.Fact(koszt=zwroc_odpowiedz("Koszt materialu", ["Niski", "Nie gra roli"]))
        yield pyknow.Fact(plastycznosc=zwroc_odpowiedz("Dobra plastyczność materiału",["Wymagana","Niewymagana"]))
        yield pyknow.Fact(odpornosc_na_korozje=zwroc_odpowiedz("Odporność na korozję",["Wymagana","Niewymagana"]))


    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"), #utworzenie reguły i określenie faktów, które warunkują jej wywołanie
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=0) #salience - priorytet zasad, im wyższa liczba tym wyższy priorytet
    def material_10(self): #funkcja która jest wykonywana, kiedy powyższa zasada jest spełniona
        zakoncz_program(self,"miedź")


    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_9(self):
        zakoncz_program(self, "ceramika")


    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=2)
    def material_8(self):
        zakoncz_program(self,"aluminium")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=3)
    def material_7(self):
        zakoncz_program(self,"żeliwo białe")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=4)
    def material_6(self):
        zakoncz_program(self, "staliwo")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=5)
    def material_5(self):
        zakoncz_program(self, "materiał polimerowe")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=6)
    def material_4(self):
        zakoncz_program(self, "stal wysokostopową odporną na korozję")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=7)
    def material_3(self):
        zakoncz_program(self, "stal niskostopową odporną na korozję")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=8)
    def material_2(self):
        zakoncz_program(self, "żeliwo szare")

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=9)
    def material_1(self):
        zakoncz_program(self, "stal niestopową konstrukcyjną")

    @pyknow.Rule(pyknow.OR(
                pyknow.AND(
                    pyknow.Fact(wytrzymalosc="Normalna"),
                    pyknow.Fact(koszt="Niski"),
                    pyknow.Fact(plastycznosc="Wymagana"),
                    pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                pyknow.AND(
                    pyknow.Fact(wytrzymalosc="Podwyższona"),
                    pyknow.Fact(koszt="Niski"),
                    pyknow.Fact(odpornosc_na_korozje="Wymagana"),
                    pyknow.Fact(plastycznosc=pyknow.W())
                    ))
                    , salience=10)
    def material_0(self):
        easygui.msgbox('Nie ma materiału spełniającego podane kryteria', title=tytuł_okna)


engine = Baza_wiedzy_materialow()
engine.reset()
engine.run()
print(engine.facts)

