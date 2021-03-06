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
    
    def _numeroCitas(self, cr, uid, ids, field, arg,context=None):
        res = {}
        
        for medico in self.browse(cr, uid, ids, context=context):
            res[medico.id] = len(medico.cita_ids)
            
        return res
    
    def _check_dni(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            esValida = True
            if len(obj.dni)==9:
                contador = 0
                while contador < 8 and esValida == True:
                    if not obj.dni[contador].isdigit() or obj.dni[contador] < 1:
                        esValida = False
                    contador += 1
                    
                if esValida == True and obj.dni[8] < 'A' or obj.dni[8] > 'Z':                    
                    esValida = False
            else:
                esValida = False
                
            return esValida
        
    def _check_telefono(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.telefono[0] == '6' or obj.telefono[0] == '9' and len(obj.telefono)==9 and obj.telefono.isdigit():
                return True
            else:
                return False

    def _check_nombre(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.name.replace(' ','').isalpha():
                return True
            else:
                return False  
            
    def _check_apellidos(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.apellidos.replace(' ','').isalpha():
                return True
            else:
                return False          

    
    _columns = {
            'name':fields.char('Nombre', size=64, required=True, readonly=False),
            'apellidos':fields.char('Apellidos', size=64, required=True, readonly=False),
            'dni':fields.char('DNI', size=9, required=True, readonly=False),
            'numColegiado':fields.char('Número colegiado', size=10, required=True, readonly=False),
            'direccion':fields.char('Dirección', size=64, required=False, readonly=False),
            'email':fields.char('Correo electrónico', size=64, required=False, readonly=False),
            'telefono':fields.char('Teléfono', size=9, required=True, readonly=False),
            'photo':fields.binary('Foto'),
            'cita_ids':fields.one2many('cita','medico_id','Citas'),
            'num_citas': fields.function(_numeroCitas, type='integer', string='Número de citas', store = True),
        }
    
    _sql_constraints=[('dni_med_uniq','unique (dni)','El dni ya existe'),('numcol_med_uniq','unique (numColegiado)','El numero de colegiado ya existe')]
    _constraints = [(_check_dni, 'El DNI no es valido.' , [ 'dni' ]),(_check_telefono, 'El telefono no es valido.' , [ 'telefono' ]),(_check_nombre, 'El nombre no es valido.' , [ 'name' ]),(_check_apellidos, 'El nombre no es valido.' , [ 'apellidos' ])]

medico()