from django.db import models
from django.core.exceptions import ValidationError

from crim.models.genre import CRIMGenre
from crim.models.person import CRIMPerson
from crim.models.role import CRIMRole

import re


class CRIMMass(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Mass'
        verbose_name_plural = 'Masses'

    mass_id = models.CharField(
        'Mass ID',
        max_length=16,
        unique=True,
        primary_key=True,
        db_index=True,
    )
    genre = models.ForeignKey(
        CRIMGenre,
        on_delete=models.SET_NULL,
        to_field='genre_id',
        null=True,
        default=CRIMGenre(genre_id='mass')
    )
    title = models.CharField(max_length=64)
    people = models.ManyToManyField(
        CRIMPerson,
        through='CRIMRole',
        through_fields=('mass', 'person'),
    )

    remarks = models.TextField('remarks (supports Markdown)', blank=True)

    def title_with_id(self):
        return self.__str__()
    title_with_id.short_description = 'mass'
    title_with_id.admin_order_field = 'title'

    def creator(self):
        roles = CRIMRole.objects.filter(mass=self).order_by('date_sort')
        if roles:
            return roles[0].person
    creator.short_description = 'creator'

    def date(self):
        roles = CRIMRole.objects.filter(mass=self).order_by('date_sort')
        if roles:
            return roles[0].date_sort
    date.short_description = 'date'

    def save(self, *args, **kwargs):
        self.genre = CRIMGenre(genre_id='mass')
        super().save()

    def clean(self):
        valid_regex = re.compile(r'^[-_0-9a-zA-Z]+$')
        if not valid_regex.match(self.mass_id):
            raise ValidationError('The Mass ID must consist of letters, numbers, hyphens, and underscores.')

    def __str__(self):
        return '[{0}] {1}'.format(self.mass_id, self.title)
