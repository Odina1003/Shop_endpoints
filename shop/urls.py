from .views import Purchases
from .customer import Customers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('auth', Customers, basename='auth')
router.register('purchas', Purchases, basename='purchas')
urlpatterns = router.urls 