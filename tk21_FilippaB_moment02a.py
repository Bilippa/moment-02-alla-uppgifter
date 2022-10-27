#Inlämningsuppgift moment 02a. Filippa Börjesson. TK21.

pi = 3.14
radie= float(input('Vad är cirkelns radie i cm? (skriv endast numret, om ditt tal har decimal skriv med en punkt mellan t.ex. "3.14"): '))
area = radie**2 * pi
omkrets= radie * 2 * pi

print("Radien av cirkeln är " + f"{radie:4.2f}" + "cm.")
print("Arean av cirkeln är " + f"{area:4.2f}" + "cm\u00b2.")
print("Omkretsen av cirkeln är " + f"{omkrets:4.2f}" + "cm.")