# -*- coding: utf-8 -*-

from openerp import fields, models

class Navintharh(models.Model):
	_inherit = 'hr.job'

	x_navintha_fechadeelaboracion = fields.Date(string="Fecha de elaboración")
	x_navintha_fechadeaprovacion = fields.Date(string="Fecha de aprovación")
	x_navintha_propositodelpuesto = fields.Text(string="Propósito del puesto")


	x_navintha_relacionesinternas_delpuestoconotros = fields.Text(string="Relaciones internas con otros puestos")
        x_navintha_responsabilidades = fields.Many2one('res.partner', string="Responsabilidades")
	x_navintha_relacionesexternas_delpuestoconotros = fields.Text(string="Relaciones externas con otros puestos")

	x_navintha_responsabilidades_descripcion = fields.Text(string="Responsabilidades")
	x_navintha_responsabilidades_frecuenciaderealizacion = fields.Text(string="Frecuencia de realización")

	x_navintha_ltd_desicion = fields.Boolean(string="Libertad para toma de desiciones")

	x_navintha_condicionesdeltrabajo = fields.Text(string="Condiciones del trabajo")

	#Perfil del puesto
	x_navintha_edad = fields.Integer(string="Edad")

	x_navintha_escolaridad = fields.Many2one('hr.escolaridad', string="Esolaridad")

        x_navintha_experiencia = fields.Text(string="Experiencia")
	x_navintha_competenciastecnicas = fields.Text(string="Competencias técnicas")
	x_navintha_manejomaquinariaequipo = fields.Text(string="Manejo de maquinaria y/o equipo")
	x_navintha_manejodesoftware = fields.Text(string="Manejo de software")
	x_navintha_idiomas = fields.Text(string="Idiomas")
	x_navintha_disponibilidadviajar = fields.Boolean(string="Diponibilidad para viajar")
	x_navintha_disponibilidadcambioresidencia = fields.Boolean(string="Disponibilidad de cambio de residencia")
	x_navintha_listadocompetencias = fields.Text(string="Listado de competencias")
	#Perfiles, competencias, habilidades y capacidades requeridas
	x_navintha_per_comp_hab_cap = fields.Text(string="Perfiles, competencias, habilidades y capacidades requeridas")

        x_navintha_skills = fields.Many2many('hr.skill')
