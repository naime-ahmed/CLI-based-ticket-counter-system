""" project name: CLI based simple ticket counter system
    Author: Naime molla
    purpose: Course assignment
    Date: oct 30 2022
"""


class Star_cinema:
    hall_list = []

    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)


def convert_seat_to_tuple(string):
    if len(string) > 2:
        return f"Invalid seat no - {string}"
    first = ord(string[0]) - 65 + 1
    second = ord(string[1]) - 48 + 1
    return tuple((first - 1, second - 1))


def convert_tuple_to_seat(t):
    string = chr(t[0] + 65)
    return string


class Hall(Star_cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[id] = [[True for j in range(self.cols)] for i in range(self.rows)]

    def book_seats(self, customer_name, phone, id, seat_list):
        isValidId = 0
        movie_name = ""
        time = ""
        for t in self.show_list:
            if t[0] == id:
                isValidId = 1
                movie_name = t[1]
                time = t[2]

        if isValidId:
            successfully_booked = []
            for t in seat_list:
                if len(t) > 2:
                    print()
                    print("-" * 45)
                    print(f"{t}. Try again")
                    print("-" * 45)
                    print()
                    continue
                if (t[0] >= self.rows) or (t[1] >= self.cols):
                    print()
                    print("-" * 30)
                    print(f"{convert_tuple_to_seat(t)}{t[1]} out of seat range!")
                    print("-" * 30)
                    print()
                    continue
                if t[0] < 0 or t[1] < 0:
                    print()
                    print("-" * 30)
                    print(f"{convert_tuple_to_seat(t)}{t[1]} Negative value error")
                    print("-" * 30)
                    print()
                    continue
                if self.seats[id][t[0]][t[1]] == True:
                    self.seats[id][t[0]][t[1]] = False
                    successfully_booked.append(f"{convert_tuple_to_seat(t)}{t[1]}")
                else:
                    print()
                    print("-" * 30)
                    print(f"{convert_tuple_to_seat(t)}{t[1]} seat unavailable")
                    print("-" * 30)
                    print()
            if len(successfully_booked) == 0:
                return
            print()
            print("##### TICKED BOOKED SUCCESSFULLY!! #####\n")
            print("-" * 70)
            print()
            print(f"NAME: {customer_name}")
            print(f"PHONE NUMBER: {phone}")
            print()
            print(f"MOVIE NAME: {movie_name} \t MOVIE TIME: {time}")
            print("TICKET:", end=" ")
            [print(x, end=" ") for x in successfully_booked]
            print()
            print("HALL:", self.hall_no)
            print()
            print("-" * 70)
            print("\n")
        else:
            print()
            print("-" * 40)
            print(f"There is no show with this id: {id}")
            print("-" * 40)
            print()

    def view_show_list(self):
        print("\n")
        print("-" * 75)
        print("\n")
        for show in self.show_list:
            print(f"MOVIE NAME: {show[1]}\t SHOW ID: {show[0]} \t TIME: {show[2]}")
        print("\n")
        print("-" * 75)
        print("\n")

    def view_available_seats(self, show_id):
        isValidID = False

        for show in self.show_list:
            if show[0] == show_id:
                print("\n\n")
                print(f"MOVIE NAME: {show[1]}\t TIME: {show[2]}")
                isValidID = True

        if isValidID == False:
            print()
            print("-" * 30)
            print("There is no show with this Id")
            print("-" * 30)
            print()
            return
        print("X for already booked seats\n")

        print("-" * 50)
        for i, r in enumerate(self.seats[show_id]):
            for j, seat in enumerate(r):
                if seat:
                    print(f"{chr(i+65)}{j}", end="\t")
                else:
                    print("X", end="\t")
            print()
        print("-" * 50)
        print("\n")


sony_hall = Hall(5, 7, 1)
sony_hall.entry_show("bat01", "Bat man", "Nov 05 2022 5:30PM")
sony_hall.entry_show("super01", "super man", "Nov 06 2022 10:30PM")


while True:
    print(f"1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT")
    user_input = int(input("Enter OPTION: "))
    if user_input == 4:
        break
    elif user_input == 1:
        sony_hall.view_show_list()
    elif user_input == 2:
        show_id = input("Enter show id: ")
        sony_hall.view_available_seats(show_id)
    elif user_input == 3:
        name = input("Enter customer name: ")
        number = input("Enter customer phone number: ")
        show_id = input("Enter show ID: ")
        ticket_num = int(input("Enter number of ticket: "))
        seat_l = []
        while ticket_num:
            id = input("Enter seat No: ")
            seat_l.append(convert_seat_to_tuple(id))
            ticket_num -= 1
        sony_hall.book_seats(name, number, show_id, seat_l)
    else:
        print("Invalid input!")
