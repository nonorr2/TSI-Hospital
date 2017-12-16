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

class paciente(osv.Model):
    _name = 'paciente'
    _description = 'Pacientes del hospital'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'dni':fields.char('DNI', size=9, required=True),
            'numSegurSocial' :fields.integer('Nº Seguridad Social', size=9, required=True),
            'apellidos':fields.char('Apellidos', size=200, required=True),
            'direccion':fields.char('Dirección', size=200, required=True),
            'email':fields.char('Email', size=64, required=True),
            'telefono': fields.integer('Telefono', size=9),
            'photo': fields.binary('Foto'), 
            'citas_ids':fields.one2many('cita', 'paciente_id', 'Citas'),
            'pruebas_ids':fields.one2many('prueba', 'paciente_id', 'Prueba'),
            'aseguradora_id': fields.many2one("aseguradora","Aseguradora"),
        }
paciente()
