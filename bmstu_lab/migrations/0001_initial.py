# Generated by Django 4.1.2 on 2022-10-09 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Марка')),
                ('country', models.CharField(max_length=150, verbose_name='Страна производителя')),
            ],
        ),
        migrations.CreateModel(
            name='Drives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Привод')),
            ],
        ),
        migrations.CreateModel(
            name='Engine_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Тип двигателя')),
            ],
        ),
        migrations.CreateModel(
            name='Gearboxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Корбка передач')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название модели')),
                ('price', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bmstu_lab.brands')),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bmstu_lab.drives')),
                ('engine_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bmstu_lab.engine_types')),
                ('gearbox', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bmstu_lab.gearboxes')),
            ],
        ),
    ]
