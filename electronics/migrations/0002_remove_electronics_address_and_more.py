# Generated by Django 4.2.6 on 2025-01-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronics',
            name='address',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='email',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='grade',
        ),
        migrations.AddField(
            model_name='electronics',
            name='price',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
