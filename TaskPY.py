
#Construiește trei clase: o clasă “Mașină”, o clasă “Șofer” și o clasă “Motor”. Avem nevoie ca o Mașină să aibe un Șofer și un Motor.
#Un Șofer are: nume, data_nașterii;
#Un Motor are: cai_putere;
#O Mașină are: marcă, model, an_fabricație;
#Construiește o metodă (funcție) în clasa Mașină în care să afișezi detaliile despre mașină și șoferul care o conduce dacă motorul ei are peste 105 cai putere.

from os import linesep as endl
        
class Motor():
    def __init__(self, cai_putere):
        self.cai_putere = cai_putere
        
class Șofer():
    def __init__(self, nume, data_nașterii):
        self.nume = nume
        self.data_nașterii = data_nașterii
    
class Mașină(Șofer, Motor):
    def __init__(self, marcă, model, an_fabricație, nume, data_nașterii, cai_putere):
        Șofer.__init__(self, nume, data_nașterii)
        Motor.__init__(self, cai_putere)
        self.marcă = marcă
        self.model = model
        self.an_fabricație = an_fabricație
      
                
    def afisare_detalii(self):
        if self.cai_putere > 105:
            print("Mașină:", endl, "Marcă:", self.marcă, endl, "Model:", self.model, endl, "An fabricație:", self.an_fabricație, endl, endl, "Șofer:", endl, "Nume:", self.nume, endl, "Data nașterii:", self.data_nașterii, endl, endl, endl, endl)
   
   
        
masini=[]
    
masini.append( Mașină('BMW', 'E46', 2000, "Mihai Eminescu", "15 ianuarie 1850", 118))
masini.append( Mașină('Volskwagen', 'Polo', 2010, "Ion Creanga", "1 martie 1837", 89))
masini.append( Mașină('Tesla', 'S', 2014, "Ion Luca Caragiale", "13 februarie 1852", 1100))
masini.append( Mașină('Dacia', 'Logan', 2015, "Mihail Sadoveanu", "5 mai 2000", 75))
masini.append( Mașină('Ford', 'Puma', 2020, "Popescu Ion", "24 septembrie 1950", 197))


for obj in masini:
    Mașină.afisare_detalii(obj)