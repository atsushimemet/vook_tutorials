import datetime
from utils import calculate_saturdays, set_slack_reminder


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
