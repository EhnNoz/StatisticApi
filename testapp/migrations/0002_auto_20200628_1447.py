# Generated by Django 2.1.15 on 2020-06-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CR_TABLE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=1000)),
                ('res_ID', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='crid',
            name='channel',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]