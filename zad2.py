import zad5 as z5
def auto_grade(users):
    for user in users:
        if "MAILED" != user["status"] != "GRADED":
            if user["punkty"] <= 50:
                user["ocena"] = 2
                user["status"] = "GRADED"
            elif 50 < user["punkty"] <= 60:
                user["ocena"] = 3
                user["status"] = "GRADED"
            elif 60 < user["punkty"] <= 70:
                user["ocena"] = 3.5
                user["status"] = "GRADED"
            elif 70 < user["punkty"] <= 80:
                user["ocena"] = 4
                user["status"] = "GRADED"
            elif 80 < user["punkty"] <= 90:
                user["ocena"] = 4.5
                user["status"] = "GRADED"
            elif user["punkty"] > 90:
                user["ocena"] = 5
                user["status"] = "GRADED"
    z5.zapisz_w_pliku(users, "stud.txt")
    return users