from django.shortcuts import render
from .models import Portfolio, Testimonial


# Create your views here.
def home(request):
    portfolio_items = Portfolio.objects.all
    all_testimonials = Testimonial.objects.all
    return render(request, 'index.html', {'portfolio_items': portfolio_items, 'all_testimonials': all_testimonials})


def portfolio_details(request, portfolio_item_id):
    portfolio_item = Portfolio.objects.get(id=portfolio_item_id)
    return render(request, 'portfolio-details.html', {'portfolio_item': portfolio_item})