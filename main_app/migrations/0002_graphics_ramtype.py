# Generated by Django 3.2.3 on 2021-05-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphics',
            name='ramType',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
