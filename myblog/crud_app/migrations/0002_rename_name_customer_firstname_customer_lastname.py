# Generated by Django 5.0.4 on 2024-05-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
