from django.urls import include, path
from rest_framework import routers


from despesa.api.viewsets import DespesaViewSet, DespesaAutenticationView

app_name = 'despesa'

router = routers.DefaultRouter()

router.register(r'despesas', DespesaViewSet, basename='despesas')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/despesa-autentication/', DespesaAutenticationView.as_view())
]