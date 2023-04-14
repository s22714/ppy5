import zad5 as z5

def usun_studenta(users):
    email = input("Podaj email: ")

    for d in users:
        if d["email"] == email:
            users.remove(d)
            print("Usunieto studenta")
            break

    z5.zapisz_w_pliku(users,"stud.txt")

    return users

def dodaj_studenta(users):
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    email = input("Podaj email: ")
    punkty = input("Podaj punkty: ")

    for d in users:
        if d["email"] == email:
            print("Email w użyciu")
            return users

    user = {"email" : email,
             "imie" : imie,
             "nazwisko" : nazwisko,
             "punkty" : punkty,
             "ocena" : 0,
             "status" : ""}
    users.append(user)
    print("Dodano studenta")

    z5.zapisz_w_pliku(users, "stud.txt")

    return users