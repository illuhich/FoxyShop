# Generated by Django 2.2.10 on 2020-04-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delivery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['user'], 'verbose_name': 'Доставка', 'verbose_name_plural': 'Доставка'},
        ),
    ]
