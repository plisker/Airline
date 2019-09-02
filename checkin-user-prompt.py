import sys
import checkin

###############################################################################
# Do not modify anything
###############################################################################


def main():
    while True:
        print("What is your confirmation number?")
        confirmation_number = checkin.get_input()
        if len(confirmation_number) != 6:
            print("Confirmation number should be six characters long")
        else:
            break

    print("What is your first name?")
    first_name = checkin.get_input()

    print("What is your last name?")
    last_name = checkin.get_input()

    while True:
        print("Do you want check in now, or schedule it?")
        print("Enter 1 to check in now, or 2 to schedule.")
        now_or_schedule = checkin.get_input()
        now_or_schedule = int(now_or_schedule)
        if now_or_schedule == 1:
            return checkin.now(confirmation_number, first_name, last_name)
        if now_or_schedule == 2:
            break
        else:
            print("That is not a valid day of the month")

    while True:
        print("What is the day of your departure?")
        departure_day = checkin.get_input()
        departure_day = int(departure_day)
        if departure_day not in range(1, 32):
            print("That is not a valid day of the month")
        else:
            break

    while True:
        print("What is the month of your departure?")
        departure_month = checkin.get_input()
        departure_month = int(departure_month)
        if departure_month not in range(1, 13):
            print("That is not a valid day of the month")
        else:
            break

    print("What is the year of your departure?")
    departure_year = checkin.get_input()  # 4 digits
    departure_year = int(departure_year)

    while True:
        print("What is the hour of your departure? (Not full time, " +
              "just the hour.) Please use 24-hour format.")
        departure_hour = checkin.get_input()  # 24 hour format
        departure_hour = int(departure_hour)
        if departure_hour not in range(25):
            print("That is not a valid hour. " +
                  "Remember that midnight is simply 0.")
        else:
            break

    while True:
        print("What is the minute of your departure?")
        departure_minute = checkin.get_input()
        departure_minute = int(departure_minute)
        if departure_minute not in range(61):
            print("That is not a valid minute")
        else:
            break
    print("Thank you! Loading . . .")

    return checkin.main(confirmation_number, first_name, last_name, departure_day,
                        departure_month, departure_year, departure_hour,
                        departure_minute)


if __name__ == "__main__":
    browser = main()
