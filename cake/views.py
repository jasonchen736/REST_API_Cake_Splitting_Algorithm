import json

from django.forms.models import model_to_dict
from django.views.generic import View

from .models import Cake
from .utils import compose_response, get_smallest_repeating_segment, validate_cake_pattern


class CakeView(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        cakes = list(Cake.objects.all().values())
        return compose_response(200, data=cakes)

    def post(self, request):
        data = json.loads(request.body)

        validation_results = validate_cake_pattern(data)
        if validation_results.errors:
            return compose_response(400, data=validation_results.errors)

        cake_pattern = data.get('cake')
        found = Cake.objects.filter(pattern=cake_pattern)
        if found:
            return compose_response(409, message='duplicate cake')

        smallest_repeating_segment, smallest_repeating_segment_size, repetitions = \
            get_smallest_repeating_segment(cake_pattern)

        cake = Cake(
            pattern=cake_pattern,
            size=len(cake_pattern),
            smallest_repeating_segment=smallest_repeating_segment,
            smallest_repeating_segment_size=smallest_repeating_segment_size,
            repetitions=repetitions,
        )
        cake.save()

        return compose_response(200, data=model_to_dict(cake))


class CakeDetailView(View):
    http_method_names = ['get', 'put', 'delete']

    def get_object(self, id):
        try:
            return Cake.objects.get(pk=id)
        except Cake.DoesNotExist:
            return None

    def get(self, request, id):
        cake = self.get_object(id)

        if not cake:
            return compose_response(404, message="not found")

        return compose_response(200, data=model_to_dict(cake))

    # create or update cake pattern under cake id
    def put(self, request, id):
        cake = Cake(id=id)

        data = json.loads(request.body)

        validation_results = validate_cake_pattern(data)
        if validation_results.errors:
            return compose_response(400, data=validation_results.errors)

        cake_pattern = data.get('cake')
        if cake.pattern != cake_pattern:
            found = Cake.objects.filter(pattern=cake_pattern)
            if found:
                return compose_response(409, message='duplicate cake')
            else:
                smallest_repeating_segment, smallest_repeating_segment_size, repetitions = \
                    get_smallest_repeating_segment(cake_pattern)

                cake.pattern = cake_pattern
                cake.size = len(cake_pattern)
                cake.smallest_repeating_segment = smallest_repeating_segment
                cake.smallest_repeating_segment_size = smallest_repeating_segment_size
                cake.repetitions = repetitions
                cake.save()

        return compose_response(200, data=model_to_dict(cake))

    def delete(self, request, id):
        cake = self.get_object(id)
        cake.delete()
        return compose_response(200, message="deleted")
