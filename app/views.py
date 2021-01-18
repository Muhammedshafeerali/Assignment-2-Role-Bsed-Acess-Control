
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required

from django.contrib.auth.models import Group,Permission
from .decorators import uauthenticateduser
from django.contrib.auth.models import  ContentType
from .models import  *



@uauthenticateduser
def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user:
            auth_login(request, user)

            if user.has_perm('app.prime_member'):
                print("workingjkjkjlkk")
            else:
                print("not working")
        
    
            return redirect(home)
        else:
            messages.info(request,'invalid credention')

    
    return render(request,'login.html')

@uauthenticateduser
def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
        return redirect(login)

    return render(request,'register.html')


@login_required(login_url='/')
def home(request):

    return render(request,'home.html')



@login_required(login_url='/')
def profile(request):
    return render(request,'profile.html')


@login_required(login_url='/')
def schedule(request,value):
    
    return render(request,'schedule.html',{'value':value})



@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect(login)


@login_required(login_url='/')
@permission_required('app.can_view_app_usage',raise_exception=True)
def appusage(request):
    
    return render(request,'app_usage.html')

@login_required(login_url='/')
@permission_required('app.can_view_revenue',raise_exception=True)
def apprevenue(request):
    
    return render(request,'app_revenue.html')

@login_required(login_url='/')
@permission_required('auth.view_user', raise_exception=True)
def users(request):

    users=User.objects.filter(is_staff=False)
    print(users)
    
    return render(request,'user.html',{'users':users})





@login_required(login_url='/')
@permission_required('auth.add_user',raise_exception=True)
def adduser(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
        return redirect(users)
    return render(request,'adduser.html')



@login_required(login_url='/')
@permission_required('auth.change_user',raise_exception=True)
def edituser(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.save()
        return redirect(users)



    return render(request,'edituser.html',{'user':user})


@login_required(login_url='/')
@permission_required('app.view_supportteam',raise_exception=True)
def staff(request):
    staffs=User.objects.filter(is_staff=True,is_superuser=False)

    return render(request,'staff.html',{'staffs':staffs})


@login_required(login_url='/')
@permission_required('auth.add_supportteam',raise_exception=True)
def addstaff(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        staff=User.objects.create_user(username=name,email=email,password=password,is_staff=True)
        staff.save()
        content_type=ContentType.objects.get_for_model(User)
        permission=Permission.objects.filter(content_type=content_type)
        staff.user_permissions.set(permission)
        return redirect('staff')
    return render(request,'addstaff.html')

@login_required(login_url='/')
@permission_required('app.delete_user',raise_exception=True)
def deleteuser(request,id): 
    User.objects.filter(id=id).delete()
    return redirect(users)

@login_required(login_url='/')
@permission_required('app.delete_supprtteam',raise_exception=True)
def deletestaff(request,id): 
    User.objects.filter(id=id).delete()
    return redirect(users)


@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect(login)


@login_required(login_url='/')
@permission_required('app.add_permission',raise_exception=True)
def addpermission(request,id):
    staff=User.objects.get(id=id)
    
    content_type = ContentType.objects.get_for_model(Superadmin)
    permissions=Permission.objects.filter(user=staff)
    print("staff permission",permissions)
    auth_user_model_ct=ContentType.objects.get_for_model(User)
    auth_user_model_all_perm=Permission.objects.filter(content_type__in=[auth_user_model_ct])
    superadmin_model_perm=Permission.objects.filter(codename__in=['can_view_revenue','can_view_app_usage'])
   
    permission_list=[]
   
    for auth_user_model_perm in auth_user_model_all_perm:
        if staff.has_perm('auth.' + auth_user_model_perm.codename) is not True:
           permission_list.append(auth_user_model_perm)
    for superadmin_perm in superadmin_model_perm:
        if staff.has_perm('app.'+superadmin_perm.codename) is not True:
            permission_list.append(superadmin_perm)



            

    if request.method=='POST':
        codename=request.POST['permission']
        
        permision=Permission.objects.get(
            codename=codename
        )
    
        staff.user_permissions.add(permision)
        return redirect(addpermission,id=id)
    
    
       
    

    return render(request,'addpermission.html',{'user':staff,'permissions':permissions,'permission_list':permission_list})



def removepermission(request,userid,permid):
    user=User.objects.get(id=userid)
    permission=Permission.objects.get(id=permid)
    print(permission)
    user.user_permissions.remove(permission)
    user.save()
    return redirect(addpermission,id=userid)
