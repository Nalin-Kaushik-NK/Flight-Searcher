from tkinter import *
import gui
import data_manager
import pprint
import flight_searcher
import notification_manager
import datetime
# MY_CITY = "LON"
#
# data_manager = data_manager.DataManager()
# sheet_data = data_manager.get_data()
#
# # ---------------------- Iata Code filler ----------------------
#
# for sheet_data_list in sheet_data:
#     if sheet_data_list["iataCode"] == "":
#         from flight_searcher import FlightSearch
#
#         flight_search = FlightSearch()
#         for row in sheet_data:
#             row["iataCode"] = flight_search.get_destination_iata_code(row["city"])
#         print(f"sheet_data:\n {sheet_data}")
#
#         data_manager.main_data = sheet_data
#         data_manager.update_destination_codes()
# # ---------------------------------------------------------------
#
# flight_search = flight_searcher.FlightSearch()
# tomorrow = datetime.datetime.now()
# after_six_months = datetime.datetime.now() + datetime.timedelta(days=(6*30))
#
# for cities in sheet_data:
#     flight = flight_search.flight_cost(MY_CITY, cities, tomorrow, after_six_months)
#     # if flight and (int(cities["lowestPrice"]) > int(flight.price)):
#     #     mail_sender = notification_manager.NotificationManager()
#     #     message = f"Subject: Low Price Alert!\n\nOnly {flight.price}Euro to fly from {flight.departure_city}-{MY_CITY} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. "
#     #
#     #     if flight.stop_overs > 0:
#     #         message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
#     #         print(message)
#     #     mail_sender.mail(message)


#################################NEW####################################

# departure = 'IND'
# destination = 'NYC'
# from_day = '20/10/2022'
# to_day = '30/03/2023'
#
# obj = flight_searcher.FlightSearch()
# data = obj.get_flight_details(departure, destination, from_day, to_day)
# pprint.pprint(data)

if __name__ == "__main__":
    win = Tk()


    trail_data =  {
            "fname": "iokl",
            "lname": "po",
            "age": "poj",
            "city": "ij",
            "username": "oi",
            "password": "po"
        }

    gui.deshboard(trail_data)
    # app title
    win.title("Flight Manager")

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    # heading label
    heading = Label(win, text="Login", font='Verdana 25 bold')
    heading.place(x=80, y=150)

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

    btn_login = Button(win, text="Login", font='Verdana 10 bold', command=gui.login)
    btn_login.place(x=200, y=293)

    btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=gui.clear)
    btn_login.place(x=260, y=293)

    # signup button

    sign_up_btn = Button(win, text="Switch To Sign up", command=gui.signup)
    sign_up_btn.place(x=350, y=20)

    win.mainloop()
