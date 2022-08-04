# bread_cat_eora

This script runs @bread_cat_bot

# How to launch
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

You can send commands to this bot using http request after running bread_cat_api.py script.
API doesn't use methods or decorators and runs console text interface instead.

Authentication is not released yet so you have to manually send to the bot an ID of the chat with the bot. 
Afterwards the bot will send answer both to your STDOUT and Telegram chat. 

# DataBase

When called from Telegram, the bot stores the following information using SQLite3:
- nickname of the user
- id of the chat
- user's message
- time of the message

The database is stored locally in the folder of the script, and saves only the message with /start command. The name of database: 'messages'.
