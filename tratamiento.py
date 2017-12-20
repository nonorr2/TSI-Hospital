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

from osv import osv
from osv import fields

class tratamiento(osv.Model):
    _name = 'tratamiento'
    _description = 'Clase que gestiona los tratamientos'
    
    _columns = {
            'name':fields.char('Instrucciones', size=256, required=True, readonly=False),
            'inicio':fields.datetime('Fecha de inicio', required=True, autodate=True),
            'fin':fields.datetime('Fecha de fin', required=True, autodate=True),
            'posologia':fields.char('Posologia', size=64, required=True, readonly=False),
            'medico_id': fields.many2one("medico", "Medico", required=True),
            'paciente_id': fields.many2one("paciente", "Paciente", required=True),
            'medicamento_ids':fields.many2many('medicamento','medicamento_tratamiento_rel', 'medicamento_id', 'tratamiento_id','Medicamento'),
            'state':fields.selection([('enTratamiento','En tratamiento'),
                                  ('finTratamiento','Fin Tratamiento')],'Estados'),
        }
    _defaults = {'state':'enTratamiento', }   
tratamiento()