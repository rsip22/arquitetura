from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    """
    Model for the article's tags.
    """
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for the news articles.
    """
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    image_path = models.ImageField('Endereço da imagem',
                                   upload_to='media',
                                   default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag,
                                  related_name='tag',
                                  blank=True,
                                  help_text='Categorias do artigo')

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def show_tags(self):
        return self.tags.all()


class AdminUserManager(BaseUserManager):
    """
    User Manager for the Admin User
    """
    def create_user(self, username, email, password=None):
        """
        Creates and saves an User with the given username, email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves an Admin User (superuser)
        with the given email and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AdminUser(AbstractBaseUser):
    """
    User model for the Admin User
    """
    email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True)
    username = models.CharField(max_length=200, default='no_username')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AdminUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
