from django.contrib import admin
from .models import DailyTurnover, MonthlyTurnover, YearTurnover, TotalTurnover


# Register your models here.
@admin.register(DailyTurnover)
class DailyTurnoverAdmin(admin.ModelAdmin):
    """
    日营业额
    """
    list_display = ("id", "daily", "turnover",)
    list_per_page = 50
    list_filter = ("daily",)
    search_fields = ("daily",)


@admin.register(MonthlyTurnover)
class MonthlyTurnoverAdmin(admin.ModelAdmin):
    """
    月营业额
    """
    list_display = ("id", "monthly", "turnover",)
    list_per_page = 50
    list_filter = ("monthly",)
    search_fields = ("monthly",)


@admin.register(YearTurnover)
class YearTurnoverAdmin(admin.ModelAdmin):
    """
    年营业额
    """
    list_display = ("id", "year", "turnover",)
    list_per_page = 50
    list_filter = ("year",)
    search_fields = ("year",)


@admin.register(TotalTurnover)
class TotalTurnoverAdmin(admin.ModelAdmin):
    """
    总营业额
    """
    list_display = ("id", "turnover",)
    list_per_page = 50
    list_filter = ("id",)
    search_fields = ("id",)
