# Generated by Django 3.0.7 on 2020-07-28 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to=settings.AUTH_USER_MODEL, verbose_name="Group's owner"),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'owner')},
        ),
    ]
