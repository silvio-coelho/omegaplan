# Generated by Django 3.2 on 2021-04-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0003_alter_arquivo_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
