# Hospice Manager


## Purpose

This project is meant to assist healthcare workers, specifically hospice providers,
with managing their assigned facilities and patients.
Functionality within the Command-Line Interface menu includes:
  + listing all assigned facilities,
  + listing all patients in concordance with their respective facilities,
  + adding, removing, and updating facilities,
  + and adding, removing, and updating patients

---

## Installation

1. After you've forked and cloned this repo to your local environment, 
open the project and run

`pipenv install`

in your terminal to install the necessary dependencies.

2. To get the database up and ready to accept new facilities and patients, run

`python lib/config.py`

OR 

If you're looking for an example of how the project functions, run

`python lib/seed.py`

to prefill the database with example facilities and patients.

3. Finally, run

`python lib/cli.py`

to enter the CLI menu and follow the prompts to facilitate your workflow!

4. If at any point you accidentally exit out of the CLI menu entirely, just re-run

`python lib/cli.py`

---

## Usage

Once inside the CLI
  + enter the number that precedes whichever option you'd like to select,
  + follow the prompts,
  + repeat until you're ready to exit

---

#### Notes
As always, I'd appreciate any and all feedback and constructive criticism! Thanks for visiting!