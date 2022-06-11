import channels.layers
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from dv_api.models import ContainerDetails


def send_message(event):
    '''
    Call back function to send message to the browser
    '''
    message = event['text']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))


@receiver(post_save, sender=ContainerDetails)
def update_container_details(sender, instance, **kwargs):
    '''
    Sends job status to the browser when a Job is modified
    '''
    group_name = 'container-{}'.format(instance.container_code)

    message = {
        'id': instance.id,
        'container_code': instance.container_code,
        'ISO_code': instance.ISO_code,
        'container_size': instance.container_size,
        'date_time': instance.date_time.isoformat(),
    }

    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )


@receiver(post_save, sender=ContainerDetails)
def update_(sender, instance, **kwargs):
    container_pk = instance.id
    group_name = 'container-{}'.format(container_pk)

    message = {
        'container_code': instance.container_code,
        'ISO_code': instance.ISO_code,
        'container_size': instance.container_size,
        'date_time': instance.date_time.isoformat(),
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )