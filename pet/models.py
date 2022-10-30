from django.db import models


# Create your models here.
# class PetMasterInfo(models.Model):
#     """宠物主信息"""
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=32, verbose_name="姓名")
#     phone = models.CharField(unique=True, max_length=128, verbose_name="电话号码")
#     address = models.CharField(unique=True, max_length=512, verbose_name="家庭住址")
#
#     def __str__(self):
#         return "%s" % (self.name,)
#
#     class Meta:
#         verbose_name = "宠物主信息"
#         verbose_name_plural = "宠物主信息"
#
#
# class PetInfo(models.Model):
#     """宠物信息"""
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=32, verbose_name="宠物名")
#     master = models.ForeignKey(PetMasterInfo, verbose_name="宠物主", on_delete=models.CASCADE, related_name="pet_master")
#
#     def __str__(self):
#         return "%s" % (self.name,)
#
#     class Meta:
#         verbose_name = "宠物信息"
#         verbose_name_plural = "宠物信息"


class Staff(models.Model):
    """员工信息"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(max_length=16, verbose_name="性别")
    phone = models.CharField(unique=True, max_length=128, verbose_name="电话号码")
    address = models.CharField(max_length=512, verbose_name="家庭住址")
    home_town = models.CharField(max_length=128, verbose_name="籍贯")
    id_number = models.CharField(max_length=64, verbose_name="身份证号")

    def __str__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = "员工信息"


class PetOwner(models.Model):
    """宠物主信息"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(max_length=16, verbose_name="性别")
    phone = models.CharField(unique=True, max_length=128, verbose_name="电话号码")
    address = models.CharField(max_length=512, verbose_name="家庭住址")

    def __str__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = "宠物主信息"
        verbose_name_plural = "宠物主信息"


class Pet(models.Model):
    """宠物信息"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字")
    age = models.IntegerField(verbose_name="年龄")
    species = models.CharField(max_length=16, verbose_name="物种")
    owner = models.ForeignKey(PetOwner, verbose_name="宠物主", on_delete=models.CASCADE, related_name="pet_owner")
    deposit_start_time = models.DateTimeField(auto_now=True, verbose_name="寄存开始时间")
    deposit_end_time = models.DateTimeField(verbose_name="寄存结束时间", blank=True, null=True)
    receive_staff = models.ForeignKey(Staff, verbose_name="接收员工", on_delete=models.CASCADE, related_name="pet_staff", default=None)

    def __str__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = "宠物信息"
        verbose_name_plural = "宠物信息"


class Order(models.Model):
    """订单"""
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=64, unique=True, verbose_name="订单号")
    pet = models.ForeignKey(Pet, verbose_name="消费宠物", on_delete=models.CASCADE, related_name="pet_order")
    staff = models.ForeignKey(Staff, verbose_name="操作员工", on_delete=models.CASCADE, related_name="staff_order")
    amount = models.FloatField(verbose_name="费用", default=0.0)
    description = models.TextField(verbose_name="记录", default="-")
    create_time = models.DateTimeField(auto_now=True, verbose_name="订单生成时间")

    def __str__(self):
        return "%s" % (self.order_id,)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"


class Assets(models.Model):
    """资产"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="资产名称")
    purchase_date = models.DateTimeField(verbose_name="进货时间")
    staff = models.ForeignKey(Staff, verbose_name="操作员工", on_delete=models.CASCADE, related_name="staff_assets")
    amount = models.FloatField(verbose_name="单价", default=0)
    quantity = models.FloatField(verbose_name="数量", default=0)
    description = models.TextField(verbose_name="资产描述", default="-")

    def __str__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = "资产"
        verbose_name_plural = "资产"
