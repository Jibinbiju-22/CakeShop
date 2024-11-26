# Generated by Django 5.1.3 on 2024-11-16 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbluser',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('contactname', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('profilephoto', models.ImageField(upload_to='')),
                ('loginid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='guestapp.tbllogin')),
            ],
        ),
    ]
