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

class medico(osv.Model):
    _name = 'medico'
    _description = 'Clase que gestiona las operaciones de un medico'
    
    _columns = {
            'name':fields.char('Nombre', size=64, required=True, readonly=False),
            'apellidos':fields.char('Apellidos', size=64, required=True, readonly=False),
            'dni':fields.char('DNI', size=64, required=True, readonly=False),
            'numColegiado':fields.char('Número colegiado', size=64, required=True, readonly=False),
            'direccion':fields.char('Dirección', size=64, required=False, readonly=False),
            'email':fields.char('Correo electrónico', size=64, required=False, readonly=False),
            'telefono':fields.char('Teléfono', size=64, required=True, readonly=False),
            'cita_ids':fields.one2many('cita','name','Citas')
        }
medico()
