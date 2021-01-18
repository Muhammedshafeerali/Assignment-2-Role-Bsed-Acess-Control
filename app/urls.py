from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name="profile"),
    path('schedule/<str:value>/',views.schedule,name="schedule"),
    path('logout/',views.logout,name='logout'),
    path('users/',views.users,name='users'),
    path('staff/',views.staff,name='staff'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('adduser/',views.adduser,name='adduser'),
    path('edituser/<int:id>/',views.edituser,name='edituser'),
    path('deleteuser/<int:id>/',views.deleteuser,name='deleteuser'),
    path('deletestaff/<int:id>/',views.deletestaff,name='deletestaff'),
    path('addpermission/<int:id>/',views.addpermission,name='addpermission'),
    path('removepermissin/<int:userid>/<int:permid>/',views.removepermission,name='removepermission'),
    path('appusage',views.appusage,name="appusage"),
    path('apprevenue',views.apprevenue,name="apprevenue"),

]
