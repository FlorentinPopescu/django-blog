# Generated by Django 3.0.4 on 2020-04-20 02:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20200318_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
