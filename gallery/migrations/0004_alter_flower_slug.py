# Generated by Django 5.1.1 on 2024-09-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_flower_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
