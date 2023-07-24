# Generated by Django 4.2.3 on 2023-07-18 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0029_postjob_work_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]