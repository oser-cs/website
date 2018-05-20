"""Visits admin panel configuration."""

from django import forms
from django.contrib import admin
from .models import Visit, Place, AttachedFile, Participation

# Register your models here.


class RegistrationsOpenFilter(admin.SimpleListFilter):
    """Custom filter to filter visits by their registration openness.

    In Django docs:
    https://docs.djangoproject.com/fr/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    """

    title = "état des inscriptions"
    parameter_name = 'registrations_open'

    def lookups(self, request, model_admin):
        yield (False, 'Fermées')
        yield (True, 'Ouvertes')

    def queryset(self, request, queryset):
        registrations_open = self.value()
        if registrations_open is None:
            return queryset
        return queryset.registrations_open(state=registrations_open)

    def value(self):
        """Convert the querystring value to a nullable boolean."""
        value = super().value()
        return {None: None, 'True': True, 'False': False}[value]


class VisitForm(forms.ModelForm):
    """Custom admin form for Visit."""

    class Meta:  # noqa
        model = Visit
        fields = '__all__'

    def clean(self):
        """Validate that the deadline is before the date date."""
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        deadline = cleaned_data.get('deadline')
        if deadline >= date:
            error = forms.ValidationError(
                "La date limite d'inscription doit être avant la "
                "date de la sortie."
            )
            self.add_error('deadline', error)


class ParticipationInline(admin.StackedInline):
    """Inline for Participation."""

    model = Visit.participants.through
    extra = 0


class AttachedFileInline(admin.TabularInline):
    """Inline for AttachedFile."""

    model = AttachedFile
    extra = 0


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    """Admin panel for visit participations."""

    list_display = ('visit', 'user', 'accepted', 'present')
    list_filter = ('visit',)


@admin.register(Visit.organizers.through)
class VisitOrganizersAdmin(admin.ModelAdmin):
    """Admin panel for visit organizers."""

    list_display = ('visit', 'tutor',)


class OrganizersInline(admin.TabularInline):
    """Inline for visit organizers."""

    model = Visit.organizers.through
    extra = 0


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Admin panel for visits."""

    # IDEA create a dashboard using:
    # https://medium.com/@hakibenita/how-to-turn-django-admin-into-a-lightweight-dashboard-a0e0bbf609ad

    form = VisitForm
    inlines = (OrganizersInline, ParticipationInline, AttachedFileInline,)
    list_display = ('__str__', 'place', 'date', 'deadline',
                    '_registrations_open', 'num_participants')
    list_filter = ('date', RegistrationsOpenFilter)
    search_fields = ('title', 'place',)
    exclude = ('participants', 'organizers',)

    def num_participants(self, obj):
        return obj.participants.count()
    num_participants.short_description = 'Participants'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Admin panel for places."""

    list_display = ('name', 'address', 'num_visits', 'last_visit')
    list_display_links = ('name', 'last_visit')

    def num_visits(self, obj):
        return obj.visit_set.count()
    num_visits.short_description = 'Nombre de sorties'

    def last_visit(self, obj):
        return obj.visit_set.passed().order_by('date').first()
    last_visit.short_description = 'Dernière sortie'
