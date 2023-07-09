# Generated by Django 4.2.2 on 2023-07-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0027_merge_20230707_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('NO', 'žádný'), ('ENG', '🇬🇧 angličtina'), ('CHF', '🇨🇭 švýcarská němčina'), ('DEU', '🇩🇪 němčina'), ('FRA', '🇫🇷 francouzština'), ('ITA', '🇮🇹 italština')], max_length=5)),
                ('level', models.CharField(choices=[('1', 'A1 - začátečník'), ('2', 'A2 - pokročilý začátečník'), ('3', 'B1 - mírně pokročilý'), ('4', 'B2 - středně pokročilý'), ('5', 'C1 - velmi pokročilý'), ('6', 'C2 - expert')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='postjob',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postjob',
            name='licence',
        ),
        migrations.AddField(
            model_name='drivinglicence',
            name='licence',
            field=models.CharField(choices=[('', '---------'), ('AM', 'AM 🛵'), ('A1', 'A1'), ('A2', 'A2'), ('A', 'A 🏍️'), ('B1', 'B1 🚚'), ('B', 'B 🚗'), ('C1', 'C1 🚛'), ('C', 'C'), ('D1', 'D1 🚐'), ('D', 'D 🚌'), ('BE', 'BE '), ('C1E', 'C1E'), ('CE', 'CE'), ('D1E', 'D1E'), ('DE', 'DE'), ('T', 'T 🚜')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='postjob',
            name='driving_licence',
            field=models.ManyToManyField(blank=True, to='jobapp.drivinglicence'),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='experience',
            field=models.CharField(choices=[('1-3 roky', '1-3'), ('4-6 let', '4-6'), ('6-9 let', '6-9'), ('10 a více let', '10 a více')], default='1-3', max_length=100),
        ),
        migrations.RemoveField(
            model_name='postjob',
            name='language',
        ),
        migrations.AddField(
            model_name='postjob',
            name='language',
            field=models.ManyToManyField(blank=True, to='jobapp.language'),
        ),
    ]
