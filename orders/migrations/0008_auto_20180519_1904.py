# Generated by Django 2.0.4 on 2018-05-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180509_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('created', 'Created')], default='created', max_length=60),
        ),
    ]
