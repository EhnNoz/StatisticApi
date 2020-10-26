from django.db import models
from django.utils.translation import ugettext_lazy as _



class System(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    url = models.CharField(verbose_name=_('Url'), max_length=200, blank=False, null=False, unique=True)
    admin_tel = models.CharField(verbose_name=_('Admin Tel'), max_length=200, blank=False, null=False, unique=True)
    admin_email = models.CharField(verbose_name=_('Admin Email'), max_length=200, blank=False, null=False, unique=True)
    token = models.CharField(verbose_name=_('Token'), max_length=32, blank=False, null=False, unique=True)
    class Meta:
        verbose_name = _('System')
        verbose_name_plural = _('Systems')

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    
    
    
class Session(models.Model):
    system = models.ForeignKey(System, verbose_name=_('System'), on_delete=models.SET_NULL, null=True)
    user_id = models.CharField(verbose_name=_('User Id'), max_length=200, blank=True, null=True)
    ip = models.CharField(verbose_name=_('IP'), max_length=200, blank=True, null=True)
    user_agent = models.CharField(verbose_name=_('User Agent'), max_length=200, blank=True, null=True)
    referer = models.CharField(verbose_name=_('Referer'), max_length=200, blank=True, null=True)
    xReferer = models.CharField(verbose_name=_('XReferer'), max_length=200, blank=True, null=True)
    start_time = models.DateTimeField(verbose_name=_('Start Time'), auto_now_add=True)
    End_time = models.DateTimeField(verbose_name=_('End Time'), blank=True, null=True)

    class Meta:
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')

    def __str__(self):
        return self.user_id

    def __unicode__(self):
        return self.user_id



class Activity(models.Model):
    session = models.ForeignKey(Session, verbose_name=_('Session'), on_delete=models.SET_NULL, null=True)
    channel_id = models.CharField(verbose_name=_('Channel Id'), max_length=200, blank=True, null=True)
    content_id = models.CharField(verbose_name=_('Content Id'), max_length=200, blank=True, null=True)
    content_type_id = models.CharField(verbose_name=_('Content Type Id'), max_length=200, blank=True, null=True)
    service_id = models.CharField(verbose_name=_('Service Id'), max_length=200, blank=True, null=True)
    action_id = models.CharField(verbose_name=_('Action Id'), max_length=200, blank=True, null=True)
    time_code = models.CharField(verbose_name=_('Time Code'), max_length=200, blank=True, null=True)


    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.channel_id

    def __unicode__(self):
        return self.channel_id