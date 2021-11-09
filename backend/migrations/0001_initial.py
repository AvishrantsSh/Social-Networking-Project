# Generated by Django 3.2.9 on 2021-11-08 17:37

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(blank=True, max_length=25, null=True)),
                ("birth_date", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=1,
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "session_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("login_status", models.BooleanField(default=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "post_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("likes", models.PositiveIntegerField()),
                ("shares", models.PositiveIntegerField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                ("timestamp", models.DateTimeField(auto_created=True)),
                (
                    "message_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                (
                    "recepient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rec_id",
                        to="backend.users",
                    ),
                ),
                (
                    "sender_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_id",
                        to="backend.users",
                    ),
                ),
            ],
        ),
    ]
