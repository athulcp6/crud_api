# Generated by Django 4.1 on 2023-09-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=220)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
