from rest_framework import routers
from especialidade.views import EspecialidadeViewSet
from medico.views import MedicoViewSet
from agenda.views import AgendaViewSet
from usuario.views import UserViewSet
from consulta.views import ConsultaViewSet


router = routers.DefaultRouter()

router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendas', AgendaViewSet)
router.register(r'usuarios', UserViewSet)
router.register(r'consultas', ConsultaViewSet)
