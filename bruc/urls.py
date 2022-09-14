
from django.urls import path, include

from rest_framework import routers
from .views import ContactViewSet, GuestsViewSet, TagsViewSet, UsersViewSet, LineupViewSet, SponsorsViewSet

router = routers.DefaultRouter()
router.register('guests', GuestsViewSet)
router.register('tags', TagsViewSet)
router.register('users', UsersViewSet)
router.register('lineup', LineupViewSet)
router.register('sponsors', SponsorsViewSet)
router.register('contact', ContactViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]