from .entities.router import Router
from .entities.session_information import SessionInformation


class ModelRouter:

    @classmethod
    def get_routers(self, db):
        try:
            routers_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_all_routers")
            routers = cursor.fetchall()
            for i in range(len(routers)):
                routers_list.append(Router(
                    routers[i][0],
                    routers[i][1],
                    routers[i][2],
                    routers[i][3],
                    routers[i][4]
                ))
            cursor.close()
            return routers_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_router_by_id(self, db, router_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_router_by_id(%s)", (router_id,))
            router = cursor.fetchone()
            cursor.close()
            return Router(
                router[0],
                router[1],
                router[2],
                router[3],
                router[4]
            )
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_router(self, db, router):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_router(%s, %s, %s, %s)",
                           (router.router_name, router.fk_site_id, router.fk_session_id,
                            router.fk_ip_address_id))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_router(self, db, router):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_router(%s, %s, %s, %s, %s)",
                           (router.router_id, router.router_name, router.fk_site_id, router.fk_session_id,
                            router.fk_ip_address_id))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_router(self, db, router_id, session_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_router(%s, %s)", (router_id, session_id))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_router_with_session(self, db, router, session_information):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "CALL sp_add_router_with_session_information(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                 router.router_name,
                 router.fk_site_id,
                 router.fk_session_id,
                 router.fk_ip_address_id,
                 session_information.session_ip_address,
                 session_information.session_mac_address,
                 session_information.session_username,
                 session_information.session_password,
                 session_information.session_connection_type,
                 session_information.session_brand,
                 session_information.session_model,
                 session_information.allow_remote_access
                 ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)