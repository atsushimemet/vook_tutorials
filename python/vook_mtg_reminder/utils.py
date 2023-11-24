import requests
from config import slack_token
from datetime import datetime, timedelta


# 第一土曜日と第三土曜日の日付を計算する関数
def calculate_saturdays(year, month):
    """
    指定された年と月における第一土曜日と第三土曜日の日付を計算する関数

    :param year: 計算する年
    :param month: 計算する月
    :return: 第一土曜日と第三土曜日の日付（datetimeオブジェクト）
    """
    # 月の最初の日を取得
    first_day_of_month = datetime(year, month, 1)

    # 最初の土曜日までの日数を計算
    days_until_first_saturday = (5 - first_day_of_month.weekday() + 7) % 7

    # 第一土曜日の日付を計算
    first_saturday = first_day_of_month + timedelta(
        days=days_until_first_saturday
    )  # noqa

    # 第三土曜日の日付を計算（第一土曜日からさらに14日後）
    third_saturday = first_saturday + timedelta(days=14)

    return first_saturday, third_saturday


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
