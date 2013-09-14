import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import View, TemplateView

from utils import json_response


class IndexView(TemplateView):
    template_name = 'wwars/index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class ThreadView(View):
    def post(self, request, *args, **kwargs):
        pass

