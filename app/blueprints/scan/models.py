# Description: Scan Model for the Scan Blueprint

# Importing Required Libraries
from sqlalchemy import Enum, ARRAY
from app.extensions import db
from app.extensions import func
# Importing Required Libraries

# Importing Required Entities
from app.blueprints.scan.entities import ARPEntity, ARPTag
# Importing Required Entities

# Importing Required Functions
from app.blueprints.scan.functions import ARPFunctions
# Importing Required Functions

# Importing Required Exceptions
from app.blueprints.scan.exceptions import *
# Importing Required Exceptions

# ARP Model
class ARP(db.Model):
    __tablename__ = 'arp'  # Table Name

    # Columns
    arp_id = db.Column(db.Integer, primary_key=True, nullable=False)  # ARP ID
    fk_ip_address_id = db.Column(db.Integer, db.ForeignKey('ip_segment.ip_segment_id'), nullable=False)  # FK IP Address ID
    arp_ip = db.Column(db.String(15), nullable=False)  # ARP IP
    arp_mac = db.Column(db.String(17), nullable=False)  # ARP MAC
    arp_alias = db.Column(db.String(255), nullable=True)  # ARP Alias
    arp_tag = db.Column(db.String(512), nullable=True)  # ARP Tag
    arp_interface = db.Column(db.String(255), nullable=False)  # ARP Interface
    arp_is_dhcp = db.Column(db.Boolean, nullable=False)  # ARP DHCP
    arp_is_invalid = db.Column(db.Boolean, nullable=False)  # ARP Invalid
    arp_is_dynamic = db.Column(db.Boolean, nullable=False)  # ARP Dynamic
    arp_is_complete = db.Column(db.Boolean, nullable=False)  # ARP Complete
    arp_is_disabled = db.Column(db.Boolean, nullable=False)  # ARP Disabled
    arp_is_published = db.Column(db.Boolean, nullable=False)  # ARP Published
    # Columns

    # Relationships
    ip_segment = db.relationship('IPSegment', backref=db.backref('arp', lazy=True))  # IP Segment Relationship
    # Relationships

    # Object Representation
    def __repr__(self):
        return f'<ARP {self.arp_id}>'  # ARP Object Representation
    # Object Representation

    # Dictionary Representation
    def to_dict(self):
        return {
            'arp_id': self.arp_id,  # ARP ID
            'fk_ip_address_id': self.fk_ip_address_id,  # FK IP Address ID
            'arp_ip': self.arp_ip,  # ARP IP
            'arp_mac': self.arp_mac,  # ARP MAC
            'arp_alias': self.arp_alias,  # ARP Alias
            'arp_tag': self.arp_tag,  # ARP Tag
            'arp_interface': self.arp_interface,  # ARP Interface
            'arp_is_dhcp': self.arp_is_dhcp,  # ARP DHCP
            'arp_is_invalid': self.arp_is_invalid,  # ARP Invalid
            'arp_is_dynamic': self.arp_is_dynamic,  # ARP Dynamic
            'arp_is_complete': self.arp_is_complete,  # ARP Complete
            'arp_is_disabled': self.arp_is_disabled,  # ARP Disabled
            'arp_is_published': self.arp_is_published  # ARP Published
        }
    # Dictionary Representation

    # Static Methods
    # ARP - Add ARP
    @staticmethod
    def add_arp(arp: ARPEntity):
        try:  # Try to add the ARP data
            # If the ARP data is new and does not exist
            if (ARPFunctions.validate_arp_exists(
                arp.arp_ip,  # ARP IP
                arp.arp_mac  # ARP MAC
            )):
                # If the arp does not exist in the database, add it
                arp.validate_arp()  # Validate the ARP
                arp_obj = ARP(  # ARP Object
                    fk_ip_address_id=arp.fk_ip_address_id,  # FK IP Address ID
                    arp_ip=arp.arp_ip,  # ARP IP
                    arp_mac=arp.arp_mac,  # ARP MAC
                    arp_alias=arp.arp_alias,  # ARP Alias
                    arp_tag=arp.arp_tag,  # ARP Tag
                    arp_interface=arp.arp_interface,  # ARP Interface
                    arp_is_dhcp=arp.arp_is_dhcp,  # ARP DHCP
                    arp_is_invalid=arp.arp_is_invalid,  # ARP Invalid
                    arp_is_dynamic=arp.arp_is_dynamic,  # ARP Dynamic
                    arp_is_complete=arp.arp_is_complete,  # ARP Complete
                    arp_is_disabled=arp.arp_is_disabled,  # ARP Disabled
                    arp_is_published=arp.arp_is_published  # ARP Published
                )
                db.session.add(arp_obj)  # Add the ARP Object
                db.session.commit()  # Commit the Database Session
            # If already exists, update all the fields
            else:
                arp.validate_arp()  # Validate the ARP
                arp_obj = ARP.query.filter(
                    ARP.arp_ip == arp.arp_ip,  # ARP IP
                    ARP.arp_mac == arp.arp_mac  # ARP MAC
                ).first()
                arp_obj.fk_ip_address_id = arp.fk_ip_address_id  # FK IP Address ID
                arp_obj.arp_alias = arp.arp_alias  # ARP Alias
                arp_obj.arp_tag = arp.arp_tag  # ARP Tag
                arp_obj.arp_interface = arp.arp_interface  # ARP Interface
                arp_obj.arp_is_dhcp = arp.arp_is_dhcp  # ARP DHCP
                arp_obj.arp_is_invalid = arp.arp_is_invalid  # ARP Invalid
                arp_obj.arp_is_dynamic = arp.arp_is_dynamic  # ARP Dynamic
                arp_obj.arp_is_complete = arp.arp_is_complete  # ARP Complete
                arp_obj.arp_is_disabled = arp.arp_is_disabled  # ARP Disabled
                arp_obj.arp_is_published = arp.arp_is_published  # ARP Published
                db.session.commit()  # Commit the Database Session
        except Exception as e:  # If an Exception occurs
            db.session.rollback()  # Rollback the Database Session
            print(str(e))  # Print the Exception
    # ARP - Add ARP

    # ARP - Delete ARP
    @staticmethod
    def delete_region(arp_id):
        try:  # Try to delete the ARP
            arp = ARP.query.get(arp_id)  # Get the ARP
            db.session.delete(arp)  # Delete the ARP
            db.session.commit()  # Commit the Database Session
        except Exception as e:  # If an Exception occurs
            db.session.rollback()  # Rollback the Database Session
            print(str(e))  # Print the Exception
    # ARP - Delete ARP

    # ARP - Get ARP
    @staticmethod
    def get_arp(arp_id):
        try:  # Try to get the ARP
            arp = ARP.query.get(arp_id)  # Get the ARP
            obj = ARPEntity(  # ARP Object
                arp_id=arp.arp_id,  # ARP ID
                fk_ip_address_id=arp.fk_ip_address_id,  # FK IP Address ID
                arp_ip=arp.arp_ip,  # ARP IP
                arp_mac=arp.arp_mac,  # ARP MAC
                arp_alias=arp.arp_alias,  # ARP Alias
                arp_tag=arp.arp_tag,  # ARP Tag
                arp_interface=arp.arp_interface,  # ARP Interface
                arp_is_dhcp=arp.arp_is_dhcp,  # ARP DHCP
                arp_is_invalid=arp.arp_is_invalid,  # ARP Invalid
                arp_is_dynamic=arp.arp_is_dynamic,  # ARP Dynamic
                arp_is_complete=arp.arp_is_complete,  # ARP Complete
                arp_is_disabled=arp.arp_is_disabled,  # ARP Disabled
                arp_is_published=arp.arp_is_published  # ARP Published
            )
            return obj  # Return the ARP Object
        except Exception as e:  # If an Exception occurs
            print(str(e))  # Print the Exception
    # ARP - Get ARP

    # ARP - Get ARPs
    @staticmethod
    def get_arps():
        try:  # Try to get the ARPs
            arps = ARP.query.all()  # Get the ARPs
            obj_list = []  # Object List
            for arp in arps:  # For each ARP
                obj = ARPEntity(  # Create an instance of the ARPEntity class
                    arp_id=arp.arp_id,  # ARP ID
                    fk_ip_address_id=arp.fk_ip_address_id,  # FK IP Address ID
                    arp_ip=arp.arp_ip,  # ARP IP
                    arp_mac=arp.arp_mac,  # ARP MAC
                    arp_alias=arp.arp_alias,  # ARP Alias
                    arp_tag=arp.arp_tag,  # ARP Tag
                    arp_interface=arp.arp_interface,  # ARP Interface
                    arp_is_dhcp=arp.arp_is_dhcp,  # ARP DHCP
                    arp_is_invalid=arp.arp_is_invalid,  # ARP Invalid
                    arp_is_dynamic=arp.arp_is_dynamic,  # ARP Dynamic
                    arp_is_complete=arp.arp_is_complete,  # ARP Complete
                    arp_is_disabled=arp.arp_is_disabled,  # ARP Disabled
                    arp_is_published=arp.arp_is_published  # ARP Published
                )
                obj_list.append(obj)  # Append the ARP Object to the Object List
            return obj_list  # Return the Object List
        except Exception as e:  # If an Exception occurs
            print(str(e))  # Print the Exception
    # ARP - Get ARPs
    # Static Methods
# ARP Model
