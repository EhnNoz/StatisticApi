# Generated by Django 2.1.15 on 2020-06-28 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20200628_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crid',
            old_name='channel',
            new_name='res_ID',
        ),
    ]
