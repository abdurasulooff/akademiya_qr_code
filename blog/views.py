from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Items
import segno
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.conf import settings
import os


# class ItemsListView(ListView):
#     model = Items
#     template_name = 'home.html'
#     context_object_name = 'items_list'

class ItemsListView(View):
    def get(self, request, *args, **kwargs):
        items = Items.objects.all()
        context = {'items_list': items}

        return render(request, 'home.html', context)

@csrf_protect
def items_detail(request, pk):
    item = get_object_or_404(Items, pk=pk)

    # Generate QR code
    qrcode = segno.make_qr(f"http://172.16.223.227/{pk}")

    # # Save QR code to file
    # qrcode_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{pk}.png')
    # qrcode.save(qrcode_path, scale=5, dark="darkblue")
    #

    # Get QR code data URI for display
    qr_code_svg = qrcode.svg_data_uri(scale=5)

    context = {
        "item": item,
        "qrcode": qr_code_svg,
    }
    return render(request, 'detail.html', context)

def download_qr_code(request, pk):
    # Get path to the QR code file
    qrcode_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{pk}.png')

    # Open the file
    with open(qrcode_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="{pk}.png"'
        return response

