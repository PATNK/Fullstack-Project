# Generated by Django 5.0.4 on 2024-05-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
                ('Matric_Number', models.CharField(max_length=30)),
                ('Class', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]
