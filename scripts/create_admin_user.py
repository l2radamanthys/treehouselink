import os
import sys
import django


sys.path.append("..")
sys.path.append(".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


from django.contrib.auth.models import User


User.objects.create_superuser(
    username="admin", password="asdasd123", email="admin@admin.com"
)