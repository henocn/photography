from odoo import fields, models



class PhotographyClient(models.Model):
    _name="photography.client"
    _description="Client de photographie"


    name = fields.Char(string="Nom du client", required=True)
    email = fields.Char(string="Email du client")
    phone = fields.Char(string="Téléphone du client")
    address = fields.Text(string="Adresse du client")
    