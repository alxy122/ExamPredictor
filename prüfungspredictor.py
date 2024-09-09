from datetime import datetime, timedelta

weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

print("Alte Prüfungsdaten sind hier zu finden:")
print("https://www.student.uni-stuttgart.de/pruefungsorganisation/termine/\n")

while True:
    inputStr = input("Geben Sie das Datum der Prüfung ein (TT MM JJJJ oder TTMMJJJ) oder 'q' zum Beenden: ")

    if inputStr.lower() == "q":
        print("Programm beendet.")
        break

    try:
        if " " in inputStr:     
            date = datetime.strptime(inputStr, "%d %m %Y")
        else:
            date = datetime.strptime(inputStr, "%d%m%Y")
    except ValueError:
        print("Falsches Datumsformat. Bitte geben Sie das Datum im Format TT MM JJJJ ein.")
        continue

    # Get current date details
    cw = date.isocalendar()[1]
    weekday = date.weekday()

    # Print the old date details
    print(f"\nAltes Prüfungsdatum:")
    print(f"  Kalenderwoche: KW {cw}")
    print(f"  Datum: {date.strftime('%d.%m.%Y')}")
    print(f"  Wochentag: {weekdays[weekday]}")

    # Calculate the new date for the next year
    new_date = datetime(date.year + 1, 1, 1)
    new_date += timedelta(weeks=cw - 1)
    new_date += timedelta(days=weekday - new_date.weekday())
    new_weekday = new_date.weekday()
    new_cw = new_date.isocalendar()[1]

    # Print the new date details
    print(f"\nPrognose für das nächste Jahr:")
    print(f"  Kalenderwoche: KW {new_cw}")
    print(f"  Datum: {new_date.strftime('%d.%m.%Y')}")
    print(f"  Wochentag: {weekdays[new_weekday]}")
    print("\n" + "="*30 + "\n")
