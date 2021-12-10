
from django.db.models.base import Model
from django.shortcuts import render, redirect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



# Create your views here.
# def add_stu(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         sex = request.POST.get('sex')
#         birthday = request.POST.get('birthday')

#         # 添加书籍记录，一对多
#         stu_obj = Student.objects.create(name=name, sex=sex, birthday=birthday)
        
#         return redirect('/tables')

#     students = Student.objects.all()
#     return render(request, 'home/addStudent.html', locals())



# '''删除操作'''
# @login_required(login_url="/login/")
# def delete_stu(request, delete_stu_id):
#     Student.objects.filter(id=delete_stu_id).delete()
#     students = Student.objects.all()
#     return render(request, 'home/tables.html', locals())



# '''编辑操作'''
# def change_stu(request, edit_stu_id):
#     stu_obj = Student.objects.filter(id=edit_stu_id).first()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         sex = request.POST.get('sex')
#         birthday = request.POST.get('birthday')

#         # 更新书籍记录
#         Student.objects.filter(id=edit_stu_id).update(name=name, sex=sex, birthday=birthday)
#         return redirect('/tables')

#     return render(request, 'home/editStudent.html', locals())



'''展示数据表'''
@login_required(login_url="/login/")
def show_bags(request):
    data = Bag._meta.fields
    columns = [data[i].name for i in range(len(data))]
    objs = Bag.objects.all()
    return render(request, 'home/bags_table.html', locals())


@login_required(login_url="/login/")
def show_bags(request):
    data = Bag._meta.fields
    columns = [data[i].name for i in range(len(data))]
    objs = Bag.objects.all()
    return render(request, 'home/bags_table.html', locals())


@login_required(login_url="/login/")
def show_designers(request):
    data = Designer._meta.fields
    columns = [data[i].name for i in range(len(data))]
    objs = Designer.objects.all()
    return render(request, 'home/designers_table.html', locals())


@login_required(login_url="/login/")
def show_customers(request):
    data = Customer._meta.fields
    columns = [data[i].name for i in range(len(data))]
    objs = Customer.objects.all()
    return render(request, 'home/customers_table.html', locals())


@login_required(login_url="/login/")
def show_rentals(request):
    data = Rentals._meta.fields
    columns = [data[i].name for i in range(len(data))]
    objs = Rentals.objects.all()
    return render(request, 'home/rentals_table.html', locals())


'''分页'''
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        # students = models.Student.objects.all()
        # if load_template == 'tables':
        #     return render(request, 'home/tables.html', locals())

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
