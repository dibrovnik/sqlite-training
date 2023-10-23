import sqlite3

# Установка соединения с базой данных SQLite
conn = sqlite3.connect('trainings.db')
cursor = conn.cursor()

# Функция для создания таблицы для каждого пользователя
def create_user_table(user_id):
    table_name = f'user_{user_id}'
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_name TEXT,
            repetitions INTEGER,
            weight REAL,
            date DATE
        )
    ''')
    conn.commit()

# Функция для записи данных в таблицу пользователя
def add_training_data(user_id, exercise_name, repetitions, weight, date):
    table_name = f'user_{user_id}'
    cursor.execute(f'''
        INSERT INTO {table_name} (exercise_name, repetitions, weight, date)
        VALUES (?, ?, ?, ?)
    ''', (exercise_name, repetitions, weight, date))
    conn.commit()

# Пример использования функций
user_id = 123456789  # Идентификатор пользователя (может быть chat_id из Telegram)
create_user_table(user_id)
add_training_data(user_id, 'Squats', 10, 50.5, '2023-10-25')

# Закрытие соединения с базой данных
conn.close()
