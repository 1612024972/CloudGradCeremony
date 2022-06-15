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
    cInfo = ClassInfo.objects.get(id=cid)
    print(cInfo.class_name)
    print(type(cInfo.class_name))
    if re.findall('[\u4e00-\u9fa5]+', cInfo.class_name)[0]=="计科专接本":
        cInfo.class_name="计科"+re.findall('[\d]+', cInfo.class_name)[0]+"(专接本)"

    data.update(model_to_dict(cInfo))
    #print(data)

    stu_list = []
    id = 0
    query_list = StudentInfo.objects.filter(
        class_id=cid)  # QuerySet类型[obj,obj]
    for obj in query_list:
        id = id + 1
        obj.id = id
        print(model_to_dict(obj))
        stu_list.append(model_to_dict(obj))
    # print(stu_list)
    data.update({"students": stu_list})

    return JsonResponse(data)
    # request, "student_list.html", {"data": data})


def student_add(request):
    COOKED_FOLDER = 'App/static/picture/student_pic/'  # 文件夹的地址
    # 获取目录下所有班级文件夹
    # dir_list = os.listdir(COOKED_FOLDER)
    # print(dir_list)
    dir_list = ['计科1801', '计科1802', '计科1803', '计科1804', '计科1805', '计科1806', '计科1807', '计科1808',
                '计科1809',
                '软件1801', '软件1802','软件1803', '软件1804', '软件1805', '软件1806',
                '信工1801', '信工1802', '信工1803', '信工1804',
                '自控1801', '自控1802', '自控1803', '自控1804',
                '物网1801', '物网1802', '物网1803',
                '数据1801', '数据1802', '数据1803',
                '计科专接本2001', '计科专接本2002', '计科专接本2003', '计科专接本2004', '计科专接本2005', '计科专接本2006'
                ]

    # 处理每个班级文件夹
    for class_name in dir_list:
        # 创建班级数据
        pic_url = "picture/class_pic/" + class_name + ".jpg"
        audio_url = "audios/" + class_name + "音频.mp3"
        ClassInfo.objects.create(
            class_name=class_name, pic_url=pic_url, audio_url=audio_url)
        # [20XXXXXXXXX张三,16XXXXX-李四]
        # 创建学生数据
        stu_pics_names = os.listdir(COOKED_FOLDER + class_name)
        for f in stu_pics_names:
            stu_num = re.findall('\d+', f)[0]
            stu_name = re.findall('[\u4e00-\u9fa5]+', f)[0]
            stu_url = 'picture/student_pic/' + class_name + '/' + f
            stu_cid = ClassInfo.objects.get(class_name=class_name).id
            StudentInfo.objects.create(
                number=stu_num, name=stu_name, pic_url=stu_url, class_name=class_name, class_id=stu_cid)



    return HttpResponse("学生添加完毕")


def student_delete_all(request):
    StudentInfo.objects.all().delete()
    return HttpResponse("所有学生已删除")


def student_class(request):
    StudentInfo.objects.filter(class_id=1).update(class_name="计科1800")
