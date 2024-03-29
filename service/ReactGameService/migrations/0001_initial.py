# Generated by Django 2.2.1 on 2019-07-09 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Testee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=200)),
                ('google_username', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_result', models.TextField(max_length=200)),
                ('time_result', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organisation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReactGameService.Organisation')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReactGameService.Test')),
                ('testee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReactGameService.Testee')),
            ],
        ),
    ]
