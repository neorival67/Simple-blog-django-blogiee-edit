# Generated by Django 4.2.4 on 2023-09-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
