# Generated by Django 5.0.2 on 2024-05-21 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taller', models.CharField(max_length=100)),
                ('actividad', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('catalogoId', models.ForeignKey(db_column='catalogoId', on_delete=django.db.models.deletion.CASCADE, to='catalogos.catalogo')),
                ('userId', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'visitas',
                'verbose_name_plural': 'viista',
                'db_table': 'visitas',
                'managed': True,
            },
        ),
    ]
