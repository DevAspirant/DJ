# Generated by Django 3.0.7 on 2020-07-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200710_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]