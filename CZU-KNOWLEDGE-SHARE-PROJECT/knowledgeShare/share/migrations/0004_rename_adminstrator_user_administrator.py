# Generated by Django 3.2.9 on 2021-12-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20211208_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adminstrator',
            new_name='administrator',
        ),
    ]