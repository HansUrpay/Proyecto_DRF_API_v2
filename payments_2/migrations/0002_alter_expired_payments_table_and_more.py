# Generated by Django 4.1.4 on 2022-12-29 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='expired_payments',
            table='expired_payment',
        ),
        migrations.AlterModelTable(
            name='payment_user',
            table='payment_user',
        ),
    ]
