# core/views.py

from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from .models import Firm, District
from .forms import FirmForm, FirmSoftDeleteForm

@login_required
def portal_view(request):
    context = {}
    return render(request, 'portal.html', context)

@permission_required('core.view_firm', raise_exception=True)
def firm_list_view(request):
    show_deleted = request.GET.get('show_deleted')
    if show_deleted:
        firms = Firm.objects.filter(delete__isnull=False)
        list_title = "Silinmiş Firmalar"
    else:
        firms = Firm.objects.filter(delete__isnull=True)
        list_title = "Aktif Firmalar"
    context = {
        'firms': firms,
        'list_title': list_title,
        'is_showing_deleted': bool(show_deleted)
    }
    return render(request, 'firm_list.html', context)

@permission_required('core.add_firm', raise_exception=True)
def firm_create_view(request):
    form = FirmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('core:firm-list')
    return render(request, 'firm_form.html', {'form': form})

@permission_required('core.change_firm', raise_exception=True)
def firm_update_view(request, pk):
    firm = get_object_or_404(Firm, pk=pk)
    form = FirmForm(request.POST or None, request.FILES or None, instance=firm)
    if form.is_valid():
        form.save()
        return redirect('core:firm-list')
    return render(request, 'firm_form.html', {'form': form})

@permission_required('core.delete_firm', raise_exception=True)
def firm_delete_view(request, pk):
    firm = get_object_or_404(Firm, pk=pk)
    if request.method == 'POST':
        form = FirmSoftDeleteForm(request.POST)
        if form.is_valid():
            firm.delete = form.cleaned_data['delete_date'] 
            firm.save()
            return redirect('core:firm-list')
    else:
        form = FirmSoftDeleteForm()
    return render(request, 'firm_confirm_delete.html', {'firm': firm, 'form': form})

def load_districts(request):
    city_id = request.GET.get('city_id')
    districts = District.objects.filter(city_id=city_id).order_by('name')
    return JsonResponse(list(districts.values('id', 'name')), safe=False)