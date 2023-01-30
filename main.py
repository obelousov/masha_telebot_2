import random

import telebot

from telebot import types

import sqlite3

import db
from db import getMealById

# File handling
category_meat = 1;
category_fish = 2;
category_desserts = 3;
category_pizza = 4;
category_veggies = 5;
category_tips = 6;
category_add = 7;

# with open('vegetarian.txt') as f:
#     veggies = f.read().split('\n')
#
# with open('pizza.txt') as f:
#     pizza = f.read().split('\n')
#
# with open('meat.txt') as f:
#     meat = f.read().split('\n')
#     recipe,url = db.getMealById(category_meat)
#
# with open('fish.txt') as f:
#     fish = f.read().split('\n')
#     fish = db.getMealById(2)
#
# with open('desserts.txt') as f:
#     desserts = f.read().split('\n')
#
# with open('tips') as f:
#     tip = f.read().split('\n')
#
# with open('added') as f:
#     adding = f.read().split('\n')

# Creating the bot with the token given from the bot father

bot = telebot.TeleBot('5958693209:AAEeFOmaTbyJLzcyZmbiZ9TRmkILZlWlbA8')


# Running the bot

@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Connecting to database

    connect = sqlite3.connect('fish.db')

    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS fish_recipes(

        id_dish int,

        dish_name str, 

        instructions str 

    )""")

    connect.commit()

    # Adding the buttons

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("🐟 Fish")

    item2 = types.KeyboardButton("🧁 Desserts")

    item3 = types.KeyboardButton("🥩 Meat")

    item4 = types.KeyboardButton("🍕 Pizza")

    item5 = types.KeyboardButton("🥗 Vegetarian")

    item6 = types.KeyboardButton("📌 Useful tips")

    item7 = types.KeyboardButton("📝 Add a recipe")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(m.chat.id,

                     'Press:'

                     '\n       '

                     '\n🐟 Fish for various fish recipes\n🧁 Desserts for delicious sweet courses'

                     '\n🥩 Meat, if you fancy a steak\n🍕 Pizza to find an idea for a party meal'

                     '\n🥗 Vegetarian, if you are in a salad - mood\n📌 Useful tips in case you are'

                     ' not sure how to use the equipment\n📝 Add a recipe to store your own instructions!',

                     reply_markup=markup)


# Receiving message from the user

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global answer

    match message.text.strip():

        case '🥗 Vegetarian':

            # answer = random.choice(veggies)
            category_dish = category_veggies

        case '🍕 Pizza':

            # answer = random.choice(pizza)
            category_dish = category_pizza

        case '🥩 Meat':

            # answer = random.choice(meat)
            # answer = meat
            category_dish = category_meat

        case '🐟 Fish':

            # answer = random.choice(fish)
            category_dish = category_fish

        case '🧁 Desserts':

            # answer = random.choice(desserts)
            category_dish = category_desserts

        case '📌 Useful tips':

            # answer = random.choice(tip)
            category_dish = category_tips

        case '📝 Add a recipe':

            # answer = random.choice(adding)
            category_dish = category_add

    # Sending the user the recipe
    answer, dish_name_res,instructions_res,url = db.getMealById(category_dish)
    bot.send_message(message.chat.id, dish_name_res)
    meat_url = """https://img.freepik.com/free-photo/front-view-big-meat-slice-raw-meat-with-pepper-greens-dark-photo-chicken-meal-animal-barbecue-food-butcher_179666-43725.jpg?w=2000"""
    if len(url) > 1:
        bot.send_photo(message.chat.id, url,instructions_res)


# Starting the bot

bot.polling(none_stop=True, interval=3)
