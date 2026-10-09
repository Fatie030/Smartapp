import requests
import Smartappcontroller
import Weerstation

def huidige_temperatuur():
    api_key = "c533b2a535c379f093ffc3a2d950d94d"
    Stad = "Utrecht"

    weer_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={Stad}&appid={api_key}&units=metric")
    gegevens = weer_data.json()

    if str(gegevens['cod']) == '404':
        print("Geen gegevens gevonden")

    else:
        weer = weer_data.json()['weather'][0]['main']
        temp = round(weer_data.json()['main']['temp'])

        print(f"Het weertype in {Stad} is: {weer}")
        print(f"De temperatuur in {Stad} is: {temp} °C")

def main():
    keuze = 0

    try:
        print("===== WEERWIJZER MENU =====")
        print("1. Weerstation")
        print("2. Smartappcontroller")
        print("3. Huidige weer Utrecht")
        print("4. Stoppen")

        keuze = int(input("Maak een keuze: "))

        if keuze == 1:
            Weerstation.weerstation()

        elif keuze == 2:
            Smartappcontroller.smart_app_controller()

        elif keuze == 3:
            huidige_temperatuur()

        elif keuze == 4:
            print("Programma is afgesloten")

        else:
            print("Geen invoer")

    except ValueError:
        print("Geen invoer")

if __name__ == "__main__":
    main()


