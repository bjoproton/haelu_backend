from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

