# Generated by Django 3.0.8 on 2021-01-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('passward', models.CharField(max_length=264)),
                ('confirm_password', models.CharField(max_length=264)),
            ],
        ),
    ]
