from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,User,AuthenticationForm
from updatedbank.forms import RegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View,FormView,CreateView
from django.contrib.auth import authenticate,login
from profiles.models import createprofilemodel

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'updatebank/signup.html'

class LoginView(View):
    def get(self, request):
        return render(request, 'updatebank/login.html', { 'form':  AuthenticationForm })
    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is None:
                return render(
                    request,
                    'updatebank/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'updatebank/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)
            return redirect(reverse_lazy('userhome'))

        return render(
                    request,
                    'updatebank/login.html',
                    { 'form': form, 'invalid_creds': True }
                )




class HomeView(View):
    template_name = 'updatebank/userhome.html'
    def get(self, request):
        context={}
        try:
            uid= createprofilemodel.objects.get(user=request.user).id
            print(uid,type(uid))
        except:
            uid=None
        context = {'uid': uid}
        return render(request, 'updatebank/userhome.html', context)


# class login(FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('userhome')
#     template_name = 'updatebank/login.html'


# def userhome(request):
#     return render(request,'updatebank/userhome.html')




def home(request):
    return render(request,'updatebank/home.html')


# def login(request):
#     return render(request,'updatebank/login.html')