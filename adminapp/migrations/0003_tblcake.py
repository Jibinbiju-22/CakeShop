# Generated by Django 5.1.3 on 2024-11-14 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_tblflavour'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblcake',
            fields=[
                ('cakeid', models.AutoField(primary_key=True, serialize=False)),
                ('cakename', models.CharField(max_length=50)),
                ('cakedescription', models.CharField(max_length=500)),
                ('cakeprice', models.FloatField()),
                ('cakeamount', models.FloatField()),
                ('cakephoto', models.ImageField(upload_to='')),
                ('categoryid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblcategory')),
                ('flavourid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblflavour')),
            ],
        ),
    ]
