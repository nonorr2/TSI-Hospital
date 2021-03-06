# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Hospital",
    "version": "1.0",
    "depends": ["base"],
    "author": "Grupo1",
    "category": "Hospital",
    "description": """
    Gestion hospitalaria.
    """,
    "init_xml": [],
    'data': ['medico_view.xml','cita_view.xml','ambulancia_view.xml','paciente_view.xml','tratamiento_view.xml','prueba_view.xml','hospital_view.xml','aseguradora_view.xml','laboratorio_view.xml','medicamento_view.xml','workflow/cita_workflow.xml','workflow/tratamiento_workflow.xml'],
    'demo_xml': ['demo_data.xml'],
    'installable': True,
    'active': False,
}