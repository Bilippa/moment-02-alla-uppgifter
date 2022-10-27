#m02u05

# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.
exchange_rate_dollar_to_sek = 8.82
#Ovanför har jag lagt till ett understreck mellan rate och dollar för att koppla samman orden för att göra en korrekt variabel.
#Värdet ovanför skrevs med , istället för .
print("Detta är ett program där vi kan växla mellan SEK & dollar")
#Ovanför la jag till "" inom () för att tillåta print kommandot att genomföras.
sek1 = float(input("Hur många SEK vill du växla till dollar: "))
#Ovanför skrevs variabeln som 1sek vilket jag ändrat till sek1 eftersom variabler ej får börja på siffror.
#Det saknades även en avslutande "" inom input kommandot vilket jag då lagt till.
#Datatypen beräknades som fel när programmet kördes, därför har jag lagt till float framför input, för att tillåta användaren att mata in
#önskade värden
dollar = sek1 / exchange_rate_dollar_to_sek 
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek1, dollar))
#Ovanför saknades slut ()