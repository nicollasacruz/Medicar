from rest_framework import routers
from especialidade.views import EspecialidadeViewSet
from medico.views import MedicoViewSet


router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
