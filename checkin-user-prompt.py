import checkin
import sys

################################################################################
# Do not modify anything
################################################################################

def main():
    while True:
        print("What is your confirmation number?")
        confirmationNumber = get_input()
        if len(confirmationNumber) != 6:
            print("Confirmation number should be six characters long")
        else:
            break

    print("What is your first name?")
    firstName = get_input()

    print("What is your last name?")
    lastName = get_input()
    
    while True:
        print("What is the day of your departure?")
        departure_day = get_input()
        departure_day = int(departure_day)
        if departure_day not in range(1,32):
            print("That is not a valid day of the month")
        else:
            break
    
    while True:
        print("What is the month of your departure?")
        departure_month = get_input()
        departure_month = int(departure_month)
        if departure_month not in range(1,13):
            print("That is not a valid day of the month")
        else:
            break
    
    print("What is the year of your departure?")
    departure_year = get_input() # 4 digits
    departure_year = int(departure_year)
    
    while True:
        print("What is the hour of your departure? (Not full time, just the hour.) Please use 24-hour format.")
        departure_hour = get_input() # 24 hour format
        departure_hour = int(departure_hour)
        if departure_hour not in range(25):
            print("That is not a valid hour. Remember that midnight is simply 0.")
        else:
            break
    
    while True:
        print("What is the minute of your departure?")
        departure_minute = get_input()
        departure_minute = int(departure_minute)
        if departure_minute not in range(61):
            print("That is not a valid minute")
        else:
            break
    print("Thank you! Loading . . .")

    return checkin.main(confirmationNumber, firstName, lastName, departure_day, departure_month, departure_year, departure_hour, departure_minute)

if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    browser = main()


