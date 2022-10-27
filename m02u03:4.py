#I en affär så köper du 3st pennor som kostar 4kr/st och ett äpple som väger 200g. Äpplen kostar 19kr/kg.
# Jag handlade 3 pennor för 12kr och 1 äpple för 3.80kr vilket totalt blev 15.80kr.
# Antalet varor och priser skall vara variabler. Summor, och delsummor, skall vara uträknade på lämpligt sätt.

pennor = 3 #st
prispenna = 4*pennor #kr/st
vikt= 0.2 #kg
prisäpple = 19*vikt #kr/kg
äpple = 1 #st, 0.2kg

#Jag fastnar redan i början av denna uppgift p.g.a. variabel skapandet. Hur bör jag inkludera äpplets vikt? Vad är passande namn för variablerna???

#Kommatecken:
print("Jag handlade", pennor, "pennor för", prispenna, "kr och", äpple, "äpple för",f"{prisäpple:4.2f}", "kr vilket totalt blev", f"{prispenna+prisäpple:4.2f}", "kr." )

#Plustecken:
print("Jag handlade " + str(pennor) + " pennor för " + str(prispenna) + " kr och " + str(äpple) + " äpple för " + str(f"{prisäpple:4.2f}") + " kr vilket totalt blev " + str(f"{prispenna+prisäpple:4.2f}") + " kr." )

#Uppbyggd sträng innan utskrift:
s = "Jag handlade " + str(pennor)
s += " pennor för " + str(prispenna)
s += " kr och " + str(äpple)
s += " äpple för " + str(f"{prisäpple:4.2f}")
s += " kr vilket totalt blev " + str(f"{prisäpple + prispenna:4.2f}")
s += " kr."

print(s)

#Öppen print() utan radbrytning:

print("Jag handlade " + str(pennor) + " pennor för ", end="")
print(str(prispenna) + " kr och ", end="")
print(str(äpple) + " äpple för ", end="")
print(str(f"{prisäpple:4.2f}") + " kr vilket totalt blev " + str(f"{prisäpple + prispenna:4.2f}"), end="")
print(" kr. ")

#Formatmetoden:

print( "Jag handlade {0} pennor för {1} kr och {2} äpple för {3} kr vilket totalt blev {4} kr.".format(pennor, prispenna, äpple, str(f"{prisäpple:4.2f}"), str(f"{prisäpple + prispenna:4.2f}")))

#F-stringmetoden:

print(f"Jag handlade {pennor} pennor för {prispenna} kr och {äpple} äpple för {prisäpple:4.2f} kr vilket totalt blev {prisäpple + prispenna:4.2f} kr.")