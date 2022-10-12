# Generated by Django 4.1.1 on 2022-10-12 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
        ('localidade', '0004_cidade_delete_localidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('cidade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidade.cidade', verbose_name='Cidade')),
                ('despesa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='despesa.despesa', verbose_name='Despesa')),
            ],
            options={
                'verbose_name': 'Localidade',
                'verbose_name_plural': 'Localidades',
            },
        ),
    ]