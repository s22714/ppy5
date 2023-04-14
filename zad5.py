def zapisz_w_pliku(users, filepath):
    with open(filepath, 'w') as file_object:
        for d in users:
            l = list(d.values())
            email = d["email"]
            imie = d["imie"]
            nazwisko = d["nazwisko"]
            punkty = d["punkty"]
            if len(d) == 5:
                ocena = d["ocena"]
                line = f"{email},{imie},{nazwisko},{punkty},{ocena}\n"
            elif len(d) == 6:
                ocena = d["ocena"]
                status = d["status"]
                line = f"{email},{imie},{nazwisko},{punkty},{ocena},{status}\n"
            else:
                line = f"{email},{imie},{nazwisko},{punkty}\n"
            file_object.truncate()
            file_object.write(line)