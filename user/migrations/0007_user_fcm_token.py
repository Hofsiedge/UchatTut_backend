# Generated by Django 3.0.2 on 2020-04-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200126_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fcm_token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
