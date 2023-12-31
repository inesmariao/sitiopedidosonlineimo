# Generated by Django 4.2.2 on 2023-06-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'medida',
            },
        ),
    ]
