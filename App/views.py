from django.core.serializers import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os, sys, re, json

# Create your views here.
from App.models import StudentInfo, ClassInfo


def index(request):
    return render(request, "index.html", )


# def student_list(request):
#     stu_list = []
#     query_list = StudentInfo.objects.all()  # QuerySet类型[obj,obj]
#     for obj in query_list:
#         print(model_to_dict(obj))
#         stu_list.append(model_to_dict(obj))
#     print(stu_list)
#
#     return render(request, "student_list.html", {"stu_list": stu_list})

def api_getData(request, cid):
    data = {}
    cInfo = ClassInfo.objects.get(id=cid)  # 1801班cid为2
    data.update(model_to_dict(cInfo))
    print(data)

    stu_dict = {}
    query_list = StudentInfo.objects.filter(class_id=cid - 1)  # QuerySet类型[obj,obj]
    for obj in query_list:
        print(model_to_dict(obj))
        stu_dict.update({obj.name: model_to_dict(obj)})
    # print(stu_list)
    data.update({"students": stu_dict})

    return JsonResponse(data)
    # request, "student_list.html", {"data": data})


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


def class_init(request):
    ClassInfo.objects.create(class_number=0, class_name="计科1800")
    ClassInfo.objects.create(class_number=1, class_name="计科1801")
    ClassInfo.objects.create(class_number=2, class_name="计科1802")
    ClassInfo.objects.create(class_number=3, class_name="计科1803")
    ClassInfo.objects.create(class_number=4, class_name="计科1804")
    ClassInfo.objects.create(class_number=5, class_name="计科1805")
    ClassInfo.objects.create(class_number=6, class_name="计科1806")
    ClassInfo.objects.create(class_number=7, class_name="计科1807")
    ClassInfo.objects.create(class_number=8, class_name="计科1808")
    ClassInfo.objects.create(class_number=9, class_name="计科1809")

    ClassInfo.objects.create(class_number=11, class_name="数据1801")
    ClassInfo.objects.create(class_number=12, class_name="数据1802")
    ClassInfo.objects.create(class_number=13, class_name="数据1803")

    ClassInfo.objects.create(class_number=21, class_name="物网1801")
    ClassInfo.objects.create(class_number=22, class_name="物网1802")
    ClassInfo.objects.create(class_number=23, class_name="物网1803")

    ClassInfo.objects.create(class_number=31, class_name="自控1801")
    ClassInfo.objects.create(class_number=32, class_name="自控1802")
    ClassInfo.objects.create(class_number=33, class_name="自控1803")
    ClassInfo.objects.create(class_number=34, class_name="自控1804")

    ClassInfo.objects.create(class_number=41, class_name="软件1801")
    ClassInfo.objects.create(class_number=42, class_name="软件1802")
    ClassInfo.objects.create(class_number=43, class_name="软件1803")
    ClassInfo.objects.create(class_number=44, class_name="软件1804")
    ClassInfo.objects.create(class_number=45, class_name="软件1805")
    ClassInfo.objects.create(class_number=46, class_name="软件1806")

    ClassInfo.objects.create(class_number=51, class_name="信工1801")
    ClassInfo.objects.create(class_number=52, class_name="信工1802")
    ClassInfo.objects.create(class_number=53, class_name="信工1803")
    ClassInfo.objects.create(class_number=54, class_name="信工1804")

    ClassInfo.objects.create(class_number=61, class_name="计科专接本2001")
    ClassInfo.objects.create(class_number=62, class_name="计科专接本2002")
    ClassInfo.objects.create(class_number=63, class_name="计科专接本2003")
    ClassInfo.objects.create(class_number=64, class_name="计科专接本2004")
    ClassInfo.objects.create(class_number=65, class_name="计科专接本2005")
    ClassInfo.objects.create(class_number=66, class_name="计科专接本2006")

    return HttpResponse("全部班级已初始化")
