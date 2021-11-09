from uuid import uuid4

from django.db import models

GENDER_CHOICE = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others"),
)


class Users(models.Model):
    user_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user_email = models.EmailField(null=False, blank=False)
    password = models.CharField(null=False, blank=False, max_length=20)
    first_name = models.CharField(null=False, blank=False, max_length=25)
    last_name = models.CharField(null=True, blank=True, max_length=25)
    birth_date = models.DateField(null=False)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=1, null=False, blank=False
    )
    bio = models.TextField(null=True, blank=True)


class Session(models.Model):
    session_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    login_status = models.BooleanField(default=True)


class Messages(models.Model):
    message_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    sender_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="sender_id"
    )
    recepient_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="rec_id"
    )
    content = models.CharField(null=False, blank=False, max_length=200)
    timestamp = models.DateTimeField(auto_created=True)


class Posts(models.Model):
    post_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.CharField(null=False, blank=False, max_length=200)
    likes = models.PositiveIntegerField()
    shares = models.PositiveIntegerField()
