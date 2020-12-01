# Generated by Django 2.2.8 on 2020-11-21 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0002_unidadtiempo'),
        ('contratocooperativas', '0005_auto_20201120_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratocooperativa',
            name='unidadtiempo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='complementos.UnidadTiempo'),
        ),
    ]