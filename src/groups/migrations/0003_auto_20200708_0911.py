# Generated by Django 3.0.7 on 2020-07-08 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20200706_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link',
            new_name='url',
        ),
    ]
