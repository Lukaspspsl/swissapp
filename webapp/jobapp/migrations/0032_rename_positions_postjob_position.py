# Generated by Django 4.2.3 on 2023-07-18 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0031_alter_position_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postjob',
            old_name='positions',
            new_name='position',
        ),
    ]
