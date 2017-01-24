class CardsService:
    """
    A singleton service providing methods for working with cards
    """
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(CardsService, cls)
        return cls._singleton