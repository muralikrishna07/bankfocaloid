from django.urls import path
from profiles import views

from profiles.views import createProfileView,success,WithdrawView,transfer,updateProfileView,DepositView,deleteProfile,SignOutView,Balanceenq,ViewAccount,ViewProfile,change_password,generateaccno,profileacc



urlpatterns = [
    path('createprofile/', createProfileView.as_view(), name='createprofile'),
    path("updateprofile/<int:pk>/", updateProfileView.as_view(), name="updateprofile"),
    path('viewprofile/',success,name='success'),
    path("deleteprofile/<int:pk>/",deleteProfile.as_view(),name="deleteprofile"),
    path("detailprofile/<int:pk>/",ViewProfile.as_view(),name='detailprofile'),
    path("accountdetail/<int:pk>/",ViewAccount.as_view(),name='accountdetail'),
    path('signout/',SignOutView,name="signout"),
    path('change_password/', views.change_password, name='change_password'),
    path('generateaccno/',generateaccno,name='generateaccno'),
    path('profilesuccess/',profileacc,name='profilesuccess'),
    path("balance/<int:pk>/",Balanceenq.as_view(),name='balance'),
    path("deposit/",DepositView.as_view(),name='deposit'),
    path("wirthdraw/",WithdrawView.as_view(),name='withdraw'),
    path("transfer/",transfer,name='transfer')

]