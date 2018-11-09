import pyknow
import easygui



def zwroc_odpowiedz(pytanie,możliwe_odpowiedzi):
    zwrot=easygui.buttonbox(pytanie, title="Baza wiedzy materialow", choices=możliwe_odpowiedzi)
    print(zwrot)
    return zwrot

class Baza_wiedzy_materialow(pyknow.KnowledgeEngine):
    @pyknow.DefFacts()
    def zdefiniuj_fakty(self):
        yield pyknow.Fact(wytrzymalosc=zwroc_odpowiedz("Wymagana wytrzymalosc materialu", ["Podwyzszona", "Normalna"]))
        yield pyknow.Fact(koszt=zwroc_odpowiedz("Koszt materialu", ["Niski", "Nie gra roli"]))
        yield pyknow.Fact(plastycznosc=zwroc_odpowiedz("Wymagana plastycznosc materialu",["Wymagana","Niewymagana"]))
        yield pyknow.Fact(odpornosc_na_korozje=zwroc_odpowiedz("Odpornosc na korozje",["Wymagana","Niewymagana"]))

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_10(self):
        easygui.msgbox('Wybrales miedz', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_9(self):
        easygui.msgbox('Wybrales ceramike', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_8(self):
        easygui.msgbox('Wybrales aluminium', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_7(self):
        easygui.msgbox('Wybrales zeliwo biale', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_6(self):
        easygui.msgbox('Wybrales staliwo', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_5(self):
        easygui.msgbox('Wybrales polimer', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyszona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_4(self):
        easygui.msgbox('Wybrales stal wysokostopowa odporna na korozje', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyzszona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_3(self):
        easygui.msgbox('Wybrales stal niskostopowa odporna na korozje', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyzszona"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_2(self):
        easygui.msgbox('Wybrales zeliwo szare', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyzszona"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_1(self):
        easygui.msgbox('Wybrales stal niestopowa konstrukcyjna', 'Baza wiedzy materialow')

    @pyknow.Rule(pyknow.AND(pyknow.Fact(koszt="Niski"),
                 pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=0)
    def material_0(self):
        easygui.msgbox('Brak wymaganego materialu', 'Baza wiedzy materialow')


engine = Baza_wiedzy_materialow()
engine.reset()
engine.run()
print(engine.facts)
