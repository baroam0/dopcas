# Generated by Django 2.2.8 on 2020-11-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratosobras', '0003_auto_20201122_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratoobra',
            name='tareas',
        ),
    ]