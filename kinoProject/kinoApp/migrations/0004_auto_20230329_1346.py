# Generated by Django 3.1 on 2023-03-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinoApp', '0003_auto_20230329_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]
