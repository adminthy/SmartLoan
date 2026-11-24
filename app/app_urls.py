
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Loan Type CRUD
    path("loan-type/index", views.loan_type_index, name="loan_type_index"),
    path("loan-type/add", views.add_loan_type, name="add_loan_type"),
    path("loan-type/save", views.save_loan_type, name="save_loan_type"),
    path("loan-type/edit/<int:pk>", views.edit_loan_type, name="edit_loan_type"),
    path("loan-type/update/<int:pk>", views.update_loan_type, name="update_loan_type"),
    path("loan-type/delete/<int:pk>", views.delete_loan_type, name="delete_loan_type"),
    path("loan-type/remove/<int:pk>", views.remove_loan_type, name="remove_loan_type"),

    # Loan Plan CRUD
    path("loan-plan/index", views.loan_plan_index, name="loan_plan_index"),
    path("loan-plan/add", views.add_loan_plan, name="add_loan_plan"),
    path("loan-plan/save", views.save_loan_plan, name="save_loan_plan"),
    path("loan-plan/edit/<int:pk>", views.edit_loan_plan, name="edit_loan_plan"),
    path("loan-plan/update/<int:pk>", views.update_loan_plan, name="update_loan_plan"),
    path("loan-plan/delete/<int:pk>", views.delete_loan_plan, name="delete_loan_plan"),
    path("loan-plan/remove/<int:pk>", views.remove_loan_plan, name="remove_loan_plan"),
        # Borrower CRUD
    path("borrower/index", views.borrower_index, name="borrower_index"),
    path("borrower/add", views.add_borrower, name="add_borrower"),
    path("borrower/save", views.save_borrower, name="save_borrower"),
    path("borrower/edit/<int:pk>", views.edit_borrower, name="edit_borrower"),
    path("borrower/update/<int:pk>", views.update_borrower, name="update_borrower"),
    path("borrower/delete/<int:pk>", views.delete_borrower, name="delete_borrower"),
    path("borrower/remove/<int:pk>", views.remove_borrower, name="remove_borrower"),
        # Loan Application CRUD
    path("loan-application/index", views.loan_application_index, name="loan_application_index"),
    path("loan-application/add", views.add_loan_application, name="add_loan_application"),
    path("loan-application/save", views.save_loan_application, name="save_loan_application"),
    path("loan-application/edit/<int:pk>", views.edit_loan_application, name="edit_loan_application"),
    path("loan-application/update/<int:pk>", views.update_loan_application, name="update_loan_application"),
    path("loan-application/delete/<int:pk>", views.delete_loan_application, name="delete_loan_application"),
    path("loan-application/remove/<int:pk>", views.remove_loan_application, name="remove_loan_application"),
    
    # Loan Payment CRUD
    path("loan-payment/index", views.loan_payment_index, name="loan_payment_index"),
    path("loan-payment/add", views.add_loan_payment, name="add_loan_payment"),
    path("loan-payment/save", views.save_loan_payment, name="save_loan_payment"),
    path("loan-payment/edit/<int:pk>", views.edit_loan_payment, name="edit_loan_payment"),
    path("loan-payment/update/<int:pk>", views.update_loan_payment, name="update_loan_payment"),
    path("loan-payment/delete/<int:pk>", views.delete_loan_payment, name="delete_loan_payment"),
    path("loan-payment/remove/<int:pk>", views.remove_loan_payment, name="remove_loan_payment"),
    # LOAN REPAYMENT SCHEDULE
     path("loan-repayment-schedule/index", views.loan_repayment_schedule_index, name="loan_repayment_schedule_index"),
     path("loan-repayment-schedule/add", views.add_loan_repayment_schedule, name="add_loan_repayment_schedule"),
     path("loan-repayment-schedule/save", views.save_loan_repayment_schedule, name="save_loan_repayment_schedule"),
     path("loan-repayment-schedule/edit/<int:pk>", views.edit_loan_repayment_schedule, name="edit_loan_repayment_schedule"),
     path("loan-repayment-schedule/update/<int:pk>", views.update_loan_repayment_schedule, name="update_loan_repayment_schedule"),
     path("loan-repayment-schedule/delete/<int:pk>", views.delete_loan_repayment_schedule, name="delete_loan_repayment_schedule"),
     path("loan-repayment-schedule/remove/<int:pk>", views.remove_loan_repayment_schedule, name="remove_loan_repayment_schedule"),
         # Authentication
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    # User Management
    path("user/index", views.user_index, name="user_index"),
    path("user/add", views.add_user, name="add_user"),
    path("user/save", views.save_user, name="save_user"),
     path("user/delete/<int:pk>", views.delete_user, name="delete_user"),
    
]
