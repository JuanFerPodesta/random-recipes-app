# Generated by Django 4.1.5 on 2023-01-21 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rr_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='ingredientes',
            new_name='ingredients',
        ),
    ]