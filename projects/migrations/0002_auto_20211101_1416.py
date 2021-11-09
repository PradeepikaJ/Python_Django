# Generated by Django 3.2.8 on 2021-11-01 08:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.UUID('324f8d49-d2ab-4492-9921-ea7ba86f4527'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('358877e3-e55d-4791-a6de-606c2851763a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8de8b0e1-916f-4699-9f2d-63cf80c4ca9b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
