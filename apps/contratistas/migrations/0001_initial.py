# Generated by Django 2.2.8 on 2020-07-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Contratistas',
            },
        ),
    ]
