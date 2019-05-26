# Create your views here.

from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST


@require_POST
def login_check(request):
    user_name = request.POST.get("account", "")
    password = request.POST.get("password", "")


@require_GET
def logout(request): pass
