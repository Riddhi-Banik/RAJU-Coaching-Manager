import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import models as S_models
from . import forms as S_forms
from Batch import models as B_models
from History import models as H_models
from django.db.models import QuerySet
# Create your pseudo callers here
Student = S_models.Student
Batch = B_models.Batch
StudentAddJson = S_forms.Student_AddForm
Class_choice = S_models.Class_choice
Batch_choice:list[tuple[str, str]] = [
    (x.name, x.name) for x in Batch.objects.all()
]
Gender_choice:list[tuple[str, str]] = [
    (x, x) for x in ('Male', 'Female')
]


# Create your functions here.
def db_to_json(data: QuerySet, keys: list[str]) -> str:
    JsonInPy : dict[int, dict] = {
        i: {k: getattr(x, k) for k in keys} 
        for i, x in enumerate(data)
    }
    return json.dumps(JsonInPy, default=str)

# Create your views here.

def student(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        print('request.POST = v')
        print(request.POST)
        if 'AddFormJson' in request.POST:
            form = StudentAddJson(data = request.POST)
            if form.is_valid():
                cleanedForm = form.cleaned_data            
                Student.objects.create(
                    # defaults
                    v_balance = 0,
                    # user_data
                    gender = cleanedForm['JsonData']['Gender'],
                    mobile_no = cleanedForm['JsonData']['Mobile'],
                    name = cleanedForm['JsonData']['Name'],
                    cls = cleanedForm['JsonData']['Class'],
                    batch = cleanedForm['JsonData']['Batch']
                ).save()
            elif 'EditFormJson' in request.POST:
                pass
            else:
                pass
    
    StudentAddForm = StudentAddJson()
    context:dict = {
        'forms' : {
            'AddForm' : StudentAddForm,
        },
        'student' : {
            'qty' : S_models.Student.objects.count(),
            'data' : db_to_json(Student.objects.all(), 
                    ['cls', 'batch' ,'roll', 'name', 'gender', 'v_balance', 'mobile_no'])
        },
        'batch'  : {
            'qty' : B_models.Batch.objects.count(),
            'data' : db_to_json(Batch.objects.all(),
                    ['name', 'is_running']),
        },
        'Class_choice' : (x[0] for x in Class_choice),
        'Batch_choice' : (x[0] for x in Batch_choice),
        'Gender_choice': (x[0] for x in Gender_choice),

    }

    

    return render(request, 'contexts/student.html', context)