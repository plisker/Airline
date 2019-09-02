from __future__ import print_function
import sys
from threading import Timer
from datetime import datetime, timedelta
import time
import splinter as sp

# Do not modify anything above this line
###############################################################################
# Enter personal info here!

confirmation_number = 'ABC123'
first_name = 'PAUL'
last_name = 'LISKER'
departure_day = 16
departure_month = 9
departure_year = 2016   # 4 digits
departure_hour = 18     # 24 hour format
departure_minute = 50

###############################################################################
# Do not modify anything below this line


def checkin(browser):
    time.sleep(3)  # To make sure that their server allows for checking in.
    checkin_button = browser.find_by_id('form-mixin--submit-button')
    checkin_button.click()
    time.sleep(3)
    print_documents_button = browser.find_by_css('button')[7]
    print_documents_button.click()
    print('Checked in at', datetime.now())
    print("")
    quit(browser)
    return


def get_input():
    get_user_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_user_input = raw_input

    return get_user_input()


def quit(browser):
    print("When you're finished, click enter to close the browser session.")
    get_input()
    browser.quit()


def now(confirmation_number, first_name, last_name):
    # Hard coded date of January 1, 2000 at midnight to ensure past date
    return main(confirmation_number, first_name, last_name, 1, 1, 2000, 0, 0)


def main(confirmation_number, first_name, last_name, departure_day,
         departure_month, departure_year, departure_hour, departure_minute):
    browser = sp.Browser('chrome')
    browser.visit('https://www.southwest.com/air/check-in/index.html')
    browser.find_by_id('confirmationNumber').fill(confirmation_number)
    browser.find_by_id('passengerFirstName').fill(first_name)
    browser.find_by_id('passengerLastName').fill(last_name)

    departure = datetime(departure_year,
                         departure_month,
                         departure_day,
                         departure_hour,
                         departure_minute, 1)
    checkin_time = departure - timedelta(days=1)
    now = datetime.now()
    delta_t = checkin_time - now
    secs = delta_t.seconds + 10  # Grace period of 10 sec to ensure check-in

    print('Now:', now)
    print('Check-In Time:', checkin_time)

    if (secs < 0) or (now > checkin_time):
        checkin(browser)
    else:
        days, hours, minutes, seconds = delta_t.days, delta_t.seconds // 3600, delta_t.seconds // 60 % 60, delta_t.seconds % 60
        if days > 0:
            print('Waiting', days, 'days,', hours, 'hours,', minutes,
                  'minutes, and', seconds, 'seconds before checking in...')
        elif hours > 0:
            print('Waiting', hours, 'hours,', minutes, 'minutes, and',
                  seconds, 'seconds before checking in...')
        elif minutes > 0:
            print('Waiting', minutes, 'minutes and',
                  seconds, 'seconds before checking in...')
        else:
            print('Waiting', seconds, 'seconds before checking in...')

        timer = Timer(secs, checkin, [browser])
        timer.start()

    return browser


if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    browser = main(confirmation_number, first_name, last_name, departure_day,
                   departure_month, departure_year, departure_hour,
                   departure_minute)

    print("When you're finished, click enter to close the browser session.")
    get_input()
    browser.quit()
