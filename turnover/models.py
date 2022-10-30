from django.db import models


# Create your models here.
class DailyTurnover(models.Model):
    """日营业额"""
    id = models.AutoField(primary_key=True)
    daily = models.DateField(verbose_name="日期")
    turnover = models.FloatField(verbose_name="营业额")

    def __str__(self):
        return "%s" % (self.daily,)

    class Meta:
        verbose_name = "日营业额"
        verbose_name_plural = "日营业额"


class MonthlyTurnover(models.Model):
    """月营业额"""
    id = models.AutoField(primary_key=True)
    monthly = models.CharField(max_length=12, verbose_name="月份")
    turnover = models.FloatField(verbose_name="营业额")

    def __str__(self):
        return "%s" % (self.monthly,)

    class Meta:
        verbose_name = "月营业额"
        verbose_name_plural = "月营业额"


class YearTurnover(models.Model):
    """年营业额"""
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=12, verbose_name="年份")
    turnover = models.FloatField(verbose_name="营业额")

    def __str__(self):
        return "%s" % (self.year,)

    class Meta:
        verbose_name = "年营业额"
        verbose_name_plural = "年营业额"


class TotalTurnover(models.Model):
    """总营业额"""
    id = models.AutoField(primary_key=True)
    turnover = models.FloatField(verbose_name="营业额")

    def __str__(self):
        return "%s" % (self.id,)

    class Meta:
        verbose_name = "总营业额"
        verbose_name_plural = "总营业额"
