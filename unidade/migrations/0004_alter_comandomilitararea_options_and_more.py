# Generated by Django 4.1.1 on 2022-10-09 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0003_alter_comandomilitararea_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comandomilitararea',
            options={'ordering': ['abreviatura'], 'verbose_name': 'C Mil A', 'verbose_name_plural': 'C Mil A'},
        ),
        migrations.AlterModelOptions(
            name='regiaomilitar',
            options={'ordering': ['abreviatura'], 'verbose_name': 'RM', 'verbose_name_plural': 'RM'},
        ),
        migrations.AlterModelOptions(
            name='unidade',
            options={'ordering': ['codug'], 'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
    ]
