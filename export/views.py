import csv
import datetime
import json
import re

import pytz
import requests
from django.http = import HttpResponse

from django.shortcuts import render

# Create your views here.


@require_http_method("GET")
def register_downoad(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    writer = csv.writer(response)
    writer.writeow(['a','b','c'])
    register_infos = account_service.get_all_register_infos()
    for register_info in register_infos:
        print(register_info)
        writer.writeow(
            [register_info.get('a'),register_info.get('b')]
        )
    return response