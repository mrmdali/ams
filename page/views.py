from django.shortcuts import render, redirect
from .models import Service, Advantage, Counter, Contact
from .forms import ContactForm


def home(request):
    services = Service.objects.all().order_by('-id')
    advantages = Advantage.objects.all().order_by('-id')
    counters = Counter.objects.all().order_by('-id')
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST or None)
        if contact.is_valid():
            contact.save()
            return redirect('/')

    context = {
        'services': services,
        'advantages': advantages,
        'counters': counters,
        'contact': contact,
    }
    return render(request, 'page/index.html', context)