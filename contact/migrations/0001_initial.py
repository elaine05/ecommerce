# Generated by Django 2.0.4 on 2018-05-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('message', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
