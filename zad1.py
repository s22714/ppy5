def get_list_of_students(filepath):
    users = []

    with open(filepath) as file_object:
        for line in file_object:
            l = line.rstrip().split(",")
            if len(l) == 0:
                break
            user = {"email": l[0],
                    "imie": l[1],
                    "nazwisko": l[2],
                    "punkty": float(l[3])}
            if len(l) >= 5:
                user["ocena"] = float(l[4])
            else:
                user["ocena"] = 0
            if len(l) == 6:
                user["status"] = l[5]
            else:
                user["status"] = ""
            users.append(user)
    return users
