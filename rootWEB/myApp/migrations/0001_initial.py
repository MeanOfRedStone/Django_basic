# Generated by Django 4.1.7 on 2023-03-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_tbl',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_pwd', models.CharField(max_length=50)),
            ],
        ),
    ]