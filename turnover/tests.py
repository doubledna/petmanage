# from django.test import TestCase
import pytest
from .models import DailyTurnover


# Create your tests here.
# 测试日营业额功能
@pytest.mark.django_db
def test_daily_turnover() -> None:
    """插入日营业额信息测试"""
    dt = DailyTurnover.objects.get_or_create(daily="2022.09.02", turnover=1000)
    assert dt.daily == "2022.09.02"
    assert dt.turnover == 1000
