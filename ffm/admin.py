from django.contrib import admin
from.models import user_register,Feedback,Income,Expense,Expenseimage
from .models import *
# Register your models here.
admin.site.register(user_register)
admin.site.register(Feedback)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Expenseimage)
admin.site.register(ExpenseLimit)
admin.site.register(Goal)