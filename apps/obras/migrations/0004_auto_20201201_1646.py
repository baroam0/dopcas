# Generated by Django 2.2 on 2020-12-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0003_delete_adjudicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='concluida',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='obra',
            name='fecha_recepcion_definitiva',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='obra',
            name='fecha_recepcion_provisoria',
            field=models.DateField(blank=True, null=True),
        ),
    ]