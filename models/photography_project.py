from odoo import models, fields


class PhotographyProject(models.Model):
    _name = "photography.project"
    _description = "Projet photographique"
    _rec_name = "title"

    layout_plan_selection = [
        ('annotated_photo', 'Photo annotée'),
        ('schematic_image', 'Image schématique'),
        ('other', 'Autre'),
    ]

    title = fields.Char(string="Titre du projet", required=True)
    client_id = fields.Many2one('photography.client', string="Client", ondelete='cascade', required=True)
    furniture_ids = fields.One2many('photography.furniture.association', 'project_id', string="Meubles utilisés")
    equipment_ids = fields.One2many('photography.equipment.association', 'project_id', string="Équipements utilisés")
    media_ids = fields.One2many('photography.media', 'project_id', string="Médias associés")
    layout_plan = fields.Selection(layout_plan_selection, string="Plan de disposition", default='annotated_photo', required=True)
    shooting_date = fields.Datetime(string="Date de la séance photo")
    description = fields.Text(string="Description du projet")