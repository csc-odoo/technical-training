# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _

class Editor(models.Model):
    _name = 'library.publisher'

    name = fields.Char(string='Name')



