# Generated by Django 4.2.16 on 2024-11-29 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_password_hash_user_salt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="password_hash",
        ),
        migrations.RemoveField(
            model_name="user",
            name="salt",
        ),
    ]
