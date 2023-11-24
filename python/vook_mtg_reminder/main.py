import datetime
import requests
from config import slack_token


# 第一土曜日と第三土曜日の日付を計算する関数
def calculate_saturdays(year, month):
    # ...
    return None


# Slackにリマインダーを設定する関数
def set_slack_reminder(date, message):
    url = "https://slack.com/api/reminders.add"
    headers = {
        "Authorization": f"Bearer {slack_token}",
        "Content-Type": "application/json",
    }
    data = {"text": message, "time": date, "user": "ユーザーID"}
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def main():
    # 実行
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    first_saturday, third_saturday = calculate_saturdays(
        current_year, current_month
    )  # noqa
    set_slack_reminder(first_saturday, "第一土曜日のアジェンダ募集")
    set_slack_reminder(third_saturday, "第三土曜日のアジェンダ募集")


if __name__ == "__main__":
    main()
