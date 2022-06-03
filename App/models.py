from django.db import models


# Create your models here.


class StudentInfo(models.Model):
    number = models.CharField(max_length=11)
    name = models.CharField(max_length=6)
    pic_url = models.CharField(max_length=64)
    age = models.IntegerField(default=22)
    class_name = models.CharField(max_length=64, null=True, blank=True)
    class_id = models.IntegerField(default=0)


'''
↑↑↑ create table App_student_Info 自动生成bigint ID auto_increment
'''


################## Add Data  ##################
# StudentInfo.objects.create(number=20180210888,name='张三',pic_url='picture/20180210888张三')


class ClassInfo(models.Model):
    class_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=32)
    pic_url = models.CharField(max_length=64, null=True, blank=True)
    audio_url = models.CharField(max_length=64, null=True, blank=True)
    class_des = models.CharField(max_length=64, null=True, blank=True)
