# Generated by Django 4.0.5 on 2022-06-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_classinfo_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinfo',
            name='class_des2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
