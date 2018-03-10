"""Visits factories."""

import random
import factory
import factory.django
from django.contrib.auth import get_user_model
from django.utils import timezone
from . import models

User = get_user_model()


class PlaceFactory(factory.DjangoModelFactory):
    """Place object factory."""

    class Meta:  # noqa
        model = models.Place
        exclude = ('_description',)

    name = factory.Faker('company', locale='fr')
    address = factory.Faker('address', locale='fr')
    _description = factory.Faker('paragraphs', nb=3, locale='fr')
    description = factory.LazyAttribute(lambda o: '\n'.join(o._description))


class VisitFactory(factory.DjangoModelFactory):
    """Visit object factory."""

    date_random_range = (-20, 30)
    deadline_random_range = (-5, -1)

    class Meta:  # noqa
        model = models.Visit
        exclude = ('date_random_range', 'deadline_random_range',
                   '_summary', '_description')

    title = factory.Faker('sentence', locale='fr')
    _summary = factory.Faker('sentences', nb=2, locale='fr')
    summary = factory.LazyAttribute(lambda o: ' '.join(o._summary))
    _description = factory.Faker('paragraphs', nb=5, locale='fr')
    description = factory.LazyAttribute(lambda o: '\n'.join(o._description))

    @factory.lazy_attribute
    def place(self):
        places = models.Place.objects.all()
        # return an existing place in 30% of cases
        if places and random.random() < .3:
            return random.choice(places)
        # otherwise create a new place
        return PlaceFactory.create()

    @factory.lazy_attribute
    def date(self):
        return timezone.now() + timezone.timedelta(
            days=random.randint(*self.date_random_range))

    @factory.lazy_attribute
    def deadline(self):
        return self.date + timezone.timedelta(
            days=random.randint(*self.deadline_random_range))


class VisitWithOpenRegistrationsFactory(VisitFactory):
    """Visit with open registrations object factory."""

    date_random_range = (10, 30)


class VisitWithClosedRegistrationsFactory(VisitFactory):
    """Visit with closed registrations object factory."""

    date_random_range = (0, 5)
    deadline_random_range = (-10, -6)  # guaranteed to be before today


class VisitParticipantFactory(factory.DjangoModelFactory):
    """Visit participant object factory.

    Users and visit are picked from pre-existing objects,
    instead of being created from scratch.
    This means the database must have at least one user and one visit to
    create a VisitParticipant object.
    """

    class Meta:  # noqa
        model = models.VisitParticipant

    @factory.lazy_attribute
    def user(self):
        return random.choice(User.objects.all())

    @factory.lazy_attribute
    def visit(self):
        visits_without_participants = (
            models.Visit.objects.filter(participants=None)
        )
        return random.choice(visits_without_participants)

    present = factory.LazyFunction(lambda: random.choice([None, False, True]))
    accepted = factory.LazyFunction(lambda: random.choice([None, False, True]))