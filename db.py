import sqlite3 as sql

recipe_list = [(1,2,'fish','fry')]
db_name = 'telebot.db';
table_name = "all_recipes";
id_dish = 0;
category_dish = 1;
dish_name = 2;
instructions = 3;

def create_db():
    with sql.connect('telebot.db') as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS all_recipes(
            id_dish INTEGER PRIMARY KEY,
            category_dish INTEGER,
            dish_name TEXT,
            instructions TEXT
        );
        """)
        db.commit()
        # db.close()

def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sql.connect('telebot.db')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO all_recipes
                          (id_dish, category_dish, dish_name, instructions) 
                          VALUES (?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into all_recipes table")
        sqliteConnection.commit()
        cursor.close()

    except sql.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

def getMealById(id):
    try:
        sqliteConnection = sql.connect(db_name)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sql_select_query = f"""select * from {table_name} where category_dish = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        result = "";
        for row in records:
            # s = """
            # I will %s there
            # I will go %s
            # %s
            # """ % (string1, string2, string3)
            # print(s)
            result = result + """
ID = %s
category_dish = %s
dish_name = %s
instructions  = %s
""" % (row[id_dish], row[category_dish],
                            row[dish_name],row[instructions])

            # print("ID = ", row[id_dish])
            # print("category_dish = ", row[category_dish])
            # print("dish_name = ", row[dish_name])
            # print("instructions  = ", row[instructions])
        cursor.close()
        return result

    except sql.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

# create_db();

# recordsToInsert = [(1, 1, 'meat', 'take meal and prepare it'),
#                    (2, 2, 'fish', 'catch fish first'),
#                    (3, 2, 'fish', 'you will understand speech of birds if eat that fish')]
#
# insertMultipleRecords(recordsToInsert)

# select_item(1)

print(getMealById(2))