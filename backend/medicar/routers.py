from rest_framework import routers
from especialidade.views import EspecialidadeViewSet
# from agendamento.views import EspecialidadeViewSet
from agendamento.views import MedicoViewSet
from agendamento.views import AgendaViewSet


router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'Agendas', AgendaViewSet)
