# filepath: /c:/Users/migue/Desktop/estudos diversos/tempof1/f1-laptimes/laptimes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Track, LapTime
from .forms import LapTimeForm

from django.contrib import messages

def home_view(request):
    tracks = Track.objects.all().prefetch_related('lap_times')
    if request.method == 'POST':
        form = LapTimeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lap time added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error adding lap time.')
    else:
        form = LapTimeForm()
    return render(request, 'laptimes/f1_lap_times.html', {'tracks': tracks, 'form': form})

def delete_lap_time(request, lap_time_id):
    lap_time = get_object_or_404(LapTime, id=lap_time_id)
    lap_time.delete()
    messages.success(request, 'Lap time deleted successfully!')
    return redirect('home')