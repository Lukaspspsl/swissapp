# Generated by Django 4.2.2 on 2023-07-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0020_alter_postjob_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="postjob",
            name="accomodation",
            field=models.CharField(
                choices=[
                    ("vlastní ubytování", "vlastní ubytování"),
                    ("zajištěné ubytování", "zajištěné ubytování"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="postjob",
            name="experience",
            field=models.CharField(
                choices=[
                    ("1-3 roky", "1-3"),
                    ("4-6 let", "4-6"),
                    ("6-9 let", "6-9"),
                    ("10 a více let", "10 a více"),
                ],
                default="bez zkušeností",
                max_length=100,
            ),
        ),
    ]