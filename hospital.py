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

class hospital(osv.Model):
    _name = 'hospital'
    _description = 'Hospital'
    
    def _check_nombre(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.name.replace(' ','').isalpha():
                return True
            else:
                return False 

    def _check_cif(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            esValida = True
            if len(obj.cif)==9:
                contador = 1
                    
                if esValida == True and obj.cif[0] < 'A' or obj.cif[0] > 'Z':                    
                    esValida = False
                
                
                while contador < 9 and esValida == True:
                    if not obj.cif[contador].isdigit() or obj.cif[contador] < 1:
                        esValida = False
                    contador += 1
            else:
                esValida = False
                
            return esValida        
        
    def _check_telefono(self,cr,uid,ids,context=None):
            obj=self.browse(cr,uid,ids[0],context=context)
            
            if obj.telefono[0] == '9' and len(obj.telefono)==9 and obj.telefono.isdigit():
                return True
            else:
                return False    
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'cif':fields.char('CIF', size=9, required=True),
            'direccion':fields.char('Direccion', size=200, required=True),
            'telefono':fields.char('Telefono', size=9, required=True),
            'prueba_ids':fields.one2many('prueba', 'hospital_id', 'Prueba'),
        }
    
    _sql_constraints=[('cif_hos_uniq','unique (cif)','El cif ya existe')]
    _constraints = [(_check_nombre, 'El nombre no es valido.' , [ 'name' ]),(_check_cif, 'El CIF no es valido.' , [ 'cif' ]),(_check_telefono, 'El telefono no es valido.' , [ 'telefono' ])]
hospital()
