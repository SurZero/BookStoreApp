# Generated by Django 3.0.6 on 2020-08-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200515_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='cover_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
