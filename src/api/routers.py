from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('stateViewset', StateViewset, basename='stateViewset')
router.register('cityViewset', CityViewset, basename='cityViewset')
router.register('customViewset', CustomViewset, basename='customViewset')
router.register('detailOrderViewset', DetailOrderViewset, basename='detailOrderViewset')
router.register('locationViewset', LocationViewset, basename='locationViewset')
router.register('ordersViewset', OrdersViewset, basename='ordersViewset')
router.register('paymentViewset', PaymentViewset, basename='paymentViewset')
router.register('productViewset', ProducViewset, basename='productViewset')
router.register('reviewViewset', ReviewViewset, basename='reviewViewset')
router.register('sellerViewset', SellerViewset, basename='sellerViewset')
router.register('zipCodeViewset', ZipCodeViewset, basename='zipCodeViewset')

urlpatterns = router.urls