from odoo import fields, models



class PhotographyClient(models.Model):
    _name="photography.client"
    _description="Client de photographie"
    _rec_name = "name"


    name = fields.Char(string="Nom du client", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Contact", required=True)
    address = fields.Text(string="Adresse du client")
    