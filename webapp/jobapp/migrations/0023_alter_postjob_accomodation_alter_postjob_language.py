# Generated by Django 4.2.2 on 2023-07-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0022_alter_postjob_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postjob",
            name="accomodation",
            field=models.CharField(
                choices=[
                    ("vlastní ubytování", "vlastní"),
                    ("zajištěné ubytování", "zajištěné"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="postjob",
            name="language",
            field=models.CharField(
                choices=[
                    ("NO", "žádný"),
                    ("🇬🇧A1/A2", "🇬🇧 A1/A2"),
                    ("🇬🇧B1/B2", "🇬🇧 B1/B2"),
                    ("🇬🇧C1/C2", "🇬🇧 C1/C2"),
                    ("🇨🇭A1/A2", "🇨🇭 A1/A2"),
                    ("🇨🇭B1/B2", "🇨🇭 B1/B2"),
                    ("🇨🇭C1/C2", "🇨🇭 C1/C2"),
                    ("🇩🇪A1/A2", "🇩🇪 A1/A2"),
                    ("🇩🇪B1/B2", "🇩🇪 B1/B2"),
                    ("🇩🇪C1/C2", "🇩🇪 C1/C2"),
                    ("🇫🇷A1/A2", "🇫🇷 A1/A2"),
                    ("🇫🇷B1/B2", "🇫🇷 B1/B2"),
                    ("🇫🇷C1/C2", "🇫🇷 C1/C2"),
                    ("🇮🇹A1/A2", "🇮🇹 A1/A2"),
                    ("🇮🇹B1/B2", "🇮🇹 B1/B2"),
                    ("🇮🇹C1/C2", "🇮🇹 C1/C2"),
                ],
                default="NO",
                max_length=100,
            ),
        ),
    ]