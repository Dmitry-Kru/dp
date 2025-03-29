from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from django_bootstrap5.templatetags.django_bootstrap5 import bootstrap_alert, bootstrap_button
from django_bootstrap5.forms import render_form
from django.contrib.auth import get_user
from django.middleware.csrf import get_token
from django.template.defaulttags import csrf_token

def environment(**options):
    env = Environment(**options)

    def get_user_from_request(request):
        return get_user(request)

    def get_csrf():
        from django.conf import settings
        if not settings.configured:
            settings.configure()
        request = type('Request', (), {'META': {}, 'csrf_processing_done': False})()
        return get_token(request)

    # Добавляем глобальные функции Bootstrap5
    env.globals.update({
        'static': static,
        'url': reverse,
        'bootstrap_alert': bootstrap_alert,
        'bootstrap_button': bootstrap_button,
        'bootstrap_form': render_form,
        'csrf_token': csrf_token,
        'user': lambda request: get_user_from_request(request),
    })

    return env