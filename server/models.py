from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Agent(db.Model, SerializerMixin):
    __tablename__ = "agent"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique=True,)
    password = db.Column(db.String(255))

    # Define the many-to-many relationship with Property using agents_properties table
    property = db.relationship('Property', secondary='agents_properties', backref='agent_properties')
    

    serialize_rules = ('username', 'password', '-properties',"-contact",)

    def __repr__(self):
        return f'<Agent {self.id}>'
    
    @validates('username')
    def validate_username(self, key, username):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        return username

    @validates('password')
    def validate_password(self, key, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        return password

class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(255))

    # Define the many-to-many relationship with Agent using agents_properties table
    agents = db.relationship('Agent', secondary='agents_properties', backref='property_properties')
   
    serialize_rules = ('title', 'description', 'price', 'image_url','-agent', '-contacts')

    def __repr__(self):
        return f'<Property {self.id}>'
    
    @validates('title', 'description', 'image_url')
    def validate_string_fields(self, key, value):
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")
        return value

class AgentProperty(db.Model, SerializerMixin):
    __tablename__ = 'agents_properties'

    id = db.Column(db.Integer, primary_key=True)

    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

    serialize_rules = (('agent_id',), ('property_id',))



class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    message = db.Column(db.String(255))

    # Define the 'agents' relationship with the 'Agent' model
   
 
# Rest of your model definitions...

    serialize_rules = ('username', 'message',)
    
    def __repr__(self):
        return f'<Contact {self.id}>'




