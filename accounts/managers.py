from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone, username, fullname=None, email=None, password=None):
        if not phone:
            raise ValueError(_("کاربر باید شماره همراه داشته باشد"))
        elif not username:
            raise ValueError(_("کاربر باید نام کاربری داشته باشد"))

        user = self.model(
            phone=phone,
            username=username,
            fullname=fullname,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, fullname=None, email=None, password=None):
        user = self.create_user(
            phone=phone,
            username=username,
            fullname=fullname,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
