import logging

LOGGER = logging.getLogger(__name__)

default_admin_views = []
default_admin_menu_links = []

def integrate_view_list(admin):
    '''Insert views from list'''

    admin_views = default_admin_views
    # admin_views = admin_views + imported_views

    for v in admin_views:
        LOGGER.debug('Adding view %s', v['name'])
        admin.add_view(
            v['view'],
            v['name'],
            category=v['category']
        )

    admin_menu_links = default_admin_menu_links
    # admin_menu_links = admin_menu_links + imported_views

    for ml in admin_menu_links:
        LOGGER.debug('Adding menu link %s', ml['name'])
        admin.add_link(
            ml['name'],
            href=ml['href'],
            category=ml['category'],
            category_icon=ml['category_icon']
        )


def init_views(admin):
    integrate_view_list(admin)
