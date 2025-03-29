from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from django_bootstrap5.templatetags.django_bootstrap5 import bootstrap_alert, bootstrap_button
from django_bootstrap5.forms import render_form
from django.contrib.auth import get_user

def environment(**options):
    env = Environment(**options)

    def get_user_from_request(request):
        return get_user(request)

    # Добавляем глобальные функции Bootstrap5
    env.globals.update({
        'static': static,
        'url': reverse,
        'bootstrap_alert': bootstrap_alert,
        'bootstrap_button': bootstrap_button,
        'bootstrap_form': render_form,
        'csrf_token': lambda request: request.META.get('CSRF_COOKIE', ''),
        'user': lambda request: get_user_from_request(request),
    })

    return env