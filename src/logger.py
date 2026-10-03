from datetime import datetime


def log_success(message):
    with open("logs/success.log", "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}] {message}\n"
        )


def log_failed(message):
    with open("logs/failed.log", "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}] {message}\n"
        )