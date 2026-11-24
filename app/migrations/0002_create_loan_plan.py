
from django.db import migrations


def create_loan_plan_table(apps, schema_editor):
    LoanPlan = apps.get_model("app", "LoanPlan")

    table_name = LoanPlan._meta.db_table
    existing_tables = schema_editor.connection.introspection.table_names()

    if table_name not in existing_tables:
        schema_editor.create_model(LoanPlan)


def reverse_create_loan_plan_table(apps, schema_editor):
    LoanPlan = apps.get_model("app", "LoanPlan")

    table_name = LoanPlan._meta.db_table
    existing_tables = schema_editor.connection.introspection.table_names()

    if table_name in existing_tables:
        schema_editor.delete_model(LoanPlan)


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_loan_plan_table,
            reverse_create_loan_plan_table
        ),
    ]
