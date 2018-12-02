# Airline Check-In Script
## Installation and Use Instructions

This script, if run over 24 hours before my [favorite airline's](https://www.southwest.com/) check-in, will automatically check you in to your flight as soon as checkin is allowed, thus increasing the likelihood of a good seat. This script is compatible with both Python 2.7 and 3.

## Installation
This script has a few dependencies that must be installed before use.

### Chromedriver
The easiest way to install this is with Homebrew. In a command line window, run `brew cask install chromedriver` and it will be automatically installed.

If you do not have Homebrew installed, follow the instructions on [its website](https://brew.sh/ "Homebrew").

### Splinter
To install the splinter library to Python, use pip by running `pip install splinter`. You may have to prepend `sudo` and enter your password.

### Other
You may be missing other packages not listed above, which would cause the script to fail the first time you run it. Make sure to install any other missing libraries with `pip`.

## Use
### <a name="prepare"></a>Preparing the Script [optional]
The easiest way to prepare in advance to use the script is to add your ticket info directly to the file. If you feel comfortable with this, keep reading. Alternatively, skip to the [Running the Script](#run) section.

1. Make sure that you have the latest code by running `git pull`
2. To ensure that the file you'll prepare is not overwritten, first copy the `checkin.py` file to the `Ready-to-Run` folder. Python files in that folder are ignored by git.
3. Open the Python file (`checkin.py`) with your favorite text editor (I'd suggest [Sublime](https://www.sublimetext.com/ "Sublime Text")) and modify any relevant information for your flight. Make sure to follow instructions and not modify anything outside of the box. Additionally, the single quotes should be straight quotes rather than curly quotes.

### <a name="run"></a>Running the Script
#### If you skipped the section above, follow these steps:

1. In a Terminal window, navigate to the folder in which the Python file is located (using `cd`)
2. Then, run the bash script with `./schedule_checkin.sh`. This script will automatically update your local repo with the latest code and start the Python script
3. Follow the prompts
4. Leave Terminal open and your computer open, awake, and with an Internet connection until it checks in to your flight for you
5. Enjoy your great seat!

#### If you prepared a script in advance, follow these steps:

1. In a Terminal window, navigate to the folder in which the Python file your prepared is located (using `cd`)
2. Run the file with `python checkin.py`
3. Leave Terminal open and your computer open, awake, and with an Internet connection until it checks in to your flight for you
4. Enjoy your great seat!

### Debugging
If the bash script does not work, it may have failed on some intermediate step, or it might not have permissions to run. If that is the case, run through the [Preparing the Script](#prepare) instructions and the corresponding steps to run the prepared script.

If the script fails to check you in to your flight, first make sure that you're using the most up-to-date script by first running `git pull`. If you are preparing a script in advance, try deleting the script from the `Ready-to-Run` folder and copying in a new one after git pulling.

Though unlikely, a bug may exist in some of the libraries used by the script. To update chromedriver, run `brew update && brew cask upgrade chromedriver`; upate splinter with `pip install splinter --upgrade`.

If the script is broken, let me know so that I can update it, or submit a pull request yourself!

*Safe travels!*
