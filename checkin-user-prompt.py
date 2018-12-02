import checkin
import sys

################################################################################
# Do not modify anything
################################################################################

def main():
    while True:
        print("What is your confirmation number?")
        confirmationNumber = checkin.get_input()
        if len(confirmationNumber) != 6:
            print("Confirmation number should be six characters long")
        else:
            break

    print("What is your first name?")
    firstName = checkin.get_input()

    print("What is your last name?")
    lastName = checkin.get_input()
    
    while True:
        print("What is the day of your departure?")
        departure_day = checkin.get_input()
        departure_day = int(departure_day)
        if departure_day not in range(1,32):
            print("That is not a valid day of the month")
        else:
            break
    
    while True:
        print("What is the month of your departure?")
        departure_month = checkin.get_input()
        departure_month = int(departure_month)
        if departure_month not in range(1,13):
            print("That is not a valid day of the month")
        else:
            break
    
    print("What is the year of your departure?")
    departure_year = checkin.get_input() # 4 digits
    departure_year = int(departure_year)
    
    while True:
        print("What is the hour of your departure? (Not full time, just the hour.) Please use 24-hour format.")
        departure_hour = checkin.get_input() # 24 hour format
        departure_hour = int(departure_hour)
        if departure_hour not in range(25):
            print("That is not a valid hour. Remember that midnight is simply 0.")
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

    return checkin.main(confirmationNumber, firstName, lastName, departure_day, departure_month, departure_year, departure_hour, departure_minute)

if __name__ == "__main__":
    browser = main()


