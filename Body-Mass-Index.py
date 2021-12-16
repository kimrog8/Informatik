# Der Benutzer gibt Gewicht in Kilogramm ein.
# Das eingegebene Gewicht wir in einen Float umgewandelt.

Gewicht=input("Gib dein Gewicht in kg ein: ")
Gewicht=float(Gewicht)

# Der Benutzer gibt seine Grösse in Meter ein.
# Die eingegebene Grösse wird in einen Float umgewandelt.
Grösse=input("Gib deine Grösse in m ein: ")
Grösse=float(Grösse)

# Die Grösse wird mal die Grösse gerechnet. Das ergibt Grösse1.
Grösse1=float(Grösse*Grösse)

# Das Gewicht wird geteilt durch die Grösse1 gerechnet. 
BMI=Gewicht/Grösse1

# Das ergibt den BMI. Dieser wird ausgegeben.
BMI=str(BMI)
print("Dein BMI beträgt:" +BMI)
