# bread_cat_eora
It's an example project for HRs that won't be finished soon. 

This script runs @bread_cat_bot

# How to set up
With a single command using Docker: https://hub.docker.com/r/urusaitech/breadcat

Or manually: 
- download scripts in a single folder
- install python 3+ if neccessary
- in python use this command: **pip install -r requirements**  (if any issues, install packages manually or use IDE and store all scripts in one project)
- run bread_cat_bot.py
- send '/start' command to @bread_cat_bot

**Commands:**

'/start' - launches the bot and resets its state if the bot is already on

User can navigate through the bot via buttons, or using text messages. 

# API
In development.
There would be an end-point with a single POST method. 

# DataBase

When called from Telegram, the bot stores the following information using SQLite3:
- nickname of the user
- id of the chat
- user's message
- time of the message

The database is stored locally in the folder of the script, and saves only the message with /start command. The name of the database: 'messages'.

# Functions

**insert_data**(username, chatid, message, time) - creates a table in the folder of the script if not already exist, and writes info passed from bot_start().

**bot_start**(message) - asynchronous function initialized by '/start' command, sends welcome message and launches insert_data().

**first_state**(message, state) - asynchronous function that handles the first reply after the /start command, changes state of DetectObject class if a user choosed 'yes', sends message and returns nothing if choosed 'no'.

**second_state**(message, state) - asynchronous function that handles the second reply after the /start command, resets state of DetectObject class if a user choosed 'yes', sends message and returns nothing if choosed 'no'.

**register_handlers_state**(dp) - registers bot_start(), first_state(), and second_state() functions.

**main**() - runs the script

# Logging

The bot has ability to log it's state, can be turned on by uncomment ING part of the main() function 
