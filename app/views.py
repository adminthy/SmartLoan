from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import LoanType, LoanPlan, Borrower, LoanApplication, LoanPayment, LoanRepaymentSchedule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
def is_admin(user):
    return user.is_authenticated and user.is_superuser
@login_required
def home(request):
    return render(
        request,
        "home.html",
        context={
            "title": "Welcome Home Page"
        }
    )
# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


# Logout
def user_logout(request):
    logout(request)
    return redirect("login")


# Display Loan Type
@login_required
def loan_type_index(request):
    data = LoanType.objects.all()

    return render(
        request,
        "loantype/index.html",
        context={
            "title": "LoanType Page",
            "data": data
        }
    )


# Add Loan Type Page
@login_required
def add_loan_type(request):
    return render(
        request,
        "loantype/add.html"
    )


# Save Loan Type
@login_required
def save_loan_type(request):
    if request.method == "POST":
        loan_type_name = request.POST.get("loan-type-name")
        loan_type_description = request.POST.get("loan-type-description")

        LoanType.objects.create(
            name=loan_type_name,
            description=loan_type_description
        )

        return redirect("loan_type_index")

    return redirect("add_loan_type")


# Edit Loan Type Page
@login_required
def edit_loan_type(request, pk):
    data = get_object_or_404(LoanType, pk=pk)

    return render(
        request,
        "loantype/edit.html",
        {
            "data": data
        }
    )

# Update Loan Type
@login_required
def update_loan_type(request, pk):
    data = get_object_or_404(LoanType, pk=pk)

    if request.method == "POST":
        data.name = request.POST.get("loan-type-name")
        data.description = request.POST.get("loan-type-description")
        data.save()

        return redirect("loan_type_index")

    return redirect("edit_loan_type", pk=pk)


# Delete Confirmation Page
@login_required
def delete_loan_type(request, pk):
    data = get_object_or_404(LoanType, pk=pk)

    return render(
        request,
        "loantype/delete.html",
        context={
            "data": data
        }
    )


# Remove Loan Type
@login_required
def remove_loan_type(request, pk):
    data = get_object_or_404(LoanType, pk=pk)

    if request.method == "POST":
        data.delete()

    return redirect("loan_type_index")


# =========================
# LOAN PLAN CRUD
# =========================

# Display Loan Plan
@login_required
def loan_plan_index(request):

    data = LoanPlan.objects.select_related("loan_type").all()

    return render(
        request,
        "loanplan/index.html",
        {
            "title": "Loan Plan Page",
            "data": data
        }
    )


# Add Loan Plan Page
@login_required
def add_loan_plan(request):
    loan_types = LoanType.objects.all()

    return render(
        request,
        "loanplan/add.html",
        {
            "loan_types": loan_types
        }
    )


# Save Loan Plan
@login_required
def save_loan_plan(request):

    if request.method == "POST":
        LoanPlan.objects.create(
            name=request.POST.get("name"),
            loan_type_id=request.POST.get("loan_type"),
            interest_rate=request.POST.get("interest_rate"),
            duration=request.POST.get("duration"),
            description=request.POST.get("description")
        )

        return redirect("loan_plan_index")

    return redirect("add_loan_plan")


# Edit Loan Plan Page
@login_required
def edit_loan_plan(request, pk):

    data = get_object_or_404(LoanPlan, pk=pk)
    loan_types = LoanType.objects.all()

    return render(
        request,
        "loanplan/edit.html",
        {
            "data": data,
            "loan_types": loan_types
        }
    )


# Update Loan Plan
@login_required
def update_loan_plan(request, pk):

    data = get_object_or_404(LoanPlan, pk=pk)

    if request.method == "POST":
        data.name = request.POST.get("name")
        data.loan_type_id = request.POST.get("loan_type")
        data.interest_rate = request.POST.get("interest_rate")
        data.duration = request.POST.get("duration")
        data.description = request.POST.get("description")

        data.save()
        return redirect("loan_plan_index")

    return redirect("edit_loan_plan", pk=pk)


# Delete Loan Plan Page
@login_required
def delete_loan_plan(request, pk):

    data = get_object_or_404(LoanPlan, pk=pk)

    return render(
        request,
        "loanplan/delete.html",
        {
            "data": data
        }
    )


# Remove Loan Plan
@login_required
def remove_loan_plan(request, pk):
    data = get_object_or_404(LoanPlan, pk=pk)

    if request.method == "POST":
        data.delete()

    return redirect("loan_plan_index")


# =========================
# BORROWER CRUD
# =========================

# Display Borrower
@login_required
def borrower_index(request):
    data = Borrower.objects.all()

    return render(
        request,
        "borrower/index.html",
        {
            "title": "Borrower Page",
            "data": data
        }
    )


# Add Borrower Page
@login_required
def add_borrower(request):

    return render(request, "borrower/add.html")


# Save Borrower
@login_required
def save_borrower(request):
    if request.method == "POST":
        Borrower.objects.create(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            date_of_birth=request.POST.get("date_of_birth"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            address=request.POST.get("address")
        )

        return redirect("borrower_index")

    return redirect("add_borrower")


# Edit Borrower Page
@login_required
def edit_borrower(request, pk):

    data = get_object_or_404(Borrower, pk=pk)

    return render(
        request,
        "borrower/edit.html",
        {
            "data": data
        }
    )


# Update Borrower
@login_required
def update_borrower(request, pk):

    data = get_object_or_404(Borrower, pk=pk)

    if request.method == "POST":
        data.name = request.POST.get("name")
        data.gender = request.POST.get("gender")
        data.date_of_birth = request.POST.get("date_of_birth")
        data.phone = request.POST.get("phone")
        data.email = request.POST.get("email")
        data.address = request.POST.get("address")

        data.save()
        return redirect("borrower_index")

    return redirect("edit_borrower", pk=pk)


# Delete Borrower Page
@login_required
def delete_borrower(request, pk):

    data = get_object_or_404(Borrower, pk=pk)

    return render(
        request,
        "borrower/delete.html",
        {
            "data": data
        }
    )


# Remove Borrower
@login_required
def remove_borrower(request, pk):
    data = get_object_or_404(Borrower, pk=pk)

    if request.method == "POST":
        data.delete()

    return redirect("borrower_index")



# =========================
# LOAN APPLICATION CRUD
# =========================

# Display Loan Application
@login_required
def loan_application_index(request):
    data = LoanApplication.objects.select_related(
        "borrower", "loan_type", "loan_plan"
    ).all()

    return render(
        request,
        "loanapplication/index.html",
        {
            "title": "Loan Application Page",
            "data": data
        }
    )


# Add Loan Application Page
@login_required
def add_loan_application(request):

    borrowers = Borrower.objects.all()
    loan_types = LoanType.objects.all()
    loan_plans = LoanPlan.objects.all()

    return render(
        request,
        "loanapplication/add.html",
        {
            "borrowers": borrowers,
            "loan_types": loan_types,
            "loan_plans": loan_plans
        }
    )


# Save Loan Application
@login_required
def save_loan_application(request):

    if request.method == "POST":
        LoanApplication.objects.create(
            ref_no=request.POST.get("ref_no"),
            borrower_id=request.POST.get("borrower"),
            loan_type_id=request.POST.get("loan_type") or None,
            loan_plan_id=request.POST.get("loan_plan"),
            purpose=request.POST.get("purpose"),
            amount=request.POST.get("amount"),
            release_date=request.POST.get("release_date") or None,
            status=request.POST.get("status") or "Pending"
        )

        return redirect("loan_application_index")

    return redirect("add_loan_application")


# Edit Loan Application Page
@login_required
def edit_loan_application(request, pk):

    data = get_object_or_404(LoanApplication, pk=pk)

    borrowers = Borrower.objects.all()
    loan_types = LoanType.objects.all()
    loan_plans = LoanPlan.objects.all()

    return render(
        request,
        "loanapplication/edit.html",
        {
            "data": data,
            "borrowers": borrowers,
            "loan_types": loan_types,
            "loan_plans": loan_plans
        }
    )


# Update Loan Application
@login_required
def update_loan_application(request, pk):

    data = get_object_or_404(LoanApplication, pk=pk)

    if request.method == "POST":
        data.ref_no = request.POST.get("ref_no")
        data.borrower_id = request.POST.get("borrower")
        data.loan_type_id = request.POST.get("loan_type") or None
        data.loan_plan_id = request.POST.get("loan_plan")
        data.purpose = request.POST.get("purpose")
        data.amount = request.POST.get("amount")
        data.release_date = request.POST.get("release_date") or None
        data.status = request.POST.get("status") or "Pending"

        data.save()

        return redirect("loan_application_index")

    return redirect("edit_loan_application", pk=pk)


# Delete Loan Application Page
@login_required
def delete_loan_application(request, pk):

    data = get_object_or_404(LoanApplication, pk=pk)

    return render(
        request,
        "loanapplication/delete.html",
        {
            "data": data
        }
    )


# Remove Loan Application
@login_required
def remove_loan_application(request, pk):
    data = get_object_or_404(LoanApplication, pk=pk)

    if request.method == "POST":
        data.delete()

    return redirect("loan_application_index")


# =========================
# LOAN PAYMENT CRUD
# =========================

@login_required
def loan_payment_index(request):
    data = LoanPayment.objects.select_related(
        "loan_application",
        "loan_application__borrower"
    ).all()

    return render(
        request,
        "loanpayment/index.html",
        {
            "title": "Loan Payment Page",
            "data": data
        }
    )


@login_required
def add_loan_payment(request):

    applications = LoanApplication.objects.select_related(
        "borrower"
    ).filter(status="Approved")

    return render(
        request,
        "loanpayment/add.html",
        {
            "applications": applications
        }
    )



@login_required
def save_loan_payment(request):

    if request.method == "POST":
        LoanPayment.objects.create(
            loan_application_id=request.POST.get("loan_application"),
            payee_name=request.POST.get("payee_name"),
            payment_amount=request.POST.get("payment_amount"),
            penalty_amount=request.POST.get("penalty_amount"),
            overdue=request.POST.get("overdue"),
            payment_date=timezone.localdate()
        )

        return redirect("loan_payment_index")

    return redirect("add_loan_payment")



@login_required
def edit_loan_payment(request, pk):
    data = get_object_or_404(LoanPayment, pk=pk)

    applications = LoanApplication.objects.filter(status="Approved")

    return render(
        request,
        "loanpayment/edit.html",
        {
            "data": data,
            "applications": applications
        }
    )



@login_required
def update_loan_payment(request, pk):
    data = get_object_or_404(LoanPayment, pk=pk)

    if request.method == "POST":
        data.loan_application_id = request.POST.get("loan_application")
        data.payee_name = request.POST.get("payee_name")
        data.payment_amount = request.POST.get("payment_amount")
        data.penalty_amount = request.POST.get("penalty_amount")
        data.overdue = request.POST.get("overdue")

        data.save()

        return redirect("loan_payment_index")

    return redirect("edit_loan_payment", pk=pk)



@login_required
def delete_loan_payment(request, pk):

    data = get_object_or_404(LoanPayment, pk=pk)

    return render(
        request,
        "loanpayment/delete.html",
        {
            "data": data
        }
    )


@login_required
def remove_loan_payment(request, pk):
    data = get_object_or_404(LoanPayment, pk=pk)

    if request.method == "POST":
        data.delete()

    return redirect("loan_payment_index")
# =========================
# LOAN REPAYMENT SCHEDULE CRUD
# =========================

@login_required
def loan_repayment_schedule_index(request):
    data = LoanRepaymentSchedule.objects.select_related(
        "loan_application",
        "loan_application__borrower"
    ).all()

    return render(
        request,
        "loanrepaymentschedule/index.html",
        {
            "title": "Loan Repayment Schedule Page",
            "data": data
        }
    )
@login_required
def add_loan_repayment_schedule(request):
    applications = LoanApplication.objects.select_related(
        "borrower"
    ).filter(status="Approved")

    return render(
        request,
        "loanrepaymentschedule/add.html",
        {
            "applications": applications
        }
    )
@login_required
def save_loan_repayment_schedule(request):
    if request.method == "POST":
        LoanRepaymentSchedule.objects.create(
            loan_application_id=request.POST.get("loan_application"),
            due_date=request.POST.get("due_date"),
            payment_amount=request.POST.get("payment_amount"),
            status=request.POST.get("status")
        )

        return redirect("loan_repayment_schedule_index")

    return redirect("add_loan_repayment_schedule")
@login_required
def edit_loan_repayment_schedule(request, pk):
    data = get_object_or_404(
        LoanRepaymentSchedule,
        pk=pk
    )

    applications = LoanApplication.objects.filter(
        status="Approved"
    )

    return render(
        request,
        "loanrepaymentschedule/edit.html",
        {
            "data": data,
            "applications": applications
        }
    )
@login_required
def update_loan_repayment_schedule(request, pk):

    data = get_object_or_404(
        LoanRepaymentSchedule,
        pk=pk
    )

    if request.method == "POST":
        data.loan_application_id = request.POST.get("loan_application")
        data.due_date = request.POST.get("due_date")
        data.payment_amount = request.POST.get("payment_amount")
        data.status = request.POST.get("status")

        data.save()

        return redirect("loan_repayment_schedule_index")

    return redirect("edit_loan_repayment_schedule", pk=pk)
@login_required
def delete_loan_repayment_schedule(request, pk):
    data = get_object_or_404(
        LoanRepaymentSchedule,
        pk=pk
    )

    return render(
        request,
        "loanrepaymentschedule/delete.html",
        {
            "data": data
        }
    )
@login_required
def remove_loan_repayment_schedule(request, pk):
    data = get_object_or_404(
        LoanRepaymentSchedule,
        pk=pk
    )

    if request.method == "POST":
        data.delete()

    return redirect("loan_repayment_schedule_index")

# ================= USER MANAGEMENT =================

@login_required
@user_passes_test(is_admin)
def user_index(request):
    users = User.objects.all().order_by("id")

    return render(
        request,
        "user_index.html",
        {"users": users}
    )


@login_required
@user_passes_test(is_admin)
def add_user(request):
    return render(request, "user_add.html")


@login_required
@user_passes_test(is_admin)
def save_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("add_user")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "User created successfully")
        return redirect("user_index")

    return redirect("add_user")


@login_required
@user_passes_test(is_admin)
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if user.is_superuser:
        messages.error(request, "Cannot delete superuser")
        return redirect("user_index")

    user.delete()
    messages.success(request, "User deleted successfully")

    return redirect("user_index")