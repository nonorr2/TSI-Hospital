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
from datetime import datetime, timedelta

class cita(osv.Model):
    _name = 'cita'
    _description = 'cita de un paciente con un medico'

    def _recuperarID(self, cr, uid, ids, field, arg,context=None):
        res = {}
        
        for cita in self.browse(cr, uid, ids, context=context):
            res[cita.id] = cita.id
            
        return res
    
    def onchange_inicio(self,cr,uid,ids,inicio):
        fechaHoraFin=datetime.strptime(inicio,"%Y-%m-%d %H:%M:%S")+timedelta(minutes=10)
        return{'value':{'fechaHoraFin':str(fechaHoraFin)}}


    _columns = {
        'name': fields.function(_recuperarID, type='integer', string='Id Cita', store=True),
        'fechaHora': fields.datetime('Fecha y Hora',required=True, autodate = True),
        'fechaHoraFin': fields.datetime('Fecha y Hora de fin',required=True, autodate = False, readonly=True),
        'medico_id': fields.many2one("medico","Medico", required=True),
        'paciente_id': fields.many2one("paciente","Paciente", required=True),
        'ambulancia_id': fields.many2one("ambulancia","Ambulancia"),
        'descripcion': fields.text("Descripcion", required=True),
        'state':fields.selection([('start','Pendiente'),
                                  ('realizandose', 'Realizandose'),
                                  ('cancelar', 'Cancelar'),
                                  ('terminada','Terminada')],'Estados'),
    }
    _defaults = {'state':'start', }
cita()