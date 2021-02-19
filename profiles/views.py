from django.shortcuts import render,redirect
from profiles.forms import createprofileform
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View,FormView,CreateView,DeleteView 
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.contrib.auth import logout
from django.http import HttpResponse
from profiles.models import createprofilemodel
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth


# Create your views here.

class createProfileView(CreateView):
    form_class = createprofileform
    success_url = reverse_lazy('userhome')
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

def SignOutView(request):
    logout(request)
    return redirect("login")



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            auth.logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {
        'form': form
    })



def success(request):
    return HttpResponse("<h1>saved successfully</h1>")