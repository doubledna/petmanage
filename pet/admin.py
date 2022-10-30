from django.contrib import admin
from .models import PetOwner, Pet, Staff, Order, Assets

admin.site.site_header = '宠物寄存管理系统'
admin.site.site_title = '宠物寄存管理系统'
admin.site.index_title = '宠物寄存管理系统'


# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    """
    员工信息
    """
    list_display = ("id", "name", "age", "gender", "phone", "address", "home_town", "id_number")
    list_per_page = 50
    list_filter = ("name",)
    search_fields = ("name", "phone")


@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    """
    宠物主信息
    """
    list_display = ("id", "name", "age", "gender", "phone", "address")
    list_per_page = 50
    list_filter = ("name",)
    search_fields = ("name", "phone")


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """
    宠物信息
    """
    list_display = ("id", "name", "age", "species", "owner", "receive_staff", "deposit_start_time", "deposit_end_time")
    list_per_page = 50
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    订单
    """
    list_display = ("id", "order_id", "create_time", "pet", "staff", "amount", "description")
    list_per_page = 50
    list_filter = ("order_id",)
    search_fields = ("order_id",)


@admin.register(Assets)
class AssetsAdmin(admin.ModelAdmin):
    """
    资产
    """
    list_display = ("id", "name", "purchase_date", "staff", "amount", "quantity", "description")
    list_per_page = 50
    list_filter = ("name",)
    search_fields = ("name",)

