# Generated by Django 2.2.10 on 2021-07-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_jury'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sujet', models.CharField(max_length=150)),
                ('Avis', models.CharField(max_length=150)),
                ('MotsCles', models.CharField(max_length=150)),
            ],
        ),
    ]