from django.shortcuts import render
from dv_api.models import ContainerDetails
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from datetime import datetime, timedelta
from django.conf import settings


# Create your views here.
class ContainerDetailsView(View):
    http_method_names = ["options", "get"]
    template_name = 'dv_web_app/container.html'

    def get(self, request, *args, **kwargs):
        result = {}
        print(datetime.now() - timedelta(minutes=30))
        container_details_obj = ContainerDetails.objects.last()
        container_details_dict = {
            "container_code": container_details_obj.container_code,
            "ISO_code": container_details_obj.ISO_code,
            "container_size": container_details_obj.container_size,
            "container_type": container_details_obj.container_type,
            "gate": container_details_obj.gate,
            "valid_container": container_details_obj.valid_container,
            "container_owner": container_details_obj.container_owner,
            "image_right": container_details_obj.image_right,
            "image_left": container_details_obj.image_left,
            "image_rear": container_details_obj.image_rear,
            "image_top": container_details_obj.image_top,
            "date_time": container_details_obj.date_time,
            "date": container_details_obj.date
        }
        context = {
            "status": "success",
            "result": container_details_dict
        }
        return render(request, self.template_name, {'form': context})
