# Generated by Django 5.0.6 on 2024-05-27 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_user_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
