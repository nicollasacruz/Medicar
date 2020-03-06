from rest_framework import routers
from especialidade.views import EspecialidadeViewSet
from medico.views import MedicoViewSet
from agenda.views import AgendaViewSet


router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendas', AgendaViewSet)
