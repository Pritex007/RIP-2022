# Generated by Django 4.1.2 on 2022-10-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>'),
        ),
    ]
