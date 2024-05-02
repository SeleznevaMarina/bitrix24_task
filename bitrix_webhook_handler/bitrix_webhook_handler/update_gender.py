import psycopg2
from flask import Flask
from flask import request
from pybitrix import PyBitrix

app = Flask(__name__)

@app.route('/out_webhook_url', methods=['POST'])
def outwebhook():
    request_data = request.form
    request_data = request_data.json()
    handle_contact_change(request_data)
    return 'OK'

def execute_query(query):
    connection = psycopg2.connect(
        dbname="test_bitrix",
        user="marina",
        password="123",
        host="localhost"
        )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def update_contact_gender(contact_id, gender):
    webhook = "https://test123"
    bx24 = PyBitrix(inbound_hook=webhook)

    contact_data = {
        "ID": contact_id,
        "fields": {
            "UF_CRM_1611234567": gender
            },
        }

    response = bx24.call('crm.contact.update', contact_data)


def handle_contact_change(request_data):
    # Получаем данные контакта из Битрикс
    if request_data:
        contact_id = request_data["data"]["FIELDS"]["ID"]
        contact_name = request_data["data"]["FIELDS"]["NAME"]
        # Подключаемся к бд
        try:
            result_woman = execute_query(f"SELECT * FROM names_woman WHERE name = '{contact_name}'")
            if result_woman:
                gender = 'Женщина'
            else:
                result_man = execute_query(f"SELECT * FROM names_man WHERE name = '{contact_name}'")
                if result_man:
                    gender = 'Мужчина'
                else:
                    gender = 'Не удалось определить пол'
            
            update_contact_gender(contact_id, gender)

        except psycopg2.Error as e:
            print("Ошибка при работе с базой данных PostgreSQL:", e)
    else:
        print("Ошибка: не удалось получить данные контакта из Битрикс24")
