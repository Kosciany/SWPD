import pyknow

class First_value(pyknow.Fact):
    pass
class Second_value(pyknow.Fact):
    pass

class AND_Gate(pyknow.KnowledgeEngine):
    @pyknow.DefFacts()
    def needed_data(self):
        yield pyknow.Fact(First_value = input("Podaj pierwszą wartość"))
        yield pyknow.Fact(Second_value = input("Podaj drugą wartość"))
    @pyknow.Rule(pyknow.AND(First_value("True"), Second_value("True")))
    def gate_open(self):
        print("GATE OPEN")
    @pyknow.Rule(pyknow.OR(First_value("False"), Second_value("False")))
    def gate_closed(self):
        print("GATE CLOSED")

engine = AND_Gate()
engine.reset()
engine.run()
