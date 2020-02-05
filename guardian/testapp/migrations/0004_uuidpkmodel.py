# Generated by Django 3.0.3 on 2020-02-05 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20190611_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDPKModel',
            fields=[
                ('uuid_pk', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
