from django import forms


from core import models


class CreateBankForm(forms.ModelForm):
    class Meta:
        model = models.Bank
        fields = [
            "bank_name",
            "address",
            "status",
        ]
        widgets = {}



class UpdateBankForm(forms.ModelForm):
    class Meta:
        model = models.Bank
        fields = [
            "bank_name",
            "address",
            "status",
        ]
        widgets = {}