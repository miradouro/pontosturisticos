# Generated by Django 3.1.7 on 2021-04-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210403_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=True),
        ),
    ]
