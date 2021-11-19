from flask import Blueprint 
from app.horario_disponivel.controllers import (HorarioMedico, HorarioCreate, HorarioDetails) 

horario_api = Blueprint('horario_api', __name__)

horario_api.add_url_rule(
    '/horario/medico/current/<int:medico_id>', view_func=HorarioMedico.as_view('horario_medico'), methods=['GET']
)

horario_api.add_url_rule(
    '/horario/medico/create/<int:medico_id>', view_func=HorarioCreate.as_view('horario_create'), methods=['POST']
)

horario_api.add_url_rule(
    '/horario/medico/details/<int:medico_id>/<int:horario_id>', view_func=HorarioDetails.as_view('horario_details'), methods=['GET','PATCH','DELETE']
)