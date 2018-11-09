import pyknow
import easygui
import sys

class Fakt(pyknow.Fact):
    pass

def zwróć_odpowiedź(pytanie,możliwe_odpowiedzi):
    tytuł = "Baza wiedzy materiałów"
    return easygui.buttonbox(pytanie, title = tytuł, choices = możliwe_odpowiedzi)

class Baza_wiedzy_materiałów(pyknow.KnowledgeEngine):
    @pyknow.DefFacts()
    def zdefiniuj_fakty(self):
        easygui.msgbox("Witaj! Pomogę Ci wybrać odpowiedni materiał i dodatki stopowe.")
        yield Fakt(ciężar_względny = zwróć_odpowiedź("Czy zależy Ci na jak najmniejszym ciężarze konstrukcji?", ["tak","nie"]))
        yield Fakt(odporność_na_korozję = zwróć_odpowiedź("Czy materiał będzie narażony na środowisko korozyjne?",["tak","nie"]))
        yield Fakt(odpowiedzialnosć_konstrukcji = zwróć_odpowiedź("Czy materiał powinien się cechować się wysoką wytrzymałością?",["tak","nie"]))
        yield Fakt(przewodność_cieplna = zwróć_odpowiedź("Czy materiał powinien dobrze przewodzić ciepło?",["tak","nie"]))
        yield Fakt(spawalność = zwróć_odpowiedź("Czy elementy konstrukcji będą spawane?",["tak","nie"]))
        yield Fakt(żaroodporność = zwróć_odpowiedź("Czy konstrukcja będzie pracować w temperaturach powżej 400 stopni?",["tak","nie"]))
        yield Fakt(koszt = zwróć_odpowiedź("Czy cena materiału jest istotnym czynnikiem?",["tak","nie"]))
    @pyknow.Rule(Fakt(ciężar_względny = "tak"))
    def ciężar(self):
        print("Zależy na ciężarze")


engine = Baza_wiedzy_materiałów()
engine.reset()
engine.run()
