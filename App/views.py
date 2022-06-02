from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
import os, sys, re

# Create your views here.
from App.models import StudentInfo


def index(request):
    return render(request, "index.html", )


def student_list(request):
    stu_list = []
    query_list = StudentInfo.objects.all()  # QuerySet类型[obj,obj]
    for obj in query_list:
        print(model_to_dict(obj))
        stu_list.append(model_to_dict(obj))
    print(stu_list)

    return render(request, "student_list.html", {"stu_list": stu_list})


def student_add(request):
    COOKED_FOLDER = 'App/static/picture/student_pic/'  # 文件夹的地址
    # 获取目录下所有文件
    stu_pics = os.listdir(COOKED_FOLDER)

    # 通过文件名获得学生对象
    for f in stu_pics:
        # print(re.split('\+|-|\s+|_|\.', f[11:]))
        f_list = re.split('\+|-|\s+|_|\.', f[11:])
        t_num = f[:11]
        if f_list[0] != '':
            t_name = f_list[0]
        else:
            t_name = f_list[1]
        t_url = 'picture/student_pic/' + f
        StudentInfo.objects.create(number=t_num, name=t_name, pic_url=t_url)

    StudentInfo.objects.filter(class_id=1).update(class_name="计科1800")

    return HttpResponse("学生添加完毕")


def student_delete_all(request):
    StudentInfo.objects.all().delete()
    return HttpResponse("所有学生已删除")


def student_class(request):
    StudentInfo.objects.filter(class_id=1).update(class_name="计科1800")
