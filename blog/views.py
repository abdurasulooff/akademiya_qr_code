from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Items, Fakultet
import segno
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.conf import settings
import os

class ItemsListView(ListView):
    model = Items
    template_name = 'home.html'
    context_object_name = 'items_list'

class ItemsDetailView(DetailView):
    model = Items
    template_name = 'detail.html'
    context_object_name = 'item'

class ItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = Items
    template_name = 'update.html'
    context_object_name = 'item_update'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']

class ItemsDeleteView(LoginRequiredMixin, DeleteView):
    model = Items
    template_name = 'delete.html'
    context_object_name = 'item_delete'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']
    success_url = reverse_lazy('home')

class ItemsCreateView(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'create.html'
    context_object_name = 'item_create'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']


@csrf_protect
def items_detail(request, pk):
    item = get_object_or_404(Items, pk=pk)

    # Generate QR code
    qrcode = segno.make_qr(f"http://172.16.223.227/{pk}")
    
    # Save QR code to file
    qrcode_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{pk}.png')
    qrcode.save(qrcode_path, scale=5, dark="darkblue")

 
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
