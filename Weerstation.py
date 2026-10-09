def Fahrenheit(temp_celsius):
    return 32 + 1.8 * temp_celsius

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel_temp = gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid)

    if gevoel_temp < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel_temp < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif 0 <= gevoel_temp < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel_temp < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel_temp < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"

def weerstation():
    print("Welkom bij het Weerstation!")
    totaal_temperatuur = 0
    aantal_dagen = 0

    for dag in range(1,8):
        temperatuur = input(f"Wat is op dag {dag} de temperatuur[C]: ")
        if temperatuur == "":
            print("doei")
            break

        wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")
        if wind == "":
            print("doei")
            break

        vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
        if vocht == "":
            print("doei")
            break

        temperatuur = float(temperatuur)
        wind = float(wind)
        vocht = int(vocht)

        totaal_temperatuur = totaal_temperatuur + temperatuur
        aantal_dagen = aantal_dagen + 1

        gemiddelde = totaal_temperatuur / aantal_dagen

        print("Het is", temperatuur, "°C (",Fahrenheit(temperatuur), "F) ")
        print(weerrapport(temperatuur, wind, vocht))
        print("Gem. temperatuur tot nu toe is", gemiddelde)
        print("==========================================================")

if __name__ == "__main__":
    weerstation()










