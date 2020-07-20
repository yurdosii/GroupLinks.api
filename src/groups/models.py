"""
API models (Group, Link)
"""

from django.db import models


class Group(models.Model):
    """
    Group model
    Represents group of links (like folder)
    """
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
        # unique_together = [
        #     ['name', 'user_id']
        # ]

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
