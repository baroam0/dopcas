# Generated by Django 2.2 on 2020-11-27 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratocooperativas', '0007_remove_contratocooperativa_tareas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratocooperativa',
            name='numeropoliza',
        ),
        migrations.RemoveField(
            model_name='contratocooperativa',
            name='poliza',
        ),
    ]
