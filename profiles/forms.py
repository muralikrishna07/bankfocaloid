from django.forms import ModelForm
from django import forms
from profiles.models import createprofilemodel,Transferdetails,accounInfoModel

class createprofileform(ModelForm):
    #user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = createprofilemodel
        fields = '__all__'
        widgets={"user":forms.HiddenInput(),}




class DepositAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields=["amount","mpin"]

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        amount=cleaned_data.get("amount")
        print(mpin,",",amount)
        try:
            object=accounInfoModel.objects.get(mpin=mpin)
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)


class WithdrawAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields=["amount","mpin"]

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        amount=cleaned_data.get("amount")
        print(mpin,",",amount)
        try:
            object=accounInfoModel.objects.get(mpin=mpin)
            if(object):
                if(object.balace<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                    pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)



class TransferAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields=["mpin","accountnumber","amount"]
        widgets={"user":forms.HiddenInput(),}


    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accountnumber=cleaned_data.get("accountnumber")
        amount=cleaned_data.get("amount")
        print(mpin,",",accountnumber,",",amount)
        try:
            object=accounInfoModel.objects.get(mpin=mpin)
            if(object):

        # for checking sufficent balance
                if(object.balace<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)
        # for account validation
        try:
            object=accounInfoModel.objects.get(accountNumber=accountnumber)
            if(object):
                pass
        except:
            msg="you have provided invalid accno"
            self.add_error("accountnumber",msg)