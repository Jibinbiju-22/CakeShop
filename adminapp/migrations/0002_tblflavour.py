# Generated by Django 5.1.3 on 2024-11-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblflavour',
            fields=[
                ('flavourid', models.AutoField(primary_key=True, serialize=False)),
                ('flavourname', models.CharField(max_length=50)),
            ],
        ),
    ]
