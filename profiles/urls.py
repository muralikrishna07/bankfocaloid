from django.urls import path
from profiles import views

from profiles.views import createProfileView,success,updateProfileView,deleteProfile,SignOutView,ViewProfile,change_password




urlpatterns = [
    path('createprofile/', createProfileView.as_view(), name='createprofile'),
    path("updateprofile/<int:pk>/", updateProfileView.as_view(), name="updateprofile"),
    path('viewprofile/',success,name='success'),
    path("deleteprofile/<int:pk>/",deleteProfile.as_view(),name="deleteprofile"),
    path("detailprofile/<int:pk>/",ViewProfile.as_view(),name='detailprofile'),
    path('signout/',SignOutView,name="signout"),
    path('change_password/', views.change_password, name='change_password'),
]