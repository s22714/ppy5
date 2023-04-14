import zad1 as z1
import zad2 as z2
import zad3 as z3
import zad4 as z4
import zad5 as z5

users = z1.get_list_of_students("stud.txt")
inp = ""

while inp != "exit":
    inp = input("Podaj polecenie: ")

    if inp == "print":
        for l in users:
            print(l)

    if inp == "grade":
        users = z2.auto_grade(users)

    if inp == "add":
        users = z3.dodaj_studenta(users)

    if inp == "erase":
        users = z3.usun_studenta(users)
    if inp == "email":
        users = z4.send_email(users)

