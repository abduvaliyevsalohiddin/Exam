# Generated by Django 5.0 on 2023-12-29 05:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Haydovchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('kiritilgan_sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=30)),
                ('narx', models.PositiveSmallIntegerField()),
                ('litr', models.PositiveSmallIntegerField()),
                ('batafsil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('ish_vaqti', models.CharField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('manzil', models.CharField(max_length=50)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('umumiy_narx', models.PositiveIntegerField(default=0)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('haydovchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.haydovchi')),
                ('mijoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mijoz')),
                ('suv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.suv')),
            ],
        ),
    ]
