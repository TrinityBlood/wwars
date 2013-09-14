from django.views.generic.base import View
from utils.mixins import JSONResponseMixin

from turn.models import Turn


class SituationView(View, JSONResponseMixin):
    def post(self, request, *args, **kwargs):
        turn = Turn.objects.latest('pk')
        return self.render_to_json_response(
            context={
                'turn_id': turn.id,

            },
            **kwargs
        )