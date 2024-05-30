# Generated by Django 5.0.6 on 2024-05-30 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed', models.BooleanField(default=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.role')),
            ],
            options={
                'unique_together': {('role', 'permission')},
            },
        ),
    ]
