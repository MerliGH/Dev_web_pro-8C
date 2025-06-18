from django.contrib import admin

# Register your models here.
from core import models


@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [
        "bank_name",
        "address",
        "status"
    ]


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "currency_name",
        "short_name",
        "status"
    ]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "account_name",
        "currency",
        "status"
    ]



@admin.register(models.CategoryProvider)
class CategoryProviderAdmin(admin.ModelAdmin):
    list_display = [
        "category_name",
        "status"
    ]


@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = [
        "provider_name",
        "category",
        "status"
    ]


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "payment_name",
        "provider",
        "account",
        "timestamp",
        "status"
    ]