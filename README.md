The Telegram Recipe Bot is a bot that allows users to access and add recipes for various categories of dishes, including meat, pizza, fish, desserts, and vegetarian. Users can also access general cooking tips through the bot.

Usage

To use the bot, follow these steps:

Open Telegram and search for the bot username: @telegram_recipe_bot.
Click on the bot to open a chat window.
Use the following commands to interact with the bot:
/start: Start the bot and see the main menu.
/meat: Access meat recipes.
/pizza: Access pizza recipes.
/fish: Access fish recipes.
/desserts: Access dessert recipes.
/vegetarian: Access vegetarian recipes.
/add_recipe: Add a new recipe.
/useful_tips: Access useful cooking tips.
Features

Access recipes for various categories of dishes.
Add new recipes to the bot's database.
Access general cooking tips.

Database

The bot's database stores the following information:

Recipes: Type of dish, name of dish, recipe instructions, and image.
Tips: Text of the tip.

Requirements

To run the bot, you'll need:

Python 3
python-telegram-bot library
MongoDB
Installation

To install and run the bot, follow these steps:

Clone the repository: git clone https://github.com/obelousov/masha_telebot_2.git
Install the required libraries: pip install -r requirements.txt
Set up a MongoDB database and add the connection string to config.py.
Run the bot: python bot.py
License

This project is licensed under the MIT License - see the LICENSE file for details.

Credits
This bot was created by Maria Belousova.
