# Generated by Django 4.0.5 on 2022-06-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_remove_classinfo_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinfo',
            name='cid',
            field=models.IntegerField(null=True),
        ),
    ]