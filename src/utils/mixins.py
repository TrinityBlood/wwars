import json

from django.http.response import HttpResponse


class NewManualModelIdMixin(object):

    @classmethod
    def new(cls):
        try:
            last_id = cls.objects.latest('id').id + 1
        except cls.DoesNotExist:
            last_id = 0
        return cls(id=last_id)


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        return json.dumps(context)