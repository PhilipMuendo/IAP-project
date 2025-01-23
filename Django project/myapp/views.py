from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm  


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event_detail.html', {'event': event})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving event...")
            form.save()  
            return redirect('event_list') 
        else:
            print("Form is not valid")
    else:
        form = EventForm()  
    
    return render(request, 'create_event.html', {'form': form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('event_list')