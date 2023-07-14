# Generated by Django 4.2.3 on 2023-07-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_company_num_alter_company_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area_code',
            field=models.CharField(blank=True, choices=[('🇨🇿 CZ', '🇨🇿 +420'), ('🇸🇰 SK', '🇸🇰 +421'), ('🇨🇭 CH', '🇨🇭 +41')], max_length=6),
        ),
    ]