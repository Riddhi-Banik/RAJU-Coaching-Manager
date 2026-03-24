import django.forms as forms
from django.core.exceptions import ValidationError

from . import models as S_models
from Batch import models as B_models

# initialize variables
Class_choice: list[tuple[str, str]] = S_models.Class_choice
Batch = B_models.Batch


class Student_AddForm(forms.Form):
    JsonData = forms.JSONField(
        widget = forms.HiddenInput(
            attrs = {
            'class' : 'JsonF_Form',
            'id' : 'Student_add_form',

            }
        )
    )

    
    def clean(self):
        cleaned_data = super().clean()
        #print("started cleaning")
        dataDict:dict[str, str] = cleaned_data.get('JsonData')
        if dataDict:
            name:str = dataDict['Name']
            gender:str = dataDict['Gender']
            mobile:str = dataDict['Mobile']
            clas:str = dataDict['Class']
            batch:str = dataDict['Batch']

            ExistingBatches:list[str] = [x.__str__() for x in Batch.objects.all()]

            if len(name) > 26:
                raise ValidationError('Name too long')
            elif gender.lower().strip() not in ['male', 'female', '-']:
                raise ValueError('gender incorrect')
            elif (mobile[1:]).isalpha():
                raise ValidationError('mobile no not correct')
            elif (clas, clas,) not in Class_choice:
                raise ValidationError('Specify class correctly')
            elif batch not in ExistingBatches: # implement after 
                raise ValidationError('batch doesnt exist')

            dataDict['Batch'] = Batch.objects.get(name = batch)
            

            return cleaned_data
        
        else:
            raise ValidationError('No Data is here! DUH!')
        


        
