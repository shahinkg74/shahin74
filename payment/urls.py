from django.urls import path
from .views import (
    CartView,

    CartAddCourseView,
    CartRemoveCourseView,

    OrderCreateView,
    OrderDetailView,

    SendRequestView,
    VerifyView
)

app_name = 'payment'
cart_urlpatterns = [
    path('cart/add/<int:course_id>/', CartAddCourseView.as_view(), name='cart_add_course'),
    path('cart/remove/<int:course_id>/', CartRemoveCourseView.as_view(), name='cart_remove_course'),
]
order_urlpatterns = [
    path('order/create/', OrderCreateView.as_view(), name='order_creation'),
    path('order/detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]
zarinpal_urlpatterns = [
    path('request/<int:pk>/', SendRequestView.as_view(), name='request'),
    path('order/verify/', VerifyView.as_view(), name='verify'),
]

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_detail'),
] + cart_urlpatterns + order_urlpatterns + zarinpal_urlpatterns
