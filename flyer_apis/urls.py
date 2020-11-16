from django.urls import path
from rest_framework import routers
from .views import FlyerViewSet

router = routers.SimpleRouter()

router.register(r'', FlyerViewSet, basename='FlyerModel')
# router.register(r'<int:id>', FlyerViewSet.)

urlpatterns = router.urls


# urlpatterns = [
# 	# path('', Flyer),
# 	path('<int:id>', Flyer),
# ]