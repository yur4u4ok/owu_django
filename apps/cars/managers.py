from django.db.models import QuerySet


class CarManager(QuerySet):
    def get_auto_park_by_id(self, id):
        return self.filter(auto_park_id=id)
