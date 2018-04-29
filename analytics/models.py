from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .signals import object_viewed_signal
from .utils import get_user_ip

User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=220,  blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed %s".format(self.content_object, self.created)

    class Meta:
        ordering =['-created']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    obj_cls = ContentType.objects.get_for_model(sender)
    new_view_obj = ObjectViewed(
        user = request.user,
        ip_address = get_user_ip(request),
        content_type = obj_cls,
        object_id = instance.id
    )


object_viewed_signal.connect(object_viewed_receiver)
