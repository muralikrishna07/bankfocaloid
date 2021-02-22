from django.shortcuts import render,redirect
from profiles.forms import createprofileform,DepositAmountForm,WithdrawAmountForm,TransferAmountForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View,FormView,CreateView,DeleteView 
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.contrib.auth import logout
from django.http import HttpResponse
from profiles.models import createprofilemodel,accounInfoModel,Transferdetails
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
import random


# Create your views here.

class createProfileView(CreateView):
    form_class = createprofileform
    success_url = reverse_lazy('profilesuccess')
    template_name = 'profiles/profile.html'

    def get_initial(self):
        return {'user': self.request.user}


class updateProfileView(UpdateView):
    model=createprofilemodel
    fields = "__all__"
#     # form_class = createProfileForm
    success_url = reverse_lazy('userhome')
    template_name = "profiles/updateprofile.html"
    
class deleteProfile(DeleteView):
    model= User
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name="profiles/deleteprofile.html"

class ViewProfile(DetailView):
    model = createprofilemodel
    fields="__all__"
    success_url = reverse_lazy('userhome')
    template_name = "profiles/detail.html"

class ViewAccount(DetailView):

    model = accounInfoModel
    fields="__all__"
    success_url = reverse_lazy('userhome')
    template_name = "profiles/accountdetail.html"


class Balanceenq(DetailView):

    model = accounInfoModel
    fields="balace"
    success_url = reverse_lazy('userhome')
    template_name = "profiles/balance.html"

def SignOutView(request):
    logout(request)
    return redirect("login")



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password successfully updated!')
            auth.logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {
        'form': form
    })


# def deposit(request):s
#     form=DepositAmountForm()
#     context={}
#     context["form"]=form
#     if request.method=="POST":
#         form=DepositAmountForm(request.POST)
#         if form.is_valid():
#             mpin=form.cleaned_data.get("mpin")
#             amount=form.cleaned_data.get("amount")
            
#             try:
#                 object=accounInfoModel.objects.get(mpin=mpin)
                
#                 bal=object.balace+amount
                
#                 object.balace=bal
            
#                 object.save()

#             except Exception:
#                 context["form"] = form
#                 return render(request, "profiles/deposit.html", context)

#             form.save()


#             return redirect("userhome")
#         else:
#             context["form"]=form
#             return render(request, "profiles/deposit.html", context)

#     return render(request,"profiles/deposit.html",context)

class DepositView(View):
    model = Transferdetails
    template_name = "profiles/deposit.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form=DepositAmountForm()
        self.context["form"]=form
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form=DepositAmountForm(request.POST)
        self.context={}
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            try:
                object = accounInfoModel.objects.get(mpin=mpin)
                bal = object.balace + amount
                object.balace = bal
                object.save()
            except Exception:
                self.context["form"] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect("userhome")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

# def withdraw(request):
#     form=WithdrawAmountForm()
#     context={}
#     context["form"]=form
#     if request.method=="POST":
#         form=WithdrawAmountForm(request.POST)
#         if form.is_valid():
#             mpin=form.cleaned_data.get("mpin")
#             amount=form.cleaned_data.get("amount")
            
#             try:
#                 object=accounInfoModel.objects.get(mpin=mpin)
                
#                 bal=object.balace-amount
                
#                 object.balace=bal
            
#                 object.save()

#             except Exception:
#                 context["form"] = form
#                 return render(request, "profiles/withdraw.html", context)

#             form.save()


#             return redirect("userhome")
#         else:
#             context["form"]=form
#             return render(request, "profiles/withdraw.html", context)

#     return render(request,"profiles/withdraw.html",context)

class WithdrawView(View):
    model = Transferdetails
    template_name = "profiles/withdraw.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form=DepositAmountForm()
        self.context["form"]=form
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form=DepositAmountForm(request.POST)
        self.context={}
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            try:
                object = accounInfoModel.objects.get(mpin=mpin)
                bal = object.balace - amount
                object.balace = bal
                object.save()
            except Exception:
                self.context["form"] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect("userhome")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


def transfer(request):
    form=TransferAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TransferAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            accountnumber = form.cleaned_data.get("accountnumber")
            try:
                object=accounInfoModel.objects.get(mpin=mpin)
                object1=accounInfoModel.objects.get(accountNumber=accountnumber)
                bal=object.balace-amount
                bal1=object1.balace+amount
                object.balace=bal
                object1.balace=bal1
               
                object.save()
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "profiles/transfer.html", context)

            form.save()


            return redirect("userhome")
        else:
            context["form"]=form
            return render(request, "profiles/transfer.html", context)

    return render(request,"profiles/transfer.html",context)









def success(request):
    return HttpResponse("<h1>saved successfully</h1>")


def rGen():
    return int(random.randint(100000, 999999))


def randomGen1():   
    return int(random.uniform(1000,9999))


def generateaccno(request):
    
    try:
        curr_user = accounInfoModel.objects.get(username=request.user)
    except:
        curr_user = accounInfoModel()
        curr_user.accountNumber = rGen()
        curr_user.mpin = randomGen1()
        curr_user.balance = 1000
        curr_user.username = request.user
        curr_user.save()
    return render(request,'profiles/accountcreate.html',{"curr_user":curr_user})

def profileacc(request):
    return render(request,'profiles/create.html')





