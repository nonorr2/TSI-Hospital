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

class aseguradora(osv.Model):
    _name = 'aseguradora'
    _description = 'aseguradora'
    
    _columns = {
        'name': fields.char('Nombre', size=64, required=True),
        'direccion': fields.char("Dirección", size=64, required=True),
        'cif': fields.char('Cif', size=9, required=True),
        'telefono': fields.integer('Telefono', size=9, required=True),
        'pacientes_ids':fields.one2many('paciente', 'aseguradora_id', 'Pacientes'),
    }
    
    _sql_constraints=[('cif_ase_uniq','unique (cif)','El cif ya existe')]
aseguradora()