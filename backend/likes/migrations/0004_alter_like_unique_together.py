# Generated by Django 5.0.6 on 2024-05-27 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_alter_like_table'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]
