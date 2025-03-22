from django.db import models

# Create your models here.
class user_register(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=60,null=True,blank=True)
    image=models.ImageField(upload_to='user_image/',null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    re_password=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return str(self.Name)
    
class Feedback(models.Model):
    RATING_CHOICES=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    feedback_text=models.TextField()
    rating=models.IntegerField(choices=RATING_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()
    def __str__(self):
        return str(self.email)


class Income(models.Model):
    user=models.ForeignKey(user_register,on_delete=models.CASCADE,blank=True)
    incomesource=models.CharField(max_length=50)
    income=models.IntegerField()
    totalincome=models.IntegerField()
    date = models.DateField() 
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Income from {self.incomesource} on {self.date}"
    
class Expense(models.Model):
    user = models.ForeignKey('user_register', on_delete=models.CASCADE, null=True, blank=True)
    expensecategory = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.expensecategory} - {self.amount} on {self.date}"
    
class  Expenseimage(models.Model):
    user=models.ForeignKey(user_register,on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to='expense/')
    
class ExpenseLimit(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    expensecategory = models.CharField(max_length=100)
    limit_amount = models.FloatField()

    def __str__(self):
        return f"{self.user.Name} - {self.expensecategory} - {self.limit_amount}"

# class Goal(models.Model):
#     user = models.ForeignKey('user_register', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)  # The name of the goal (e.g., "Vacation", "Emergency Fund")
#     target_amount = models.FloatField()  # The target amount the user wants to save
#     current_savings = models.FloatField(default=0.0)  # The amount the user has saved so far
#     start_date = models.DateField()  # When they started saving

#     def __str__(self):
#         return self.name

class Goal(models.Model):
    user = models.ForeignKey('user_register', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

