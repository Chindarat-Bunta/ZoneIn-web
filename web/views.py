import sys
import traceback
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import django


def home(request):
    try:
        context = {
            "is_vercel": getattr(settings, "IS_VERCEL", False),
            "debug": settings.DEBUG,
            "django_version": django.get_version(),
        }
        return render(request, "web/index.html", context)
    except Exception as e:
        tb_text = traceback.format_exc()
        return HttpResponse(
            f"<h2>Error inside home view:</h2><pre style='white-space: pre-wrap; font-family: monospace; font-size: 14px;'>{tb_text}</pre>",
            status=500,
        )


def custom_500(request):
    type_, value, tb = sys.exc_info()
    tb_text = "".join(traceback.format_exception(type_, value, tb))
    return HttpResponse(
        f"<h2>Django 500 Server Error:</h2><pre style='white-space: pre-wrap; font-family: monospace; font-size: 14px;'>{tb_text}</pre>",
        status=500,
    )

