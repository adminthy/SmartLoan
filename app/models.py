
from django.db import models


class LoanType(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "tbl_loan_type"

    def __str__(self):
        return self.name

class LoanPlan(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    loan_type = models.ForeignKey(
        LoanType,
        on_delete=models.CASCADE
    )

    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    duration = models.IntegerField()

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "tbl_loan_plan"

    def __str__(self):
        return self.name

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "tbl_borrower"

    def __str__(self):
        return self.name


class LoanApplication(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    ref_no = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    borrower = models.ForeignKey(
        Borrower,
        on_delete=models.CASCADE
    )

    loan_type = models.ForeignKey(
        LoanType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    loan_plan = models.ForeignKey(
        LoanPlan,
        on_delete=models.CASCADE
    )

    purpose = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    application_date = models.DateField(
        auto_now_add=True
    )

    release_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    class Meta:
        db_table = "tbl_loan_application"

    def __str__(self):
        return f"{self.borrower.name} - {self.amount}"



class LoanPayment(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]

    OVERDUE_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    loan_application = models.ForeignKey(
        LoanApplication,
        on_delete=models.CASCADE
    )

    payee_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    payment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    penalty_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    overdue = models.CharField(
        max_length=10,
        choices=OVERDUE_CHOICES,
        default="No"
    )

    payment_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="Pending"
    )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "tbl_loan_payment"

    def __str__(self):
        return f"{self.loan_application} - {self.payment_amount}"

class LoanRepaymentSchedule(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Overdue", "Overdue"),
    ]

    loan_application = models.ForeignKey(
        LoanApplication,
        on_delete=models.CASCADE
    )

    due_date = models.DateField()

    payment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    class Meta:
        db_table = "tbl_loan_repayment_schedule"

    def __str__(self):
        return f"{self.loan_application} - {self.due_date}"


