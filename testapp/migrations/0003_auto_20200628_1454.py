# Generated by Django 2.1.15 on 2020-06-28 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200628_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crid',
            old_name='name',
            new_name='keyword',
        ),
    ]
