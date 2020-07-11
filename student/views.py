from django.shortcuts import render, redirect
from .models import StudentList
from .forms import ResultForm, StudentCreateForm


def create_student(request):
    form = StudentCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # c_roll = form.cleaned_data["roll"]
            # c_name = form.cleaned_data["name"]
            # c_std_class = form.cleaned_data["std_class"]
            # c_gender = form.cleaned_data["gender"]
            #
            # StudentList.objects.create(
            #     roll=c_roll,
            #     name=c_name,
            #     std_class=c_std_class,
            #     gender=c_gender
            # )
            form.save()
            return redirect('create-student')


    context = {
        'form': form
    }
    return render(request, 'student/create_std.html', context)


def get_result(request):
    form = ResultForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            std_class = form.cleaned_data["std_class"]
            roll = form.cleaned_data["roll"]

            try:
                std = StudentList.objects.get(std_class=std_class, roll=roll)
                context = {'gpa': std.gpa, 'form': form}
            except Exception as err:
                context = {'error': str(err), 'form': form}
    return render(request, 'student/get_result.html', context)


def student_filter(request, gender):
    std_list = StudentList.objects.filter(gender='male')
    return render(request, 'std_filter', {'std_list': std_list})


def student_detail(request, roll):
    student = {
        1: {
            "name": "Std 1",
            "gender": "Male",
            "phone": "01711"
        },
        2: {
            "name": "Std 2",
            "gender": "Male",
            "phone": "01711"
        },
        3: {
            "name": "Std 3",
            "gender": "Male",
            "phone": "01711"
        },

    }

    student_detail = student[roll]

    context = {
        'std': student_detail
    }
    return render(request, 'std_detail.html', context)