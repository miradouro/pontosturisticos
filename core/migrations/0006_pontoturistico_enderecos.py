# Generated by Django 3.1.7 on 2021-04-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ManyToManyField(to='enderecos.Endereco'),
        ),
    ]
