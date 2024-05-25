from audioop import reverse
from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'job/job_list.html', {'jobs':page_obj, 'myfilter':myfilter})


# def job_detail(request, id):
#     job_detail = Job.objects.get(id = id)
#     return render(request, 'job/job_detail.html', {'job':job_detail})

def job_detail(request, slug):
    job_detail = Job.objects.get(slug = slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
        else:
            print(form.errors)
    else :
        form = ApplyForm()
    
    return render(request, 'job/job_detail.html', {'job':job_detail, 'form':form})

@login_required
def add_job(request):
    if request.method == 'post':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:jobs_list'))
        else:
            print(form.errors)
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form':form})