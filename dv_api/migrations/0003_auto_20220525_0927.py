# Generated by Django 3.2.13 on 2022-05-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dv_api', '0002_auto_20220511_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerdetails',
            name='container_owner',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='containerdetails',
            name='valid_container',
            field=models.BooleanField(default=True),
        ),
    ]
