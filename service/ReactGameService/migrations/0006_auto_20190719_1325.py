# Generated by Django 2.2.1 on 2019-07-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReactGameService', '0005_auto_20190715_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]