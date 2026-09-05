from django.shortcuts import render
from django.conf import settings
import django


def home(request):
    context = {
        "is_vercel": getattr(settings, "IS_VERCEL", False),
        "debug": settings.DEBUG,
        "django_version": django.get_version(),
    }
    return render(request, "web/index.html", context)

