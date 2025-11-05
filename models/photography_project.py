from odoo import models, fields


class PhotographyProject(models.Model):
    _name = "photography.project"
    _description = "Projet photographique"
    _inherit = "project.project"

    layout_plan_selection = [
        ('annotated_photo', 'Photo annotée'),
        ('schematic_image', 'Image schématique'),
        ('other', 'Autre'),
    ]

    client_id = fields.Many2one('res.partner', string="Client", required=True)
    furniture_ids = fields.One2many('photography.furniture', 'project_id', string="Meubles utilisés")
    equipment_ids = fields.One2many('photography.equipment', 'project_id', string="Équipements utilisés")
    media_ids = fields.One2many('photography.media', 'project_id', string="Médias associés")
    layout_plan = fields.Selection(layout_plan_selection, string="Plan de disposition", default='annotated_photo', required=True)
    shooting_date = fields.Datetime(string="Date de la séance photo")
    description = fields.Text(string="Description du projet")