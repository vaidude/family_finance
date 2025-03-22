from django.urls import path
from ffm import views

urlpatterns=[
    path('',views.indexpage,name='indexpage'),
    path('indexpage/',views.indexpage,name='indexpage'),
    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contactpage,name='contact'),
    path('services/',views.servicespage,name='services'),
    path('logout/',views.logout,name='logout'),

    path('register/',views.registerpage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('profile/',views.profile,name='profile'),
    path('edit/<int:uid>/',views.edit,name='edit'),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('home/',views.home,name='home'),
    path('addincome/',views.addincome,name='addincome'),
    path('listincome/',views.list_income,name='listincome'),
    path('edit_income/<int:income_id>/',views.edit_income,name='edit_income'),  
    path('deleteincome/<int:in_id>/',views.deleteincome,name='deleteincome'),
    
    path('addexpense/',views.addexpense,name='addexpense'),
    path('editexpense/<int:expense_id>/', views.editexpense, name='editexpense'),
    path('expenselist/',views.expenselist,name='expenselist'),
    path('editexpense/<int:expense_id>/',views.editexpense,name='editexpense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('expenseimage/',views.addexpenseimage,name='expenseimage'),
    path('add-expense-voice/', views.add_expense_voice, name='addexpensevoice'),
    path('addexpensevoice/', views.add_expense_voice, name='add_expense_voice'),

    path('expense-pie-chart/', views.expense_bar_chart, name='expense_pie_chart'),
    path('verify-otp/', views.loginpage, name='verify_otp'),
    
    
    path('predict_expenses/', views.predict_expenses, name='predict_expenses'),
    path('predict_savings/', views.predict_savings, name='predict_savings'),
    path('viewgoals/', views.view_goals, name='viewgoals'),
    
    
    path('set_expense_limit/', views.set_category_limit, name='set_expense_limit'),
    path('expense_limit/', views.category_limit_check, name='expense_limit'),
    path('delete-expense-limit/<int:limit_id>/', views.delete_expense_limit, name='delete_expense_limit'),
    
    path('exportexcel/', views.export_report, name='exportexcel'),
    path('processpdf/', views.process_pdf, name='processpdf'),
    
    
    path('adminindex/',views.adminindex,name='adminindex'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlist/',views.userlist,name='userlist'),
    path('user_delete/<int:did>/',views.user_delete,name='user_delete'),
    path('feedback/',views.feedback,name='feedback'),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('deletefeedback/<int:id>/',views.deletefeedback,name='deletefeedback'),
    
    path('scan/', views.scan_receipt, name='scan_receipt'),
    
   

   
    
]