from django.db import models
from Batch import models as B_models
import random
from django.db.models import QuerySet

# create your variables here

Gender_choice: list[tuple[str, str]] = [
    ("male", "male"),
    ("female", "female"),
    ("unspec", "unspec")
]

Class_choice: list[tuple[str, str]] = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('new 10', 'new 10'),
    ('old 10', 'old 10'),
]
# Create your functions here.



# Create your models here.

class Student(models.Model):
    mobile_no = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=Gender_choice, default=" - ")
    roll = models.CharField(max_length=4, default=random.randint(1,100))
    cls = models.CharField(max_length=7, choices=Class_choice)
    batch = models.ForeignKey(B_models.Batch, on_delete=models.CASCADE)
    v_balance = models.IntegerField(null=True)

    def __str__(self):
        return self.name


def get_all_rolls() -> list[int]:
    students:QuerySet[Student] = Student.objects.only('roll')
    
def generate_roll() -> int:
    return random.randint(1, 100)
    

# Create your Sub-iconic functions here


