# Generated by Django 3.1.14 on 2023-08-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program_language',
            options={'ordering': ['name'], 'verbose_name': 'Мова', 'verbose_name_plural': 'Мови'},
        ),
    ]
