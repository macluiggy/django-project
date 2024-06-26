# Generated by Django 5.0.6 on 2024-05-27 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0006_alter_like_unique_together_like_unique_like'),
        ('posts', '0004_rename_user_id_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post'),
        ),
    ]
