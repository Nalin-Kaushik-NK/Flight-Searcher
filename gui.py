from tkinter import *
import flight_searcher
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import json
from datetime import datetime, timezone


# ---------------------------------------------------------------Login Function --------------------------------------
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        with open("customers.json", "r") as file:
            data = json.load(file)
            data = data["customers"]
            # print(data)
            for temp in data:
                if temp["username"] == user_name.get() and temp["password"] == password.get():
                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    close()
                    dashboard(temp)
            else:
                messagebox.showerror("Error", "Invalid User Name Or Password", parent=win)


# ------------------------------------------------ End Login Function ---------------------------------

# ------------------------------------------------- DeshBoard Panel -----------------------------------------
def display_flights(data, user):
    des = Tk()
    des.title("Flight Manager")
    des.maxsize(width=1100, height=500)
    des.minsize(width=1100, height=500)

    # img = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))
    # # Add image to the Canvas Items
    # canvas = Canvas(des, width=900, height=400)
    # canvas.create_image(0, 0, anchor='nw', image=img)
    # canvas.pack()

    label = Label(des, text="DETAILS", font='Verdana 25 bold')
    label.place(x=450, y=20)

    flight_no_l = Label(des, text="Flight no.", font='Verdana 11 bold')
    flight_no_l.place(x=20, y=90)

    airline_l = Label(des, text=f"Airline", font='Verdana 11 bold')
    airline_l.place(x=20, y=125)

    from_country_l = Label(des, text="Departure", font='Verdana 11 bold')
    from_country_l.place(x=20, y=160)

    to_country_l = Label(des, text="Destination", font='Verdana 11 bold')
    to_country_l.place(x=20, y=195)

    date_l = Label(des, text="Date", font='Verdana 11 bold')
    date_l.place(x=20, y=230)

    departure_time_l = Label(des, text="Departure Time", font='Verdana 11 bold')
    departure_time_l.place(x=20, y=265)

    arrival_time_l = Label(des, text="Arrival Time", font='Verdana 11 bold')
    arrival_time_l.place(x=20, y=300)

    total_duration = Label(des, text="Total Duration", font='Verdana 11 bold')
    total_duration.place(x=20, y=335)

    distance = Label(des, text="Distance", font='Verdana 11 bold')
    distance.place(x=20, y=370)

    availability_l = Label(des, text="availability", font='Verdana 11 bold')
    availability_l.place(x=20, y=405)

    bag = Label(des, text="Luggage Weight", font='Verdana 11 bold')
    bag.place(x=520, y=90)

    extra_bag = Label(des, text="Extra luggage price", font='Verdana 11 bold')
    extra_bag.place(x=520, y=125)

    fare_l = Label(des, text="Fare", font='Verdana 11 bold')
    fare_l.place(x=520, y=160)
    # canvas.create_rectangle(0, 280, 800, 282, fill="black")
    # canvas.pack()

    i = len(data)
    j = 0
    if i == 0:
        messagebox.showinfo(" ", "No flight Available", parent=win)
        close()
        dashboard(user)

    while True:
        details = data[j]
        j += 1
        temp = details['utc_departure']
        dpt = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
        temp = details['utc_arrival']
        arv = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)

        flight_no_l = Label(des, text=f"{details['flight_no']}", font='Verdana 10 bold')
        flight_no_l.place(x=220, y=90)

        airline_l = Label(des, text=f"{details['airline']}", font='Verdana 10 normal')
        airline_l.place(x=220, y=125)

        from_country_l = Label(des,
                               text=f"{details['from']['airport']}, {details['from']['city']}, {details['from']['country']}",
                               font='Verdana 10 normal')
        from_country_l.place(x=220, y=160)

        to_country_l = Label(des,
                             text=f"{details['to']['airport']}, {details['to']['city']}, {details['to']['country']}",
                             font='Verdana 10 normal')
        to_country_l.place(x=220, y=195)

        date_l = Label(des, text=f"{dpt.strftime('%d-%m-%Y')}", font='Verdana 10 normal')
        date_l.place(x=220, y=230)

        departure_time_l = Label(des, text=f"{dpt.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        departure_time_l.place(x=220, y=265)

        arrival_time_l = Label(des, text=f"{arv.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        arrival_time_l.place(x=220, y=300)

        time = details['duration']
        time //=60
        min = time%60
        hr = time//60
        total_duration = Label(des, text=f"{hr} HR {min} min", font='Verdana 10 normal')
        total_duration.place(x=220, y=335)

        distance = Label(des, text=f"{details['distance']} Km", font='Verdana 10 normal')
        distance.place(x=220, y=370)

        availability_l = Label(des, text=f"{details['availability']}", font='Verdana 10 normal')
        availability_l.place(x=220, y=405)

        bag_limit = Label(des, text=f"{details['bag_limit']} Kg", font='Verdana 10 normal')
        bag_limit.place(x=720, y=90)

        extra_bag_cost = Label(des, text=f"₹ {details['bags_price']['1']} per bag", font='Verdana 10 normal')
        extra_bag_cost.place(x=720, y=125)

        fare_1 = Label(des, text=f"Adult : ", font='Verdana 10 bold')
        fare_1.place(x=720, y=160)
        fare_2 = Label(des, text=f"₹ {details['fare']['adults']}", font='Verdana 10 normal')
        fare_2.place(x=810, y=160)

        fare_3 = Label(des, text=f"Children : ", font='Verdana 10 bold')
        fare_3.place(x=720, y=195)
        fare_4 = Label(des, text=f"₹ {details['fare']['children']}", font='Verdana 10 normal')
        fare_4.place(x=810, y=195)

        break

def display_flights2(data, user):
    des = Tk()
    des.title("Flight Manager")
    des.maxsize(width=1000, height=680)
    des.minsize(width=1000, height=680)

    # img = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))
    # # Add image to the Canvas Items
    # canvas = Canvas(des, width=900, height=400)
    # canvas.create_image(0, 0, anchor='nw', image=img)
    # canvas.pack()

    Label(des, text="DETAILS", font='Verdana 25 bold').place(x=450, y=20)

    Label(des, text="Flight no.", font='Verdana 11 bold').place(x=20, y=90)

    Label(des, text=f"Airline", font='Verdana 11 bold').place(x=20, y=125)

    Label(des, text="Departure", font='Verdana 11 bold').place(x=20, y=160)

    Label(des, text="Destination", font='Verdana 11 bold').place(x=20, y=195)

    Label(des, text="Date", font='Verdana 11 bold').place(x=20, y=230)

    Label(des, text="Departure Time", font='Verdana 11 bold').place(x=20, y=265)

    Label(des, text="Arrival Time", font='Verdana 11 bold').place(x=20, y=300)

    Label(des, text="Total Duration", font='Verdana 11 bold').place(x=20, y=335)

    Label(des, text="Distance", font='Verdana 11 bold').place(x=20, y=370)

    Label(des, text="availability", font='Verdana 11 bold').place(x=20, y=405)

    Label(des, text="Luggage Weight", font='Verdana 11 bold').place(x=20, y=440)

    Label(des, text="Extra luggage price", font='Verdana 11 bold').place(x=20, y=475)

    Label(des, text="Fare", font='Verdana 11 bold').place(x=20, y=510)

    Label(des, text="Flight no.", font='Verdana 11 bold').place(x=520, y=90)

    Label(des, text=f"Airline", font='Verdana 11 bold').place(x=520, y=125)

    Label(des, text="Departure", font='Verdana 11 bold').place(x=520, y=160)

    Label(des, text="Destination", font='Verdana 11 bold').place(x=520, y=195)

    Label(des, text="Date", font='Verdana 11 bold').place(x=520, y=230)

    Label(des, text="Departure Time", font='Verdana 11 bold').place(x=520, y=265)

    Label(des, text="Arrival Time", font='Verdana 11 bold').place(x=520, y=300)

    Label(des, text="Total Duration", font='Verdana 11 bold').place(x=520, y=335)

    Label(des, text="Distance", font='Verdana 11 bold').place(x=520, y=370)

    Label(des, text="availability", font='Verdana 11 bold').place(x=520, y=405)

    Label(des, text="Luggage Weight", font='Verdana 11 bold').place(x=520, y=440)

    Label(des, text="Extra luggage price", font='Verdana 11 bold').place(x=520, y=475)

    Label(des, text="Fare", font='Verdana 11 bold').place(x=520, y=510)



    i = len(data)
    j = 0
    if i == 0:
        messagebox.showinfo(" ", "No flight Available", parent=win)
        close()
        dashboard(user)

    while True:
        details = data[j]
        j += 1
        temp = details['a']['utc_departure']
        dpt = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
        temp = details['a']['utc_arrival']
        arv = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)

        flight_no_l = Label(des, text=f"{details['a']['flight_no']}", font='Verdana 10 bold')
        flight_no_l.place(x=220, y=90)

        airline_l = Label(des, text=f"{details['a']['airline']}", font='Verdana 10 normal')
        airline_l.place(x=220, y=125)

        from_country_l = Label(des,
                               text=f"{details['a']['from']['airport']}, {details['a']['from']['city']}, {details['a']['from']['country']}",
                               font='Verdana 10 normal')
        from_country_l.place(x=220, y=160)

        to_country_l = Label(des,
                             text=f"{details['a']['to']['airport']}, {details['a']['to']['city']}, {details['a']['to']['country']}",
                             font='Verdana 10 normal')
        to_country_l.place(x=220, y=195)

        date_l = Label(des, text=f"{dpt.strftime('%d-%m-%Y')}", font='Verdana 10 normal')
        date_l.place(x=220, y=230)

        departure_time_l = Label(des, text=f"{dpt.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        departure_time_l.place(x=220, y=265)

        arrival_time_l = Label(des, text=f"{arv.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        arrival_time_l.place(x=220, y=300)

        time = details['a']['duration']
        time //=60
        min = time%60
        hr = time//60
        total_duration = Label(des, text=f"{hr} HR {min} min", font='Verdana 10 normal')
        total_duration.place(x=220, y=335)

        distance = Label(des, text=f"{details['a']['distance']} Km", font='Verdana 10 normal')
        distance.place(x=220, y=370)

        availability_l = Label(des, text=f"{details['a']['availability']}", font='Verdana 10 normal')
        availability_l.place(x=220, y=405)

        bag_limit = Label(des, text=f"{details['a']['bag_limit']} Kg", font='Verdana 10 normal')
        bag_limit.place(x=220, y=440)

        extra_bag_cost = Label(des, text=f"₹ {details['a']['bags_price']['1']} per bag", font='Verdana 10 normal')
        extra_bag_cost.place(x=220, y=475)

        fare_1 = Label(des, text=f"Adult : ", font='Verdana 10 bold')
        fare_1.place(x=220, y=510)
        fare_2 = Label(des, text=f"₹ {details['fare']['adults']}", font='Verdana 10 normal')
        fare_2.place(x=310, y=510)

        fare_3 = Label(des, text=f"Children : ", font='Verdana 10 bold')
        fare_3.place(x=220, y=540)
        fare_4 = Label(des, text=f"₹ {details['fare']['children']}", font='Verdana 10 normal')
        fare_4.place(x=310, y=540)


        temp = details['b']['utc_departure']
        dpt = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)
        temp = details['b']['utc_arrival']
        arv = datetime.fromisoformat(temp[:-1]).astimezone(timezone.utc)

        flight_no_l = Label(des, text=f"{details['b']['flight_no']}", font='Verdana 10 bold')
        flight_no_l.place(x=720, y=90)

        airline_l = Label(des, text=f"{details['b']['airline']}", font='Verdana 10 normal')
        airline_l.place(x=720, y=125)

        from_country_l = Label(des,
                               text=f"{details['b']['from']['airport']}, {details['b']['from']['city']}, {details['b']['from']['country']}",
                               font='Verdana 10 normal')
        from_country_l.place(x=720, y=160)

        to_country_l = Label(des,
                             text=f"{details['a']['to']['airport']}, {details['b']['to']['city']}, {details['b']['to']['country']}",
                             font='Verdana 10 normal')
        to_country_l.place(x=720, y=195)

        date_l = Label(des, text=f"{dpt.strftime('%d-%m-%Y')}", font='Verdana 10 normal')
        date_l.place(x=720, y=230)

        departure_time_l = Label(des, text=f"{dpt.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        departure_time_l.place(x=720, y=265)

        arrival_time_l = Label(des, text=f"{arv.strftime('%H:%M:%S')} utc", font='Verdana 10 normal')
        arrival_time_l.place(x=720, y=300)

        time = details['b']['duration']
        time //=60
        min = time%60
        hr = time//60
        total_duration = Label(des, text=f"{hr} HR {min} min", font='Verdana 10 normal')
        total_duration.place(x=720, y=335)

        distance = Label(des, text=f"{details['b']['distance']} Km", font='Verdana 10 normal')
        distance.place(x=720, y=370)

        availability_l = Label(des, text=f"{details['b']['availability']}", font='Verdana 10 normal')
        availability_l.place(x=720, y=405)

        bag_limit = Label(des, text=f"{details['b']['bag_limit']} Kg", font='Verdana 10 normal')
        bag_limit.place(x=720, y=440)

        extra_bag_cost = Label(des, text=f"₹ {details['b']['bags_price']['1']+23.4} per bag", font='Verdana 10 normal')
        extra_bag_cost.place(x=720, y=475)

        fare_1 = Label(des, text=f"Adult : ", font='Verdana 10 bold')
        fare_1.place(x=720, y=510)
        fare_2 = Label(des, text=f"₹ {details['fare']['adults']-400}", font='Verdana 10 normal')
        fare_2.place(x=810, y=510)

        fare_3 = Label(des, text=f"Children : ", font='Verdana 10 bold')
        fare_3.place(x=720, y=540)
        fare_4 = Label(des, text=f"₹ {details['fare']['children']-572}", font='Verdana 10 normal')
        fare_4.place(x=810, y=540)

        Label(des, text=f"Nights in Destination : ", font='Verdana 12 bold').place(x=360, y=590)
        nights_in_des = Label(des, text=f" {details['nightsInDest']} days", font='Verdana 12 normal')
        nights_in_des.place(x=570, y=590)

        break

def dashboard(user):

    def ticket_check(event):
        if ticket_type.get() == "Oneway":
            r_from_date_f.configure(state='disabled')
            r_to_date_f.configure(state='disabled')
        else:
            r_from_date_f.configure(state='normal')
            r_to_date_f.configure(state='normal')

    def details():
        flight = flight_searcher.FlightSearch()
        flight_data = flight.get_flight_details(from_country.get(), from_city.get(), to_country.get(),
                                                to_city.get(), from_date.get(), to_date.get(), ticket_type.get(),
                                                return_date_from.get(), return_date_to.get())
        # print(flight_data)
        if ticket_type.get() == 'oneway':
            display_flights(flight_data, user)
        else:
            display_flights2(flight_data, user)

    def clear():
        from_country.delete(0, END)
        to_country.delete(0, END)
        from_city.delete(0, END)
        to_city.delete(0, END)
        from_date.delete(0, END)
        to_date.delete(0, END)
        ticket_type.delete(0, END)
        return_date_to.delete(0, END)
        return_date_from.delete(0, END)

    des = Tk()
    des.title("Flight Manager")
    des.maxsize(width=1100, height=500)
    des.minsize(width=1100, height=500)

    s = ttk.Style()

    img = ImageTk.PhotoImage(Image.open("images/bg6.jpg"))

    # Add image to the Canvas Items
    canvas = Canvas(des, width=900, height=400)
    canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.pack()

    # heading label
    heading = Label(des, text=f"FLIGHT SEARCH", font='Verdana 22 bold')
    heading.place(x=400, y=40)

    from_country = StringVar()
    from_city = StringVar()
    to_country = StringVar()
    to_city = StringVar()
    from_date = StringVar()
    to_date = StringVar()
    ticket_type = StringVar()
    return_date_to = StringVar()
    return_date_from = StringVar()

    from_country_l = Label(des, text="From Country", font='Verdana 10 bold')
    from_country_l.place(x=80, y=150)
    from_country_f = Entry(des, width=20, textvariable=from_country)
    from_country_f.place(x=190, y=150)

    from_city_l = Label(des, text="From City", font='Verdana 10 bold')
    from_city_l.place(x=80, y=220)
    from_city_f = Entry(des, width=20, textvariable=from_city)
    from_city_f.place(x=190, y=220)

    to_country_l = Label(des, text="To Country", font='Verdana 10 bold')
    to_country_l.place(x=430, y=150)
    to_country_f = Entry(des, width=20, textvariable=to_country)
    to_country_f.place(x=520, y=150)

    to_city_l = Label(des, text="To City", font='Verdana 10 bold')
    to_city_l.place(x=430, y=220)
    to_city_f = Entry(des, width=20, textvariable=to_city)
    to_city_f.place(x=520, y=220)

    from_date_l = Label(des, text="From Date", font='Verdana 10 bold')
    from_date_l.place(x=80, y=290)
    from_date_f = Entry(des, width=20, textvariable=from_date)
    from_date_f.place(x=190, y=290)

    to_date_l = Label(des, text="To Date", font='Verdana 10 bold')
    to_date_l.place(x=430, y=290)
    to_date_f = Entry(des, width=20, textvariable=to_date)
    to_date_f.place(x=520, y=290)

    r_from_date_l = Label(des, text="Return Date from", font='Verdana 10 bold')
    r_from_date_l.place(x=760, y=220)
    r_from_date_f = Entry(des, width=20, textvariable=return_date_from, state='disable')
    r_from_date_f.place(x=900, y=220)

    r_to_date_l = Label(des, text="Return Date to", font='Verdana 10 bold')
    r_to_date_l.place(x=760, y=290)
    r_to_date_f = Entry(des, width=20, textvariable=return_date_to, state='disable')
    r_to_date_f.place(x=900, y=290)

    options = ["oneway", "round"]

    ticket_type.set("oneway")
    return_l = Label(des, text="Ticket Type", font='Verdana 10 bold')
    return_l.place(x=760, y=150)
    return_f = OptionMenu(des, ticket_type, *options, command=ticket_check)
    return_f.place(x=900, y=150)

    btn_search = Button(des, text="Search", font='Verdana 15 bold', height=2, width=38, command=details, relief="groove")
    btn_search.place(x=20, y=370)

    btn_clr = Button(des, text="Clear", font='Verdana 15 bold', height=2, width=37, command=clear, relief="groove")
    btn_clr.place(x=552, y=370)


# ------------------------------------------------- End Deshboard Panel --------------------------------------------
# ------------------------------------------------- Signup Window --------------------------------------------------

def signup():
    def action():
        if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                exist = False
                # with open("customers.json", "r") as fl:
                #     data = json.load(fl)
                #     if data[user_name.get()]["username"] == user_name.get():
                #         exist = True
                if exist:
                    messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                else:
                    format = {
                        "fname": first_name.get(),
                        "lname": last_name.get(),
                        "username": user_name.get(),
                        "password": password.get()
                    }

                    with open("customers.json", "r") as outfile:
                        file_data = json.load(outfile)

                    with open("customers.json", "w") as outfile:
                        file_data["customers"].append(format)
                        json.dump(file_data, outfile, indent=4)
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        first_name.delete(0, END)
        last_name.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window

    winsignup = Tk()
    winsignup.title("Flight Manager")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    # heading label
    heading = Label(winsignup, text="Signup", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name = Label(winsignup, text="First Name :", font='Verdana 10 bold')
    first_name.place(x=80, y=130)

    last_name = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
    last_name.place(x=80, y=160)

    user_name = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name.place(x=80, y=190)

    password = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password.place(x=80, y=220)

    very_pass = Label(winsignup, text="Verify Password:", font='Verdana 10 bold')
    very_pass.place(x=80, y=250)

    # --------------------------------------------- Entry Box -----------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=40, textvariable=first_name)
    first_name.place(x=200, y=133)

    last_name = Entry(winsignup, width=40, textvariable=last_name)
    last_name.place(x=200, y=163)

    user_name = Entry(winsignup, width=40, textvariable=user_name)
    user_name.place(x=200, y=193)

    password = Entry(winsignup, width=40, textvariable=password)
    password.place(x=200, y=223)

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=200, y=253)

    # button login and clear

    btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=action)
    btn_signup.place(x=200, y=313)

    btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear)
    btn_login.place(x=290, y=313)

    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()


# ----------------------------------------------------------- End Singup Window ------------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------


win = Tk()
win.title("Flight Manager")
# app title
# window size
win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

# heading label
heading = Label(win, text="Login", font='Lucida 25 bold')
heading.place(x=200, y=150)

username = Label(win, text="User Name :", font='Verdana 10 bold')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 10 bold')
userpass.place(x=80, y=260)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

# button login and clear

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login, foreground="green",
                   activebackground="green", activeforeground="white", relief="groove")
btn_login.place(x=200, y=293)

btn_clr = Button(win, text="Clear", font='Verdana 10 bold', command=clear, foreground="red",
                   activebackground="red", activeforeground="white", relief="groove")
btn_clr.place(x=270, y=293)

# signup button

sign_up_btn = Button(win, text="Switch To Sign up", command=signup, foreground="black",
                     activebackground="green", activeforeground="white", relief="groove")
sign_up_btn.place(x=350, y=20)

win.mainloop()
