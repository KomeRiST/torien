# Generated by Django 2.1.3 on 2018-12-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torien', '0003_kategorything_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='kategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torien.KategoryThing'),
            preserve_default=False,
        ),
    ]
