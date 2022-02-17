# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odooalmacen(models.Model):
#     _name = 'odooalmacen.odooalmacen'
#     _description = 'odooalmacen.odooalmacen'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
class almacen(models.Model):
	_name = 'odooalmacen.almacen'
	_description = 'model almacen'

	name = fields.Char('Id',required=True)
	tipo = fields.Char(string='Tipo',required=True)
	encargados_ids = fields.One2many('odooalmacen.encargado','encargado_id',string='EncargadoAlmacen')
class encargado(models.Model):
	_name = 'odooalmacen.encargado'
	_description = 'model encargado'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	encargado_id=fields.Many2one('odooalmacen.almacen',string='Almacen')
class camion(models.Model):
	_name = 'odooalmacen.camion'
	_description = 'model camion'
	name = fields.Char('Id',required=True)
	tamano = fields.Char(string='Tamano',required=True)
	camion_id=fields.Many2one('odooalmacen.camionero',string='Camionero')
class camionero(models.Model):
	_name = 'odooalmacen.camionero'
	_description = 'model camionero'
	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	camiones_ids = fields.One2many('odooalmacen.camion','camion_id',string='camion Almacen')
class empleado(models.Model):
	_name = 'odooalmacen.empleado'
	_description = 'model empleado'
	name = fields.Char('Id',required=True)
	nif = fields.Char(string='Nif',required=True)
	paquetesgrandes_ids = fields.One2many('odooalmacen.paquetegrande','paquetegrande_id',string='paquetegrande Almacen')
	paquetesmedianos_ids = fields.One2many('odooalmacen.paquetemediano','paquetemediano_id',string='paquetemediano Almacen')
	paquetespequenos_ids = fields.One2many('odooalmacen.paquetepequeno','paquetepequeno_id',string='paquetepequeno Almacen')
class paquetegrande(models.Model):
	_name = 'odooalmacen.paquetegrande'
	_description = 'model paquetegrande'
	name = fields.Char('Id',required=True)
	peso = fields.Char(string='Peso',required=True)
	paquetegrande_id=fields.Many2one('odooalmacen.empleado',string='Empleado')
class paquetemediano(models.Model):
	_name = 'odooalmacen.paquetemediano'
	_description = 'model paquetemediano'
	name = fields.Char('Id',required=True)
	peso = fields.Char(string='Peso',required=True)
	paquetemediano_id=fields.Many2one('odooalmacen.empleado',string='Empleado')
class paquetepequeno(models.Model):
	_name = 'odooalmacen.paquetepequeno'
	_description = 'model paquetepequeno'
	name = fields.Char('Id',required=True)
	peso = fields.Char(string='Peso',required=True)
	paquetepequeno_id=fields.Many2one('odooalmacen.empleado',string='Empleado')
class inversor(models.Model):
	_name = 'odooalmacen.inversor'
	_description = 'model inversor'
	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)