from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from difflib import SequenceMatcher
from .models import ContainerDetails
from datetime import datetime


class AddContainerDetailsView(View):
    http_method_names = ["options", "post", "put"]

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(AddContainerDetailsView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        result = {}

        if not request.body:
            return self.get_error_response(
                {"message": "request body is empty"})
        request_body = json.loads(request.body)

        container_code = request_body.get("container_code")
        ISO_code = request_body.get("ISO_code")
        container_size = request_body.get("container_size")
        container_type = request_body.get("container_type")
        gate = request_body.get('gate')
        container_owner = request_body.get("container_owner")
        image_right = request_body.get("image_right")
        image_left = request_body.get("image_left")
        image_rear = request_body.get("image_rear")
        image_top = request_body.get("image_top")
        date_time = request_body.get("date_time")
        date = request_body.get("date")
        valid_container = request_body.get("valid_container")


        if not container_code:
            return self.get_error_response(
                {"message": "container code is required"})
        if not gate:
            return self.get_error_response(
                {"message": "gate type is required"})
        
        # if not image_path:
        #     return self.get_error_response(
        #         {"message": "image path is required"})
        if not date_time:
            return self.get_error_response(
                {"message": "date_time is required"})
        if not date:
            return self.get_error_response(
                {"message": "date is required"})

        container_details_obj, created = ContainerDetails.objects.get_or_create(
            image_left=image_left,
            gate=gate,
            container_code=container_code,
            image_right=image_right,
            image_rear=image_rear,
            image_top=image_top,
            date_time=date_time,
            date=date,
            container_type=container_type,
            container_size=container_size,
            ISO_code=ISO_code,
            valid_container = valid_container,
            container_owner = container_owner
        )
        if not created:
            return self.get_error_response(
                {"message": "container details already exist"})
        result = {
            "status": "success",
            "result": "container details data created successfully"
        }
        return JsonResponse(result, status=200)


    def put_(self, request, *args, **kwargs):
        result = {}

        if not request.body:
            return self.get_error_response(
                {"message": "request body is empty"})
        request_body = json.loads(request.body)

        container_code = request_body.get("container_code")
        ISO_code = request_body.get("ISO_code")
        container_size = request_body.get("container_size")
        container_type = request_body.get("container_type")
        gate = request_body.get('gate')
        container_owner = request_body.get("container_owner")
        image_right = request_body.get("image_right")
        image_left = request_body.get("image_left")
        image_rear = request_body.get("image_rear")
        image_top = request_body.get("image_top")
        date_time = request_body.get("date_time")
        date = request_body.get("date")
        valid_container = request_body.get("valid_container")

        container_details_list = ContainerDetails.objects.filter(
            date=date,
            gate=gate,
            container_code=container_code
        )


        if not container_obj:
            try:
                container_details_obj = ContainerDetails.objects.create(
                image_left=image_left,
                gate=gate,
                container_code=container_code,
                image_right=image_right,
                image_rear=image_rear,
                image_top=image_top,
                date_time=date_time,
                date=date,
                container_type=container_type,
                container_size=container_size,
                ISO_code=ISO_code,
                valid_container = valid_container,
                container_owner = container_owner
                )
            except Exception as e:
                result = {"status": "error",
                "messsage":"Exception while creating new container " + e}
            
            result = {
                "status": "success",
                "result": "container details data created successfully"
            }
            return JsonResponse(result, status=200)
        else:
            container_obj = container_details_list[0]

            if SequenceMatcher(None, container_obj.container_code, container_code).ratio() > 0.65:
                if len(container_code) > len(container_obj.container_code):
                    container_obj.container_code = container_code
                    if len(container_code) == 11 and valid_container:
                        container_obj.valid_container = valid_container

            if not container_obj.ISO_code and ISO_code:
                container_obj.ISO_code = ISO_code
            if not container_obj.container_type and container_type:
                container_obj.container_type = container_type
            if not container_obj.container_size and container_size:
                container_obj.container_size = container_size
            if not container_obj.image_left and image_left:
                container_obj.image_left = image_left
            if not container_obj.image_right and image_right:
                container_obj.image_right = image_right
            if not container_obj.image_rear and image_rear:
                container_obj.image_rear = image_rear
            if not container_obj.image_top and image_top:
                container_obj.image_top = image_top
            if not container_obj.container_owner and container_owner:
                container_obj.container_owner = container_owner

            container_obj.save()


            result = {
                "status": "success",
                "result": "container details data updated successfully"
            }

            return JsonResponse(result, status=200)

    def put(self, request, *args, **kwargs):
        result = {}

        if not request.body:
            return self.get_error_response(
                {"message": "request body is empty"})
        request_body = json.loads(request.body)

        container_code = request_body.get("container_code")
        ISO_code = request_body.get("ISO_code")
        container_size = request_body.get("container_size")
        container_type = request_body.get("container_type")
        gate = request_body.get('gate')
        container_owner = request_body.get("container_owner")
        image_right = request_body.get("image_right")
        image_left = request_body.get("image_left")
        image_rear = request_body.get("image_rear")
        image_top = request_body.get("image_top")
        date_time = request_body.get("date_time")
        date = request_body.get("date")
        valid_container = request_body.get("valid_container")

        # container_details_list = ContainerDetails.objects.filter(
        #     date=date,
        #     gate=gate,
        #     container_code=container_code
        # )

        container_obj = ContainerDetails.objects.last()

        if not container_obj:
            try:
                container_details_obj = ContainerDetails.objects.create(
                image_left=image_left,
                gate=gate,
                container_code=container_code,
                image_right=image_right,
                image_rear=image_rear,
                image_top=image_top,
                date_time=date_time,
                date=date,
                container_type=container_type,
                container_size=container_size,
                ISO_code=ISO_code,
                valid_container = valid_container,
                container_owner = container_owner
                )
            except Exception as e:
                result = {"status": "error",
                "messsage":"Exception while creating new container " + e}
            
            result = {
                "status": "success",
                "result": "container details data created successfully"
            }
            return JsonResponse(result, status=200)
        else:
            # container_obj = container_details_list[0]
            if SequenceMatcher(None, container_obj.container_code, container_code).ratio() > 0.65:
                if len(container_code) > len(container_obj.container_code):
                    container_obj.container_code = container_code
                    if len(container_code) == 11 and valid_container:
                        container_obj.valid_container = valid_container

                if not container_obj.ISO_code and ISO_code:
                    container_obj.ISO_code = ISO_code
                if not container_obj.container_type and container_type:
                    container_obj.container_type = container_type
                if not container_obj.container_size and container_size:
                    container_obj.container_size = container_size
                if not container_obj.image_left and image_left:
                    container_obj.image_left = image_left
                if not container_obj.image_right and image_right:
                    container_obj.image_right = image_right
                if not container_obj.image_rear and image_rear:
                    container_obj.image_rear = image_rear
                if not container_obj.image_top and image_top:
                    container_obj.image_top = image_top
                if not container_obj.container_owner and container_owner:
                    container_obj.container_owner = container_owner

                container_obj.save()
            else:
                try:
                    container_details_obj = ContainerDetails.objects.create(
                    image_left=image_left,
                    gate=gate,
                    container_code=container_code,
                    image_right=image_right,
                    image_rear=image_rear,
                    image_top=image_top,
                    date_time=date_time,
                    date=date,
                    container_type=container_type,
                    container_size=container_size,
                    ISO_code=ISO_code,
                    valid_container = valid_container,
                    container_owner = container_owner
                    )
                except Exception as e:
                    result = {"status": "error",
                    "messsage":"Exception while creating new container " + e}


            result = {
                "status": "success",
                "result": "container details data updated successfully"
            }

            return JsonResponse(result, status=200)

    def get_error_response(self, result, status=400):
        context = {"status": "error", "result": result}
        return JsonResponse(context, status=status)


class GetContainerDetailsView(View):
    http_method_names = ["options", "get"]

    def get(self, request, *args, **kwargs):
        result = {}
        container_code = request.GET.get('container_code', None)
        # date_time = request.GET.get('date_time', None)
        date = request.GET.get('date', None)
        gate = request.GET.get('gate', None)
        valid_container = request.GET.get('valid_container', None)

        if date and valid_container and gate:
            container_details_list = ContainerDetails.objects.filter(
                date=date,
                gate=gate,
                valid_container=valid_container
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif date and valid_container:
            container_details_list = ContainerDetails.objects.filter(
                date=date,
                valid_container=valid_container
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container",  "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date" 
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif valid_container:
            container_details_list = ContainerDetails.objects.filter(
                valid_container=valid_container
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        if not container_code and not date and not gate:   
            container_details = ContainerDetails.objects.all().values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {"status": "success", "result": list(container_details)}
            return JsonResponse(result, status=200, safe=False)
        elif not container_code and not gate and date:   
            # datetime.fromisoformat(date_time)
            container_details_list = ContainerDetails.objects.filter(
                date=date
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif not container_code and gate and date: 
            container_details_list = ContainerDetails.objects.filter(
                date=date,
                gate=gate
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif container_code and not gate and date: 
            # datetime.fromisoformat(date_time)
            container_details_list = ContainerDetails.objects.filter(
                date=date,
                container_code=container_code
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif container_code and not date and not gate: 
            container_details_list = ContainerDetails.objects.filter(
                container_code=container_code
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)
        
        elif container_code and not date and gate: 
            container_details_list = ContainerDetails.objects.filter(
                container_code=container_code,
                gate=gate
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)

        elif not container_code and not date and gate: 
            # datetime.fromisoformat(date_time)
            container_details_list = ContainerDetails.objects.filter(
                gate=gate
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }


        elif container_code and not date and gate:
            # datetime.fromisoformat(date_time)
            container_details_list = ContainerDetails.objects.filter(
                gate=gate,
                container_code=container_code
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }

        elif container_code and date and gate:
            # datetime.fromisoformat(date_time)
            container_details_list = ContainerDetails.objects.filter(
                date=date,
                container_code=container_code,
                gate=gate
            ).values(
                "container_code", "ISO_code", "container_size", "container_type", "gate", "valid_container", "container_owner",
                "image_right", "image_left", "image_rear", "image_top", "date_time", "date"
            )
            result = {
                "status": "success",
                "result": list(container_details_list)
            }
            return JsonResponse(result, status=200, safe=False)
        return JsonResponse(result, status=200)

class GetLastContainerView(View):
    http_method_names = ["options", "get"]

    def get(self, request, *args, **kwargs):
        result = {}
        last_container = ContainerDetails.objects.last()
        response = {
            "container_code": last_container.container_code, 
            "ISO_code": last_container.ISO_code,
            "container_size":last_container.container_size,
            "container_type": last_container.container_type,
            "gate": last_container.gate,
            "date_time": last_container.date_time, 
            "date": last_container.date,
            "valid_container":last_container.valid_container,
            "container_owner":last_container.container_owner,
            "image_right":last_container.image_right,
            "image_left":last_container.image_left,
            "image_rear":last_container.image_rear,
            "image_top":last_container.image_top
            }
        result = {"status": "success", "result": response}
        return JsonResponse(result, status=200)

