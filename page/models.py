from django.db import models
from django.utils.translation import gettext_lazy as _


class Timestamp(models.Model):
    class Meta:
        abstract = True

    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date modified'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))


class Service(Timestamp):
    class Meta:
        verbose_name_plural = _('Services')
        verbose_name = _('Service')

    title = models.CharField(max_length=50, verbose_name=_('Title'))
    image = models.FileField(upload_to='service/icon/', verbose_name=_('Image'))
    description = models.TextField()

    def __str__(self):
        return self.title


class Advantage(Timestamp):
    class Meta:
        verbose_name_plural = _('Advantages')
        verbose_name = _('Advantage')

    title = models.CharField(max_length=50, verbose_name=_('Title'))
    image = models.FileField(upload_to='service/icon/', verbose_name=_('Image'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title


class Counter(Timestamp):
    class Meta:
        verbose_name_plural = _('Counters')
        verbose_name = _('Counter')

    count = models.IntegerField(verbose_name=_('Counter'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    def __str__(self):
        return self.title


class Contact(Timestamp):
    class Meta:
        verbose_name_plural = _('Contacts')
        verbose_name = _('Contact')

    full_name = models.CharField(max_length=100, verbose_name=_('Full name'))
    phone = models.CharField(max_length=100, verbose_name=_('Phone number'))
    type_of_service = models.ForeignKey(Service, verbose_name=_('Service'), on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name

