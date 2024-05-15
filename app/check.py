import requests
import json
import time

def check_payment_status():
    url = "https://mw-api-test.dengi.kg/api/json/json.php"
    payload = {
        "cmd": "statusPayment",
        "version": 1005,
        "sid": "6554503425",
        "mktime": "1714725452",
        "lang": "ru",
        "data": {
            "invoice_id": "169734632784",
            "order_id": "testpr1",
            "mark": 1
        },
        "hash": "e170d79ee7569fe29fa9057e2eb3e65e"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "payments" in data["data"]:
            payment = data["data"]["payments"][0]
            if payment["status"] == "approved":
                amount = int(payment["amount"]) / 100
                update_data(amount, payment["trans_id"])

def update_data(amount, trans_id):
    url = "https://mw-api-test.dengi.kg/api/json/json.php"
    payload = {
        "cmd": "updateMark",
        "version": 1005,
        "sid": "6554503425",
        "mktime": "1714726582",
        "lang": "ru",
        "data": {
            "trans_id": trans_id,
            "mark": None
        },
        "hash": "9c3863dd8aac4245608a0378d298f433"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        with open("data.txt", "a") as file:
            file.write(str(amount) + "\n")

while True:
    check_payment_status()
    time.sleep(5)
