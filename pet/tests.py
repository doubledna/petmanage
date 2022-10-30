# from django.test import TestCase
import pytest
from pet.models import PetOwner, Pet, Staff, Order, Assets


# Create your tests here.
# 测试员工信息功能
@pytest.mark.django_db
def test_staff() -> None:
    """插入员工信息测试"""
    s = Staff.objects.get_or_create(name="员工C", age=20, gender="女", phone="00000000006", address="北京", home_town="北京", id_number="xxxxxxxxxxxxxxxxx")
    assert s.name == "员工C"
    """查询员工信息测试"""
    s = Staff.objects.get(name="员工C")
    assert s.name == "员工C"


# 测试宠物主信息功能
@pytest.mark.django_db
def test_pet_owner() -> None:
    """插入宠物主信息测试"""
    po = PetOwner.objects.get_or_create(name="王二", age=18, gender="女", phone="00000000003", address="北京")
    assert po.name == "王二"
    """查询宠物主信息测试"""
    po = PetOwner.objects.get(name="王二")
    assert po.name == "王二"


# 测试宠物信息功能
@pytest.mark.django_db
def test_pet() -> None:
    """插入宠物信息测试"""
    po = PetOwner.objects.get(name="王二")
    s = Staff.objects.get(name="员工C")
    p = Pet.objects.get_or_create(name="小毛", age=2, species="狗", owner=po, receive_staff=s,)
    assert p.name == "小毛"
    """查询宠物信息测试"""
    p = Pet.objects.get(name="小毛")
    assert p.name == "小毛"


# 测试订单信息功能
@pytest.mark.django_db
def test_order() -> None:
    """插入订单信息测试"""
    p = Pet.objects.get(name="小毛")
    s = Staff.objects.get(name="员工C")
    o = Order.objects.get_or_create(order_id="000003", pet=p, staff=s, amount=50, description="驱虫")
    assert o.order_id == "000003"
    """查询订单信息测试"""
    o = Order.objects.get(order_id="000003")
    assert o.order_id == "000003"


# 测试资产信息功能
@pytest.mark.django_db
def test_assets() -> None:
    """插入资产信息测试"""
    s = Staff.objects.get(name="员工C")
    a = Assets.objects.get_or_create(name="狗粮", staff=s, amount=50, quantity="10", description="精品狗粮")
    assert a.name == "狗粮"
    a = Assets.objects.get(name="狗粮")
    assert a.name == "狗粮"
