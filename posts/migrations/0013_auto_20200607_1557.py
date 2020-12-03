# Generated by Django 2.2 on 2020-06-07 15:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200603_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
