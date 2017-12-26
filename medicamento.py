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

class medicamento(osv.Model):
    _name = 'medicamento'
    _description = 'Clase que representa los medicamentos'
    
    def quitarDeTratamientos(self,cr,uid,ids,context=None):
        # ids es una lista de ids
        # desde la vista nos llega el id (en ids[0])de la clase
        # editada en la vista de formulario
        # Eliminamos los registros de la relación many2many
        res = self.write(cr,uid,ids,{'tratamiento_ids':[ (5, ) ]}, context=None)
        return res
    
    _columns = {
            'prospecto':fields.text('Prospecto', size=64, required=True, readonly=False),
            'nombre':fields.char('Nombre', size=64, required=True, readonly=False),
            'tratamiento_ids':fields.many2many('tratamiento', 'medicamento_tratamiento_rel', 'tratamiento_id', 'medicamento_id', 'Tratamientos'),
            'laboratorio_ids':fields.many2many('laboratorio', 'medicamento_laboratorio_rel', 'laboratorio_id', 'medicamento_id', 'Laboratorios'),
        }
medicamento()
