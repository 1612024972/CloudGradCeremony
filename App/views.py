from django.core.serializers import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
import sys
import re
import json

# Create your views here.
from App.models import StudentInfo, ClassInfo


def index(request):
    return render(request, "index.html")


def turn_the_tassel(request):
    return render(request, "turn_the_tassel.html")

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

    stu_list = []
    query_list = StudentInfo.objects.filter(
        class_id=cid)  # QuerySet类型[obj,obj]
    for obj in query_list:
        print(model_to_dict(obj))
        stu_list.append(model_to_dict(obj))
    # print(stu_list)
    data.update({"students": stu_list})

    return JsonResponse(data)
    # request, "student_list.html", {"data": data})


def student_add(request):
    # class_init()
    COOKED_FOLDER = 'App/static/picture/student_pic/'  # 文件夹的地址
    # 获取目录下所有班级文件夹
    dir_list = os.listdir(COOKED_FOLDER)
    # print(dir_list)
    # 处理每个班级文件夹
    for class_name in dir_list:
        # 创建班级数据
        pic_url = "picture/class_pic/"+class_name+".webp"
        audio_url = "audios/"+class_name+".m4a"
        ClassInfo.objects.create(
            class_name=class_name, pic_url=pic_url, audio_url=audio_url)
        # [20XXXXXXXXX张三,16XXXXX-李四]
        stu_pics_names = os.listdir(COOKED_FOLDER + class_name)
        for f in stu_pics_names:
            stu_num = re.findall('\d+', f)[0]
            stu_name = re.findall('[\u4e00-\u9fa5]+', f)[0]
            stu_url = 'picture/student_pic/' + class_name+'/'+f
            stu_cid = ClassInfo.objects.get(class_name=class_name).id
            StudentInfo.objects.create(
                number=stu_num, name=stu_name, pic_url=stu_url, class_name=class_name, class_id=stu_cid)

    # 通过文件名获得学生对象
    # for f in stu_pics:
    #     # print(re.split('\+|-|\s+|_|\.', f[11:]))
    #     f_list = re.split('\+|-|\s+|_|\.', f[11:])
    #     stu_num = f[:11]
    #     if f_list[0] != '':
    #         stu_name = f_list[0]
    #     else:
    #         stu_name = f_list[1]
    #     stu_url = 'picture/student_pic/' + f
    #     StudentInfo.objects.create(number=stu_num, name=stu_name, pic_url=stu_url)
    #
    # StudentInfo.objects.filter(class_id=1).update(class_name="计科1800")

    return HttpResponse("学生添加完毕")


def student_delete_all(request):
    StudentInfo.objects.all().delete()
    return HttpResponse("所有学生已删除")


def student_class(request):
    StudentInfo.objects.filter(class_id=1).update(class_name="计科1800")

# def class_init():
# ClassInfo.objects.create(class_number=0, class_name="计科1800")
# ClassInfo.objects.create(class_number=1, class_name="计科1801")
# ClassInfo.objects.create(class_number=2, class_name="计科1802")
# ClassInfo.objects.create(class_number=3, class_name="计科1803")
# ClassInfo.objects.create(class_number=4, class_name="计科1804")
# ClassInfo.objects.create(class_number=5, class_name="计科1805")
# ClassInfo.objects.create(class_number=6, class_name="计科1806")
# ClassInfo.objects.create(class_number=7, class_name="计科1807")
# ClassInfo.objects.create(class_number=8, class_name="计科1808")
# ClassInfo.objects.create(class_number=9, class_name="计科1809")
#
# ClassInfo.objects.create(class_number=11, class_name="数据1801")
# ClassInfo.objects.create(class_number=12, class_name="数据1802")
# ClassInfo.objects.create(class_number=13, class_name="数据1803")
#
# ClassInfo.objects.create(class_number=21, class_name="物网1801")
# ClassInfo.objects.create(class_number=22, class_name="物网1802")
# ClassInfo.objects.create(class_number=23, class_name="物网1803")
#
# ClassInfo.objects.create(class_number=31, class_name="自控1801")
# ClassInfo.objects.create(class_number=32, class_name="自控1802")
# ClassInfo.objects.create(class_number=33, class_name="自控1803")
# ClassInfo.objects.create(class_number=34, class_name="自控1804")
#
# ClassInfo.objects.create(class_number=41, class_name="软件1801")
# ClassInfo.objects.create(class_number=42, class_name="软件1802")
# ClassInfo.objects.create(class_number=43, class_name="软件1803")
# ClassInfo.objects.create(class_number=44, class_name="软件1804")
# ClassInfo.objects.create(class_number=45, class_name="软件1805")
# ClassInfo.objects.create(class_number=46, class_name="软件1806")
#
# ClassInfo.objects.create(class_number=51, class_name="信工1801")
# ClassInfo.objects.create(class_number=52, class_name="信工1802")
# ClassInfo.objects.create(class_number=53, class_name="信工1803")
# ClassInfo.objects.create(class_number=54, class_name="信工1804")
#
# ClassInfo.objects.create(class_number=61, class_name="计科专接本2001")
# ClassInfo.objects.create(class_number=62, class_name="计科专接本2002")
# ClassInfo.objects.create(class_number=63, class_name="计科专接本2003")
# ClassInfo.objects.create(class_number=64, class_name="计科专接本2004")
# ClassInfo.objects.create(class_number=65, class_name="计科专接本2005")
# ClassInfo.objects.create(class_number=66, class_name="计科专接本2006")
