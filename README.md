# Airline Check-In Script
## Installation and Use Instructions

This script, if run over 24 hours before my favorite airline's check-in, will check you in to your flight exactly 24 hours before the scheduled departure time, thus increasing the likelihood of a good seat.

### Installation
This script has a few dependencies that must be installed before use.

##### Chromedriver
The easiest way to install this is with Homebrew. In a command line window, run `brew install chromedriver` and it will be automatically installed.

If you do not have Homebrew installed, follow the instructions on [its website](https://brew.sh/ "Homebrew").

##### Splinter
To install the splinter library to Python, use pip by running `sudo pip install splinter`. You may have to enter your password.

### Preparation
To use the check-in script, copy the Python file of your choice (checkin.py OR checkin-user-prompt.py) to the "Ready-to-Run" folder, since python files in that folder are ignored by git. Choose checkin.py if you feel comfortable opening the file and modifying fields. Otherwise, you can choose checkin-user-prompt.py, since that one will prompt you to enter the needed fields.

If you chose the former, open the Python file (checkin.py) and modify any relevant information for your flight. Make sure to follow instructions and not modify anything outside of the box. Additionally, the single quotes should be straight quotes rather than curly quotes.

### Use
This script is compatible with both Python 2.7 and 3.

In a Terminal window, navigate to the folder in which the Python file is located (using `cd`). Then, run the file with `python checkin.py` or `python checking-user-prompt.py`. If the latter, enter your information when prompted! Make sure to leave both Terminal and your computer open, awake, and with an internet connection running until it checks in to your flight for you!

*Safe travels!*
