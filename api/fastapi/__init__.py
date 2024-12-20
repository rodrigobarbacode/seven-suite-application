from fastapi import APIRouter

from .routes.arps_api import arps_router
from .routes.logs_api import logs_router
from .routes.users_api import users_router
from .routes.sites_api import sites_router
from .routes.regions_api import regions_router
from .routes.routers_api import routers_router
from .routes.segments_api import segments_router
from .routes.settings_api import settings_router
from .routes.ipgroups_api import ip_groups_router
from .routes.dashboard_api import dashboard_router
from .routes.emailsender_api import emailsender_router
from .routes.ipgroupstags_api import ip_groups_tags_router
from .routes.notifications_api import notifications_router

private_router = APIRouter(prefix='/private', tags=['Seven Suite API'])

private_router.include_router(arps_router, tags=['ARPs'])
private_router.include_router(logs_router, tags=['Logs'])
private_router.include_router(users_router, tags=['Users'])
private_router.include_router(sites_router, tags=['Sites'])
private_router.include_router(regions_router, tags=['Regions'])
private_router.include_router(routers_router, tags=['Routers'])
private_router.include_router(segments_router, tags=['Segments'])
private_router.include_router(settings_router, tags=['Settings'])
private_router.include_router(ip_groups_router, tags=['IP Groups'])
private_router.include_router(dashboard_router, tags=['Dashboard'])
private_router.include_router(emailsender_router, tags=['Email Sender'])
private_router.include_router(notifications_router, tags=['Notifications'])
private_router.include_router(ip_groups_tags_router, tags=['IP Groups Tags'])
