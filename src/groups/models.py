"""
API models (Group, Link)
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser

from .utils import CustomUserManager


class CustomUser(AbstractBaseUser):
    """
    Custom user model
    """
    username = models.CharField(
        'username',
        max_length=150,
        null=True,
        blank=True
    )  # , unique=True)
    email = models.EmailField(
        'email address',
        unique=True
    )
    google_token = models.TextField(
        null=True,
        blank=True
    )  # unique=True
    # is_active = True  # inherited
    # is_active = models.BooleanField(
    #     'active',
    #     default=False,
    #     help_text=_(
    #         'Designates whether this user should be treated as active. '
    #         'Unselect this instead of deleting accounts.'
    #     ),
    # )
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        'date joined',
        default=timezone.now
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    class Meta:
        db_table = 'custom_users'

    def __str__(self):
        return f'Custom user - {self.email}'

    # 3 метода внизу треба для адмінки (вона їх шототам вимагає)
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


class Group(models.Model):
    """
    Group model
    Represents group of links (like folder)
    """
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        verbose_name="Group's owner",
        related_name="groups",
        null=True  # may be a problem because of unique_together
    )
    name = models.CharField(
        verbose_name="Group's name",
        max_length=150,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name="Additional group description",
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name='Timestamp when group was created',
        auto_now_add=True
    )

    # color
    # position (drag and drop)

    class Meta:
        db_table = 'groups'
        unique_together = [
            ['name', 'owner']
        ]

    def __str__(self):
        return f'Group: {self.name=}'


class Link(models.Model):
    """
    Link model
    Represents link to source (now it's only video on youtube)
    """
    url = models.URLField(
        verbose_name="Link to the source (video / article / ...)"
    )
    description = models.TextField(
        verbose_name='Description about link'
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name="Many to many relationship with group",
        related_name="links",
    )
    is_done = models.BooleanField(
        verbose_name="Flag that indicates whether user's finished processing source by link",
        default=False
    )
    added = models.DateTimeField(
        verbose_name="Timestamp when link was added",
        auto_now_add=True
    )

    # position (drag and drop)

    class Meta:
        db_table = 'links'

    def __str__(self):
        return f'Link: {self.url}'
