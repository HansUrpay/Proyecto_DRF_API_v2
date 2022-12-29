# Generated by Django 4.1.4 on 2022-12-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.URLField(max_length=255)),
                ('prefijo', models.CharField(default='--', max_length=3)),
            ],
            options={
                'db_table': 'services_2',
            },
        ),
    ]
