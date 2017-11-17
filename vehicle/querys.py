from __future__ import unicode_literals
from django.db.models.query import QuerySet


class DriversQuerySet(QuerySet):
    def get_driver_by_city(self, city):
        return self.filter(city__state=city)

    def get_driver_by_school(self, school):
        return self.filter(school__nameschool=school)


