# Generated by Django 4.0.5 on 2022-06-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_remove_classinfo_class_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinfo',
            name='cid',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]