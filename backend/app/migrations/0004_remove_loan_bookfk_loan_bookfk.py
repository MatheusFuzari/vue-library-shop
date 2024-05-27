# Generated by Django 5.0.6 on 2024-05-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_loan_loandate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='bookFK',
        ),
        migrations.AddField(
            model_name='loan',
            name='bookFK',
            field=models.ManyToManyField(blank=True, related_name='bookLoan', to='app.book'),
        ),
    ]
