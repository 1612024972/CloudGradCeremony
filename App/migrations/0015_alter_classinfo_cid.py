# Generated by Django 4.0.5 on 2022-06-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_classinfo_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='cid',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]