# Generated by Django 3.1.2 on 2020-11-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('product_name', models.CharField(max_length=128)),
                ('recycle_group_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecycleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('group_name', models.CharField(max_length=256)),
                ('group_description', models.TextField(max_length=500)),
            ],
        ),
    ]
