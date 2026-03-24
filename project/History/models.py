from django.db import models
from Batch import models as B_models
from Students import models as S_models
import datetime as dt

# Create your functions here

def get_HR_time(datetime = dt.datetime.now()) -> str:
    return datetime.strftime("(%I:%M%p) (%d/%m/%Y) (%a)")

# Create your models here.

class Session(models.Model):
    batch = models.ForeignKey(B_models.Batch, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=dt.datetime.now)

class Participated(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(S_models.Student, on_delete=models.CASCADE)

class Payment(models.Model):
    student = models.OneToOneField(S_models.Student, models.CASCADE, primary_key=True)
    amount_needed = models.IntegerField()
    amount_paid = models.IntegerField()
    context = models.CharField(max_length=127)

    @property
    def amount_to_clear(self) -> int:
        return (self.amount_needed - self.amount_paid)
    
    @property
    def is_cleared(self) -> bool:
        return self.amount_to_clear <= 0

    def Pay(self) -> str|None:
        needs = self.amount_to_clear
        has = self.student.v_balance
        if needs and has:
            pass
        else:
            return f"{self.student} Already Cleared" if needs == 0 else f"{self.student} has no balance inserted"

        # complete exchange start
        exchange_amount = min(needs, has)
        self.amount_paid, self.student.v_balance  = self.amount_paid + exchange_amount, has - exchange_amount
        # complete exchnage end
        
        self.student.save()
        self.save()

        return f"{self.student} has been paid successfully {get_HR_time()}"



















