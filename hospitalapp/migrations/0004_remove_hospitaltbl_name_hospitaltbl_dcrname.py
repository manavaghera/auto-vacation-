# Generated by Django 4.2.4 on 2023-09-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_vaccinetbl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitaltbl',
            name='name',
        ),
        migrations.AddField(
            model_name='hospitaltbl',
            name='dcrname',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Doctor Name'),
        ),
    ]
