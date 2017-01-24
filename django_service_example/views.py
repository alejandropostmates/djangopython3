from django.http import HttpResponse
from .services.cards_service import CardsService


# Create your views here.
def index(request):
    cards = CardsService().fetch_cards()
    return HttpResponse(cards)