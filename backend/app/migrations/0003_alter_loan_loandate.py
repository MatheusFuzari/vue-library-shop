# Generated by Django 5.0.6 on 2024-05-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loanDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
