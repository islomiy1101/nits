from django.db import models
from django.contrib.auth.models import User,auth

import datetime
class Branch(models.Model):
    name=models.CharField(max_length=100,verbose_name='Branch`s name')
    address=models.CharField(max_length=250,blank=True,null=True,verbose_name='Address')
    contact_number=models.CharField(max_length=100,blank=True,null=True,verbose_name='Contact Number')
    def __str__(self):
        return self.name
        verbose_name='Filial'
        verbose_name_plural='Filiallar'
        
class Teacher(models.Model):
    Branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    date=models.DateField()
    wdate=models.DateField()
    phone=models.CharField(max_length=50)
    skills=models.CharField(max_length=250)
    passport_seria=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    inn=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    inps=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    diplom=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    turdavoy=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    obyektivka=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.fullname
class Course(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name='Filial')
    name=models.CharField(max_length=200,verbose_name='Course')
    course_time=models.DateField()
    teacher=models.ManyToManyField(Teacher)
    payment=models.IntegerField()
    def __str__(self):
        return self.name
        verbose_name='Kurs'
        verbose_name_plural='Kurslar'

class Sector(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class MFY(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    sector=models.ForeignKey(Sector,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course_Part(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    surname=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=50)
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    mfy=models.ForeignKey(MFY,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    number_group=models.CharField(max_length=50)
    startdate=models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=100)
    tolov=models.CharField(max_length=10,null=True,blank=True)
    social_state=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Ro`yxatga olish'
        verbose_name_plural='Ro`yxatdan O`tganlar'

