def aantal_dagen(inputFile):
    bestand = open(inputFile)
    regels = bestand.readlines()
    bestand.close()

    return len(regels) - 1

def auto_berekenen(inputFile, outputFile):
    bestand = open(inputFile)
    regels = bestand.readlines()
    bestand.close()

    uitvoer = open(outputFile, 'w')

    for regel in regels[1:]:
        gegevens = regel.strip().split()

        datum = gegevens[0]
        aantal_personen = int(gegevens[1])
        setpoint = float(gegevens[2])
        buitentemperatuur = float(gegevens[3])
        neerslag = float(gegevens[4])

        verschil = setpoint - buitentemperatuur

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = aantal_personen + 1

        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(
            datum + ";" +
            str(cv) + ";" +
            str(ventilatie) + ";" +
            str(bewatering) + "\n"
        )

    uitvoer.close()

def overwrite_settings(outputFile):
    datum = input("Geef een datum aan: ")
    systeem = int(input("Kies een systeem: 1: CV, 2: Ventilatie,  3: Bewatering:  "))
    waarde = input("Kies een nieuwe waarde: ")

    bestand = open(outputFile)
    regels = bestand.readlines()
    bestand.close()

    for i in range (len(regels)):
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum:

            if systeem == 1:
                if int(waarde) < 0 or int(waarde) > 100:
                    return -3
                gegevens[1] = waarde

            elif systeem == 2:
                if int(waarde) < 0 or int(waarde) > 4:
                    return -3
                gegevens[2] = waarde

            elif systeem == 3:
                if waarde == "0":
                    gegevens[3] = "False"
                elif waarde == "1":
                    gegevens[3] = "True"
                else:
                    return -3
            else:
                return -3
            regels[i] = ";".join(gegevens) + "\n"

            bestand = open(outputFile, "w")
            bestand.writelines(regels)
            bestand.close()

            return 0

    return -1

def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    keuze = 0

    while keuze != 4:
        print("\n===== SMART APP CONTROLLER =====")
        print("1. Aantal dagen weergeven")
        print("2. Autoberekenen actuoren")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = int(input("Maak een keuze: "))
        if keuze == 1:
            dagen = aantal_dagen(inputFile)
            print("Aantal dagen:", dagen)

        elif keuze == 2:
            auto_berekenen(inputFile, outputFile)
            print("Actuatoren berekend en opgeslagen")

        elif keuze == 3:
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print("Waarde is goed aangepast")
            elif resultaat == -1:
                print("Datum is niet gevonden helaas")
            elif resultaat == -3:
                print("Er is geen geldige invoer")

        elif keuze == 4:
            print("Programma is afgesloten")
        else:
            print("Er is geen geldige keuze")


if __name__ == "__main__":
    smart_app_controller()
