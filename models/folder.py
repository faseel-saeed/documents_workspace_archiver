# -*- coding: utf-8 -*-
from odoo import _, api, Command, fields, models
from odoo.exceptions import ValidationError


class DocumentFolder(models.Model):
    _inherit = 'documents.folder'

    active = fields.Boolean(default=True,
                            help="If the active field is set to False, it will allow you to hide the folder without removing it.")

