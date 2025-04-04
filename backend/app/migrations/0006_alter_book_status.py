# Generated by Django 5.0.6 on 2024-05-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_book_rating_alter_loan_bookfk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('APROVADO', 'APROVADO'), ('PENDENTE', 'PENDENTE'), ('CANCELADO', 'CANCELADO')], default='PENDENTE', max_length=50, null=True),
        ),
    ]
