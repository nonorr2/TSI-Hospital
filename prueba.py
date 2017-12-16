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

class prueba(osv.Model):
    _name = 'prueba'
    _description = 'pruebas de un paciente con un medico'
    
    _columns = {
        'name': fields.char("Tipo", size=100, required=True),
        'fechaHora': fields.datetime('Fecha y Hora', required=True, autodate=True),
        'medico_id': fields.many2one("medico", "Medico", required=True),
        'paciente_id': fields.many2one("paciente", "Paciente", required=True), 
        'descripcion': fields.text("Descripcion", required=True),
        'hospital_id': fields.many2one("hospital", "Hospital", required=True), 
    }
prueba()
