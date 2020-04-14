# Generated by Django 2.2.10 on 2020-04-11 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_remove_product_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rubric',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='slug',
        ),
        migrations.CreateModel(
            name='RubricTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.Rubric')),
            ],
            options={
                'verbose_name': 'Рубрика Translation',
                'db_table': 'shop_rubric_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
        ),
    ]