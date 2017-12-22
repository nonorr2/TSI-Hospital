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

class ambulancia(osv.Model):
    _name = 'ambulancia'
    _description = 'ambulancia'
    
    def _check_matricula(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            esValida = True
            if len(obj.name)==7:
                contador = 0
                while contador < 4 and esValida == True:
                    if not obj.name[contador].isdigit():
                        esValida = False
                    contador += 1
                
                while contador < 7 and esValida == True:
                    if obj.name[contador] < 'A' or obj.name[contador] > 'Z':                    
                        esValida = False
                    contador += 1
            else:
                esValida = False
                
            return esValida
        
    def _check_capacidad(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.capacidad>0 and obj.capacidad<8:
                return True
            else:
                return False
    

    _columns = {
                'name':fields.char('Matricula', size=7, required=True, readonly=False),
                'capacidad':fields.integer('Capacidad', required=True, readonly=False),
    }
    
    _sql_constraints=[('mat_amb_uniq','unique (name)','La matricula ya existe')]
    _constraints = [(_check_matricula, 'La matricula no es valida.' , [ 'name' ]),(_check_capacidad, 'La capacidad no es valida.' , [ 'capacidad' ])]
ambulancia()