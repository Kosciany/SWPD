import pyknow
import easygui

tytuł_okna = "Baza wiedzy materiałów"

def zwroc_odpowiedz(pytanie,możliwe_odpowiedzi):
    zwrot=easygui.buttonbox(pytanie, title=tytuł_okna, choices=możliwe_odpowiedzi)
    print(zwrot)
    return zwrot

class Baza_wiedzy_materialow(pyknow.KnowledgeEngine):
    @pyknow.DefFacts()
    def zdefiniuj_fakty(self):
        yield pyknow.Fact(wytrzymalosc=zwroc_odpowiedz("Wymagana wytrzymałość materiału", ["Podwyższona", "Normalna"]))
        yield pyknow.Fact(koszt=zwroc_odpowiedz("Koszt materialu", ["Niski", "Nie gra roli"]))
        yield pyknow.Fact(plastycznosc=zwroc_odpowiedz("Dobra plastyczność materiału",["Wymagana","Niewymagana"]))
        yield pyknow.Fact(odpornosc_na_korozje=zwroc_odpowiedz("Odporność na korozję",["Wymagana","Niewymagana"]))

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_10(self):
        easygui.msgbox('Wybrano miedź', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_9(self):
        easygui.msgbox('Wybrano ceramikę', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_8(self):
        easygui.msgbox('Wybrano aluminium', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_7(self):
        easygui.msgbox('Wybrano żeliwo białe', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_6(self):
        easygui.msgbox('Wybrano staliwo', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Normalna"),
                            pyknow.Fact(koszt="Niski"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_5(self):
        easygui.msgbox('Wybrano materiały polimerowe', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_4(self):
        easygui.msgbox('Wybrano stal wysokostopową odporną na korozję', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(koszt="Nie gra roli"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Wymagana")),
                 salience=1)
    def material_3(self):
        easygui.msgbox('Wybrano stal niskostopową odporną na korozję', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(plastycznosc="Niewymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_2(self):
        easygui.msgbox('Wybrano żeliwo szare', title=tytuł_okna)

    @pyknow.Rule(pyknow.AND(pyknow.Fact(wytrzymalosc="Podwyższona"),
                            pyknow.Fact(plastycznosc="Wymagana"),
                            pyknow.Fact(odpornosc_na_korozje="Niewymagana")),
                 salience=1)
    def material_1(self):
        easygui.msgbox('Wybrano stal niestopową konstrukcyjną', 'Baza wiedzy materialow')

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
                    , salience=0)
    def material_0(self):
        easygui.msgbox('Nie ma materiału spełniającego podane kryteria', title=tytuł_okna)


engine = Baza_wiedzy_materialow()
engine.reset()
engine.run()
print(engine.facts)

