# Generated by Django 4.1.5 on 2023-07-16 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_acesso_alter_usuarios_data_postagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Acesso',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='data_postagem',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 6, 45, 56, 611408)),
        ),
    ]
