# Copyright 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Drag & drop emails to Odoo",
    "version": "16.0.1.1.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Discuss",
    "website": "https://github.com/OCA/social",
    "summary": "Attach emails to Odoo by dragging them from your desktop",
    "depends": ["mail"],
    # Quatra: this module's dependency on extract_msg implies oletools which
    # disagrees with oca-server-ux' pyrfc6266 on its version of pyparsing.
    #
    # 2024-04-17T10:26:03,611 The conflict is caused by:
    # 2024-04-17T10:26:03,611     pyrfc6266 1.0.0 depends on pyparsing~=3.0.7
    # 2024-04-17T10:26:03,611     oletools 0.60.1 depends on pyparsing<3 and >=2.1.0
    #
    # Quatra change start
    "installable": False,
    # Quatra change end
    "external_dependencies": {"python": ["extract_msg", "cryptography<37"]},
    "data": ["views/res_config_settings_views.xml"],
    "assets": {
        "web.assets_backend": [
            "mail_drop_target/static/src/js/file_uploader.esm.js",
        ],
    },
}
