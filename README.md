Django Service Example
======================

## Requirements

* Python 3

## Setup

From the main folder, run migrations and load sample data:

```
python3 ./manage.py migrate
python3 ./manage.py loaddata django_service_example/fixtures/*.json
```

Then run the server:

```
python3 ./manage.py runserver
```

And navigate to the demo endpoint:
http://localhost:8000/cards/

## Example

/cards/

1. URL maps to view in controller
2. Controller calls CardsService method to fetch cards
3. CardsService calls model method to fetch cards
4. Controller calls render function on cards data

## Explanation

When using the MVC pattern, oftentimes the controller or model do too much outside of their domain (model queries, manipulation). By adding a service layer in between the controller and the model, we **separate concerns** better.

Controller → Service → Model

**Controller** - Calls services, decides redirect or render  
**Service** - Works with models to run database queries and process data at a higher level, provides simple flat API for use by controller  
**Model** - Represents database schema  
**Serializer** - Traditionally the "view" in an API, just focuses on how to output data (e.g. JSON)

A controller calls a high-level service method, and merely passes along the resulting data to the serializer, which passes it onto the view. This makes for **thin controllers**.

Any service call that involves multiple models can now simply sit in the service, instead of arbitrarily deciding that a cross-model method belongs in some model.

When testing, one need only test the service layer exposed, leaving the models internal and open to change, much as private methods in Object-Oriented programming.

To test services, one can also simply stub a high-level method, rather than messing with controllers.
