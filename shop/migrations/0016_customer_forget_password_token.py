# Generated by Django 3.2.10 on 2022-01-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_edition_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='forget_password_token',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
