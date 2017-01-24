from django_service_example.models import Card

class CardsService:
    """
    A singleton service providing methods for working with cards
    """
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(CardsService)
        return cls.singleton

    def fetch_cards(self):
        return Card.objects.all()

