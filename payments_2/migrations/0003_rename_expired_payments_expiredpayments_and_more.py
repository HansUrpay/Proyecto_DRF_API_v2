# Generated by Django 4.1.4 on 2022-12-29 03:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services_2', '0002_alter_services_table'),
        ('payments_2', '0002_alter_expired_payments_table_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expired_payments',
            new_name='ExpiredPayments',
        ),
        migrations.RenameModel(
            old_name='Payment_user',
            new_name='PaymentUser',
        ),
    ]