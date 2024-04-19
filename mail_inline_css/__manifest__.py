# Copyright 2017 David BEAL @ Akretion
# Copyright 2019 Camptocamp SA

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Mail Inline CSS",
    "summary": "Convert style tags in inline style in your mails",
    "version": "16.0.0.1.0",
    "author": "Akretion, camptocamp, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/social",
    "license": "AGPL-3",
    "category": "Tools",
    # Quatra: this module's dependency on premailer implies oletools which
    # disagrees with oca-server-ux' pyrfc6266 on its version of pyparsing.
    #
    # 2024-04-17T10:26:03,611 The conflict is caused by:
    # 2024-04-17T10:26:03,611     pyrfc6266 1.0.0 depends on pyparsing~=3.0.7
    # 2024-04-17T10:26:03,611     oletools 0.60.1 depends on pyparsing<3 and >=2.1.0
    #
    # Quatra change start
    # "installable": True,
    "installable": False,
    # Quatra change end
    "external_dependencies": {"python": ["premailer"]},
    "depends": ["email_template_qweb"],
    "demo": ["demo/demo_template.xml", "demo/demo_mail_template.xml"],
}
