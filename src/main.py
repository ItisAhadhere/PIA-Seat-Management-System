from tkinter import *
from tkinter import ttk
import pickle
import os

inputs_validated = False
values = []
def reserve_window():
    reservation_window = Tk()
    reservation_window.title("Reserve a Seat")
    reservation_window.geometry("400x200")

    name_input = StringVar()
    id_input = StringVar()
    seat_input = StringVar()
    seat_inputnum = StringVar()
    input_luggweight = StringVar()
    def validate_input():
        valid_id = False
        valid_name = False
        valid_seatnum = False
        valid_luggage = False
        try:
            int(id_entry.get())
            if len(id_entry.get()) == 7:
                id_entry.configure(background="white", foreground="black")
                valid_id = True
            else:
                id_entry.configure(background="red3", foreground="white")
        except:
            id_entry.configure(background="red3", foreground="white")
            valid_id = False

        if  len(name_entry.get()) > 15 or len(name_entry.get()) == 0:
            name_entry.configure(background="red3", foreground="white")
        else:
            valid_name = True
            name_entry.configure(background="white", foreground="black")

        try:
            int(seat_num_entry.get())
            seat_num_entry.configure(background="white", foreground="black")
            valid_seatnum = True
        except:
            seat_num_entry.configure(background="red3", foreground="white")
            valid_seatnum = False
        try:
            if float(lug_weight_entry.get()) <= 100:
                lug_weight_entry.configure(background="white", foreground="black")
                valid_luggage = True
            else:
                lug_weight_entry.configure(background="red3", foreground="white")
        except:
                lug_weight_entry.configure(background="red3", foreground="white")

        if valid_name and valid_id and valid_seatnum and valid_luggage:
            values.append(name_entry.get())
            values.append(id_entry.get())
            values.append(seat_menu.get())
            values.append(seat_num_entry.get())
            values.append(lug_weight_entry.get())
            reservation_window.destroy()



    name_label = Label(reservation_window, text="Name:", font=("calibre", 8, "bold"), padx=10)
    name_entry = Entry(reservation_window, textvariable=name_input, width=30)
    id_label = Label(reservation_window, text="ID", font=("calibre", 8, "bold"), padx=10)
    id_entry = Entry(reservation_window, textvariable=id_input, width=30)
    seatnumber_label = Label(reservation_window, text="Seat Number", font=("calibre", 8, "bold"), padx=10)
    seat_num_entry = Entry(reservation_window, textvariable=seat_inputnum, width=30)
    seat_label = Label(reservation_window, text="Seat Class: ", font=("calibre", 8, "bold"), padx=10)
    seat_menu = ttk.Combobox(reservation_window, width=30, textvariable=seat_input)
    seat_menu["values"] = ["Economy", "Business", "Student"]
    seat_menu.current(0)

    lg_weight_label = Label(reservation_window, text="Luggage Wgt. (kg)", font=("calibre", 8, "bold"), padx=10)
    lug_weight_entry = Entry(reservation_window, textvariable=input_luggweight, width=30)


    reserve_btn = Button(reservation_window,command=validate_input,text="Reserve",activebackground="green",activeforeground="white",bd=1,font=("Arial", 12, "bold"),)

    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    id_label.grid(row=1, column=0)
    id_entry.grid(row=1, column=1)
    seat_label.grid(row=2, column=0)
    seat_menu.grid(row=2, column=1)
    seatnumber_label.grid(row=3, column=0)
    seat_num_entry.grid(row=3, column=1)
    lg_weight_label.grid(row=4,column=0)
    lug_weight_entry.grid(row=4, column=1)
    reserve_btn.grid(row=5, column=0, pady=30)
    reservation_window.bind("<Destroy>", lambda e: reservation_window.quit())
    if inputs_validated:
        return values
    reservation_window.mainloop()

def cancel_window():
    cancellation_window = Tk()
    cancellation_window.title("Cancel Reservation")
    cancellation_window.geometry("400x200")

    def validate_input():
        valid_seatnum = False
        try:
            int(seat_num_entry.get())
            seat_num_entry.configure(background="white", foreground="black")
            valid_seatnum = True
        except:
            seat_num_entry.configure(background="red3", foreground="white")
            valid_seatnum = False
        if valid_seatnum:
            values.append(seat_menu.get())
            values.append(seat_num_entry.get())
            cancellation_window.destroy()
            cancellation_window.quit()

    seat_input_type = StringVar()
    seat_inputnum = StringVar()
    seat_label = Label(cancellation_window, text="Seat Class: ", font=("calibre", 8, "bold"), padx=10)
    seat_menu = ttk.Combobox(cancellation_window, width=30, textvariable=seat_input_type)
    seat_menu["values"] = ["Economy", "Business", "Student"]

    seatnumber_label = Label(cancellation_window, text="Seat Number", font=("calibre", 8, "bold"), padx=10)
    seat_num_entry = Entry(cancellation_window, textvariable=seat_inputnum, width=30)

    cancel_button = Button(cancellation_window, text="Cancel Reservation", command=validate_input, width=30)
    seat_label.grid(row=1, column=0)
    seat_menu.grid(row=1, column=1)
    seatnumber_label.grid(row=2, column=0)
    seat_num_entry.grid(row=2, column=1)
    cancel_button.grid(row=3, column=1, pady=10)
    cancellation_window.mainloop()
main_window = Tk()
main_window.title("PIA Airline Reservation")
main_window.geometry("800x600")
main_window.configure(background="grey")

def seat_reservation():
        print("Seat Reservation")
        reserve_window()
        global values
        passenger_name, passenger_id, passenger_seat, seat_num, passenger_luggage = values
        passenger = Passenger(passenger_name, str(passenger_id), passenger_luggage)
        required_seat = Seat(str(passenger_seat), int(seat_num), passenger)
        values = []
        management.get_plane_details(1).book_seat(required_seat)
        update()
        update_seating_plan(management.get_plane_details(1))
            
def seat_cancellation():
     global values
     cancel_window()
     seat_type, seat_number = values

     for seat in management.get_plane_details(1).seats:
        if seat.seat_type == seat_type and seat.seat_number == int(seat_number):
            seat.occupied_by = "unoccupied"
     values = []

     update()
     update_seating_plan(management.get_plane_details(1))

def load_file():
    global management
    management = pickle.load(open("save_file.save", "rb"))
    update()
    update_seating_plan(management.get_plane_details(1))

def save_file():
    pickle.dump(management, open("save_file.save", "wb"))

def read_isi_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    registry = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()[1:]  # Skip header

    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            registry[parts[0]] = parts[1]  # ID -> Status

    return registry
  

state_registry = read_isi_data("isidata.txt")


class Seat:
    def __init__(self, seat_type, seat_number, occupied_by="unoccupied"):
           self.seat_type = seat_type
           self.seat_number = seat_number
           self.occupied_by = occupied_by

    def __eq__(self, other):
          return (self.seat_type == other.seat_type) and (self.seat_number == other.seat_number)
    

class Passenger:
      def __init__(self, name, id, luggage, status=""):
            self.name = name
            self.id = id
            self.luggage = luggage
            if self.id in state_registry.keys():
                self.status = state_registry[self.id]
            else:
                self.status = "unknown"


class Plane:
    def __init__(self, plane_number, economy_seats, business_seats, student_seats):
           self.plane_number = plane_number
           self.seats = []
           self.economy_seats = economy_seats
           self.business_seats = business_seats
           self.student_seats = student_seats
           self.luggage_cap = 1000

    def create_seats(self):
        for seat_num in range(1, self.economy_seats + 1, 1):
            self.seats.append(Seat("Economy", seat_num))
        for seat_num in range(1, self.business_seats + 1, 1):
            self.seats.append(Seat("Business", seat_num))
        for seat_num in range(1, self.student_seats + 1, 1):
            self.seats.append(Seat("Student", seat_num))
    
    def check_seat_availability(self, type, number):
        seat_availabe = False
        for seat in self.seats:
            if Seat(type, number) == seat:
                  if seat.occupied_by == "unoccupied":
                       seat_availabe = True
        return seat_availabe
    
    def book_seat(self, book_seat: Seat):
          for seat in self.seats:
                if seat == book_seat:
                      seat.occupied_by = book_seat.occupied_by
                      self.luggage_cap -= int(book_seat.occupied_by.luggage)
class PIAManagement:
    plane_number = 1
    def __init__(self):
        self.fleet = []

    def add_plane(self, plane: Plane):
        plane.create_seats()
        plane.plane_number = PIAManagement.plane_number
        PIAManagement.plane_number += 1
        self.fleet.append(plane)

    def get_plane_details(self, number):
         for plane in self.fleet:
              if plane.plane_number == number:
                   return plane

management = PIAManagement()
plane = Plane(1, economy_seats=24, business_seats=12, student_seats=8)

management.add_plane(plane)

def update():
    for widget in main_window.winfo_children():
        widget.destroy()
    button_frame = LabelFrame(main_window)
    button_frame.pack(expand="no", fill="both")

    frame_txt = Label(button_frame,text="PIA Ticket Reservation",font=("Arial", 18))

    btn_reservation = Button(button_frame,command=seat_reservation,text="Seat Reservation",activebackground="green",activeforeground="white",bd=1,font=("Arial", 12))
    btn_cancellation = Button(button_frame,text="Seat Cancellation",command=seat_cancellation,activebackground="green",activeforeground="white",bd=1,font=("Arial", 12))
    separator = Label(button_frame,text="-----------------------",font=("Arial", 18), pady=5)

    btn_load = Button(button_frame,text="Load from File",command=load_file,activebackground="green",activeforeground="white",bd=1,font=("Arial", 12))

    btn_save = Button(button_frame,text="Save to File",command=save_file,activebackground="green",activeforeground="white",bd=1,font=("Arial", 12))

    seating_frame = LabelFrame(main_window)
    business_label = Label(seating_frame, text="Business Class", font=("Arial", 14), foreground="blue")
    economy_label = Label(seating_frame, text="Economy Class", font=("Arial", 14), foreground="blue")
    student_label = Label(seating_frame, text="Student Class", font=("Arial", 14), foreground="blue")

    business_box = Listbox(seating_frame, font=("Arial", 14), width=20)
    economy_box = Listbox(seating_frame, font=("Arial", 14), width=20)
    student_box = Listbox(seating_frame, font=("Arial", 14), width=20)
    for seat in management.get_plane_details(1).seats:
        if seat.seat_type == "Business" and seat.occupied_by != "unoccupied":
            business_box.insert(business_box.size() + 1, seat.occupied_by.name)
        elif seat.seat_type == "Economy" and seat.occupied_by != "unoccupied":
            economy_box.insert(economy_box.size() + 1, seat.occupied_by.name)
        elif seat.seat_type == "Student" and seat.occupied_by != "unoccupied":
             student_box.insert(student_box.size() + 1, seat.occupied_by.name)
        business_box.grid(row=1,column=0, padx=25)
        economy_box.grid(row=1,column=1, padx=25)
        student_box.grid(row=1,column=2, padx=25)
    business_label.grid(row=0,column=0)
    economy_label.grid(row=0,column=1)
    student_label.grid(row=0,column=2)

    seating_frame.pack(expand="yes", fill="both", padx=10, pady=10)

    frame_txt.pack(pady=5)
    btn_reservation.pack(pady=5)
    btn_cancellation.pack(pady=5)
    separator.pack()
    btn_load.pack(pady=5)
    btn_save.pack(pady=5)

update()

seating_window = Tk()
seating_window.title("Seating Plan")
seating_window.geometry("300x650")
seating_window.grid_rowconfigure(0, weight=1)
seating_frame = LabelFrame(seating_window, padx=10, pady=10)

def update_seating_plan(plane):
    revenue = 0
    seats_occupied = 0
    for widget in seating_frame.winfo_children():
        widget.destroy()
    plane_label = Label(seating_frame, text=f"Plane Number {plane.plane_number}", font=("Arial", 14, "bold"))
    business_label = Label(seating_frame, text="Business Class", font=("Arial", 14), foreground="blue")


    for i in range(1, plane.business_seats + 1):
        seat_label = Button(seating_frame, text=f"{i}", font=("Arial", 10), width=5, state="disabled")
        seat_label.grid(row= 2 + (i-1)//3, column=(i-1) % 3)
        for seat in plane.seats:
            if seat.seat_number == i and seat.seat_type == "Business":
                if seat.occupied_by != "unoccupied":
                    seats_occupied += 1
                    revenue += 200000
                    if seat.occupied_by.status == "CLEAN":
                        seat_label.configure(background="green", foreground="white", state="normal")
                    elif seat.occupied_by.status == "TERRORIST":
                        seat_label.configure(background="red", foreground="white", state="normal")
                    else:
                        seat_label.configure(background="orange", foreground="white", state="normal")
    economy_label = Label(seating_frame, text="Economy Class", font=("Arial", 14), foreground="blue")

    
    for i in range(1, plane.economy_seats + 1):
        seat_label = Button(seating_frame, text=f"{i}", font=("Arial", 10), width=5, state="disabled")
        for seat in plane.seats:
            if seat.seat_number == i and seat.seat_type == "Economy":
                if seat.occupied_by != "unoccupied":
                    seats_occupied += 1
                    revenue += 100000
                    if seat.occupied_by.status == "CLEAN":
                        seat_label.configure(background="green", foreground="white", state="normal")
                    elif seat.occupied_by.status == "TERRORIST":
                        seat_label.configure(background="red", foreground="white", state="normal")
                    else:
                        seat_label.configure(background="orange", foreground="white", state="normal")
        seat_label.grid(row= 8 + (i-1)//3, column=(i-1) % 3)
    student_label = Label(seating_frame, text="Student Class", font=("Arial", 14), foreground="blue")


    for i in range(1, plane.student_seats + 1):
        seat_label = Button(seating_frame, text=f"{i}", font=("Arial", 10), width=5,  state="disabled")
        for seat in plane.seats:
            if seat.seat_number == i and seat.seat_type == "Student":
                if seat.occupied_by != "unoccupied":
                    seats_occupied += 1
                    revenue += 40000
                    if seat.occupied_by.status == "CLEAN":
                        seat_label.configure(background="green", foreground="white", state="normal")
                    elif seat.occupied_by.status == "TERRORIST":
                        seat_label.configure(background="red", foreground="white", state="normal")
                    else:
                        seat_label.configure(background="orange", foreground="white", state="normal")
        seat_label.grid(row= 19 + (i-1)//3, column=(i-1) % 3)

    seats_occupied = Label(seating_frame, text=f"Seats Occupied: {seats_occupied}", font=("Arial", 12, "bold"))
    cargo_label = Label(seating_frame, text=f"Cargo Filled: {int((1000-plane.luggage_cap)/10)}%", font=("Arial", 12, "bold"))
    revenue_label = Label(seating_frame, text=f"Revenue: Rs{revenue}", font=("Arial", 12, "bold"))

    plane_label.grid(row=0, column=1)
    business_label.grid(row=1, column=1)
    economy_label.grid(row=7, column=1)
    student_label.grid(row=18, column=1)
    seats_occupied.grid(row=25, column=1)
    cargo_label.grid(row=26, column=1)
    revenue_label.grid(row=27, column=1)
    seating_frame.pack(expand="yes", fill="both")
    seating_window.mainloop()


update_seating_plan(management.get_plane_details(1))
main_window.mainloop()