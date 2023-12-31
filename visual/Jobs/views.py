from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Target_list,Job
from .form import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import time
from datetime import date
# Create your views here.
@login_required(login_url='/')
def main(request):
    return HttpResponse("This is Jobs")

@login_required(login_url='/')
def overview(request):
    return render(request,'overview.html')

@login_required(login_url='/')
def chart(request):
    return render(request,'chart.html')


@login_required(login_url='/')
def table(request):
    return render(request,'table.html')


@login_required(login_url='/')
def job_list(request):
    user = request.user
    job_list=Job.objects.filter(user_id=user.id)
    
    context = {'job_list':job_list}
    return  render(request, 'job_list.html', context)

@login_required(login_url='/')
def job_list_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user_id=request.user.id
            job.active_status = 1
            job.executed_date = date.today().isoformat()
            job.complited_date = '1990-01-01'
            job.save()
            print("success")
            return redirect(reverse('jobs:joblist'))
        else:
            print("fail")
    
    form = JobForm()
    context = {'form': form}        
    return render(request, 'form.html',context)

@login_required(login_url='/')
def job_list_update_form(request,id):
    instance = get_object_or_404(Job, pk=id)
    form = JobForm(instance=instance)
    context = {'form': form}        
    
    if request.method == 'POST':
        form = JobForm(data=request.POST,instance=instance)
        if form.is_valid():
            # instance.s_word = form.cleaned_data['s_word']
            # instance.media = form.cleaned_data['media']
            instance.active_status = 1
            # instance.executed_date = '1900-01-01'
            # instance.complited_date = '1900-01-01'
            # instance.t_st_date = form.cleaned_data['t_st_date']
            # instance.t_end_date = form.cleaned_data['t_end_date']
            instance.save()
            return redirect(reverse('jobs:joblist'))
        else:
            return HttpResponse("입력 실패")
    return render(request, 'form.html',context)

@login_required(login_url='/')
def job_del(request,id):
    instance = get_object_or_404(Job, pk=id)
    print(instance)
    # print(request.GET.get('id'))
    instance.delete()

    return redirect(reverse('jobs:joblist'))

@login_required(login_url='/')
def target_list(request):
    user = request.user
    target_list=Target_list.objects.filter(user_id=user.id)
    context = {'target_list':target_list}
    # print(context)
    return render(request, 'target_list.html', context)

@login_required(login_url='/')
def target_del(request,id):
    t_instance = get_object_or_404(Target_list, pk=id)
    print(t_instance)
    # print(request.GET.get('id'))
    t_instance.delete()

    return redirect(reverse('jobs:targetlist'))


@login_required(login_url='/')
def target_list_form(request):
    if request.method == 'POST':
        form = Target_list_Form(request.POST,request.FILES)
        if form.is_valid():
            target = form.save(commit=False)
            target.user_id = request.user.id
            target.save()
            print("success")
            return redirect(reverse('jobs:targetlist'))
        else:
            print("fail")
    
    form = Target_list_Form()
    context = {'form': form}        
    return render(request, 'form.html',context)
    # return HttpResponse("This is Target_list view")


@login_required(login_url='/')
def target_list_update_form(request,id):
    instance = get_object_or_404(Target_list, pk=id)
    form = Target_list_Form(instance=instance)
    context = {'form': form}        
    if request.method == 'POST':
        form = Target_list_Form(data=request.POST,instance=instance)
        if form.is_valid():
            instance.active_status = form.cleaned_data['media']
            instance.executed_date = form.cleaned_data['crawling_url']
            instance.complited_date = form.cleaned_data['input_col']
            instance.save()
            return redirect(reverse('jobs:targetlist'))
        else:
            return HttpResponse("입력 실패")
    print(form)
    return render(request, 'form.html',context)


@login_required(login_url='/')
def crawling(request,id):
    if request.method == 'POST':
        # 버튼을 눌러서 잡이 실행되면 클롤링 모듈이 실행된다.
        # request로 현재 유저 정보를 확인하고
        # 넘어오는 id를 통해서 job 정보를 받는다.
        # 모듈에서 필요한 정보


        # 1. 큐에 잡이 저장되고 순서대로 실행되며 잡 갯수는 총 5개를 기준으로 나눠진다.
        # 실행되는 잡 기준으로 실행되는 퍼센테이지를 화면에 디스플레이 해준다.
        # 2. 잡이 큐에 들어가기 전에 실행되는 잡과 큐에 등록된 잡을 확인해서 중복해서 들어오지는 않았는지 확인한다.
        # 3. 
        return
