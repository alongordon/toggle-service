# Generated by Django 2.0 on 2020-10-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventit', '0010_auto_20190518_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='count_1_sign_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='count_2_sign_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='count_3_sign_off',
            field=models.BooleanField(default=False),
        ),
    ]