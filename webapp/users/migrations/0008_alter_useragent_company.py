# Generated by Django 4.2.2 on 2023-07-02 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_useragent_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useragent",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Companies",
                to="users.company",
            ),
        ),
    ]
