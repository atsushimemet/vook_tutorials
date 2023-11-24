# import pytest
from datetime import datetime
from utils import calculate_saturdays


def test_calculate_saturdays():
    # calculate_saturdays関数のテスト
    year = 2023
    month = 1  # 例えば2023年1月
    first_saturday, third_saturday = calculate_saturdays(year, month)
    assert first_saturday == datetime(2023, 1, 7)  # 2023年1月の第一土曜日
    assert third_saturday == datetime(2023, 1, 21)  # 2023年1月の第三土曜日


# def test_not_calculate_saturdays():
#     # calculate_saturdays関数のテスト
#     year = 2023
#     month = 1  # 例えば2023年1月
#     first_saturday, third_saturday = calculate_saturdays(year, month)
#     assert first_saturday != datetime(2023, 1, 6)  # 2023年1月の第一土曜日の一日前
#     assert third_saturday != datetime(2023, 1, 20)  # 2023年1月の第三土曜日の一日前


# @patch("requests.post")
# def test_set_slack_reminder(mock_post):
#     # set_slack_reminder関数のテスト
#     date = "2023-01-07T09:00:00Z"  # ISOフォーマットの日付
#     message = "テストリマインダー"
#     mock_post.return_value.json.return_value = {"ok": True, "reminder": {"id": "Rm123"}}

#     response = set_slack_reminder(date, message)
#     mock_post.assert_called_once()
#     assert response["ok"]
#     assert "reminder" in response
