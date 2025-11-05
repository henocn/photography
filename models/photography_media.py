from odoo import models, fields 



class PhotographyMedia(models.Model):
    _name = "photography.media"
    _description = "Média photographique"

    project_id = fields.Many2one('photography.project', string="Projet associé", required=True)
    media_file = fields.Image(string="Photo média", required=True)
    description = fields.Text(string="Description du média")