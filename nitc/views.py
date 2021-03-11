from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Course,Branch,Register,MFY,Course_Part,Teacher
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime
import time

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def course(request):
    return render(request,'course.html')

def contact(request):
    return render(request,'contact.html')

def manager(request):
    country_cod = '+998'
    branch=Branch.objects.all()
    course=Course.objects.all()
    teacher=Teacher.objects.all()
    mfy=MFY.objects.all()
    context={'course':course,'data':branch,'teacher':teacher,'mfy':mfy}
    if request.method=='POST':
        fname=request.POST['fname']#w
        lname=request.POST['lname']#w
        sname=request.POST['sname']#w
        passport=request.POST['passport']#w
        cnumber=request.POST['phone']#w
        bdate=request.POST['bdate']#w
        gender=request.POST['gender']#w
        branch=request.POST['branch']#w
        mfy=request.POST['mfy']#w
        course=request.POST['course']#w
        teacher=request.POST['teacher']
        group=request.POST['group']
        payment=request.POST['tolov']
        social_statement=request.POST['social_statement']
        sdate=request.POST['sdate']
        subject=request.POST['subject']
        mobnumber = country_cod + cnumber
        usr=User.objects.create_user(passport,password=cnumber)
        usr.username=passport
        usr.first_name=fname
        usr.last_name=lname
        usr.save()
        reg=Register(user=usr,contact_number=mobnumber,branch = Branch.objects.get(id=branch),
        course=Course.objects.get(id=course),number_group=group,gender=gender,surname=sname,birth_date=bdate,
        mfy=MFY.objects.get(id=mfy),teacher=Teacher.objects.get(id=teacher),tolov=payment,social_state=social_statement,startdate=sdate,subject=subject)
        reg.save()
        return render(request, 'index.html',
                      {'status': 'Tabriklaymiz! Hurmatli , {} Siz ro`yxatdan muvaffaqiyatli o`tdingiz'.format(fname)})
    return render(request,'manager-panel.html',context)

def check_user(request):
        if request.method == 'GET':
          un = request.GET['usern'].capitalize()
          print(un)
          check = User.objects.filter(username=un)
          if len(check) == 1:
            return HttpResponse('Exists')
          else:
            return HttpResponse('No exists')



def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                res = HttpResponseRedirect('/')
                if 'rememberme' in request.POST:
                    res.set_cookie('user__id', user.id)
                    res.set_cookie('date_login', datetime.datetime.now())
                return res

        else:
            return render(request, 'index.html', {'status': 'Foydaluvchi nomi yoki paroli xato'})

    return HttpResponse('called')

@login_required
def user_logout(request):
    logout(request)
    res = HttpResponseRedirect('/')
    res.delete_cookie('user_id')
    res.delete_cookie('date_login')
    return res
def livechat(request):
    return render(request,'livechat.html')


def register(request):
    country_cod = '+998'
    course=Course.objects.all()
    branch=Branch.objects.all()
    context={'data':course,'branch':branch}
    if request.method=='POST':
        fname=request.POST['fname']#w
        lname=request.POST['lname']#w
        sname=request.POST['sname']#w
        username=request.POST['uname']#w
        email=request.POST['email']#w
        password1=request.POST['password1']#w
        cnumber=request.POST['cnumber']#w
        branch=request.POST['branch']#w
        course=request.POST['course']#w
        course_days=request.POST['edate']#w
        course_time_type=request.POST['cdate']#w
        mobnumber = country_cod + cnumber
        fullname=lname+' '+sname

        usr=User.objects.create_user(username,email,password1)
        usr.username=username
        usr.first_name=fname
        usr.last_name=fullname
        usr.save()
        reg=Register(user=usr,contact_number=mobnumber,branch = Branch.objects.get(id=branch),
        course=Course.objects.get(id=course),course_days=course_days,course_time_type=course_time_type,
        number_group=Course_Part.objects.get(id=1))
        reg.save()
        return render(request, 'register.html',
                      {'status': 'Tabriklaymiz! Hurmatli , {} Siz ro`yxatdan muvaffaqiyatli o`tdingiz'.format(fullname)})
    return render(request,'register.html',context)
# def manager(request):
#     course=Course.objects.all()
#     st=User.objects.all()
#     teacher=Teacher.objects.all()
#     mfy=MFY.objects.all()
#     context={'course':course,'student':st,'teacher':teacher,'mfy':mfy}
#     if request.method=='POST':
#         un=request.POST['uname']
#         student=Register.objects.get(user=User.objects.get(username=un))
#         context={'st':student,'course':course,'student':st,'teacher':teacher,'mfy':mfy}
#     return render(request,'manager-panel.html',context)
