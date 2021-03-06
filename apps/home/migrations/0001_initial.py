# Generated by Django 4.0.5 on 2022-06-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
                ('priority_level', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
