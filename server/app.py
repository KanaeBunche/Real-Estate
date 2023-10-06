from models import db,Agent, Property, Contact,AgentProperty
from flask_migrate import Migrate
from flask import Flask, request, make_response,jsonify
from flask_restful import Api, Resource,reqparse
import os
from flask_cors import CORS


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Final Project</h1>'



class Agents(Resource):
    def post(self):
        data = request.get_json()

       
        if 'username' not in data or 'password' not in data:
            return make_response(jsonify({"error": "Username and password are required"}), 400)

        new_agent = Agent()

        try:
            # Check if the username already exists
            existing_agent = Agent.query.filter_by(username=data['username']).first()
            if existing_agent:
                return make_response(jsonify({"error": "Username already exists"}), 400)

            

         
            new_agent.username = data['username']
            new_agent.password = data['password']

            # Add  new agent 
            db.session.add(new_agent)
            db.session.commit()

            return make_response(new_agent.to_dict(rules=('-properties', '-contacts',)), 201)
        except Exception as error:
            db.session.rollback()

            

            new_error = {"error": str(error)}
            return make_response(jsonify(new_error), 400)





class AgentLogin(Resource):
    def post(self):
        data = request.get_json()

        try:
            
            username = data.get('username')
            password = data.get('password')

            # Check if the username exists
            agent = Agent.query.filter_by(username=username, password=password).first()
            if agent:
                # agent ID in the response
                response_data = {
                    "message": "Login successful",
                    "agent_id": agent.id
                }
                return make_response(jsonify(response_data), 200)
            else:
                return make_response(jsonify({"error": "Wrong username or password"}), 401)

        except Exception as error:
            new_error = {"error": str(error)}
            return make_response(jsonify(new_error), 400)



class AgentProperties(Resource):
    def post(self):
        data = request.get_json()

        try:
            
            agent_property = AgentProperty(
                agent_id=data.get('agent_id'),
                property_id=data.get('property_id')  
            )

            
            db.session.add(agent_property)
            db.session.commit()

            return make_response({"message": "Agent property association created successfully"}, 201)
        except Exception as error:
            db.session.rollback()  
            return make_response({"error": str(error)}, 400)



class Agentget(Resource):
    def get(self, agent_id):
        agent = Agent.query.get(agent_id)
        if agent:
            agent_data = {
                "id": agent.id,
                "username": agent.username,
                "password": agent.password,
                
            }
            return jsonify(agent_data), 200
        else:
            return {"message": "Agent not found"}, 404




        

class PropertyPostResource(Resource):
    def post(self):
        data = request.get_json()
        new_property = Property()

        try:
            for key in data:
                setattr(new_property, key, data[key])
            db.session.add(new_property)
            db.session.commit()
            return make_response(new_property.to_dict(), 201)
        except ValueError as error:
            new_error = {"error": str(error)}
            return make_response(new_error, 400)

class PropertyGetResource(Resource):
    def get(self, property_id):
        property_obj = Property.query.get(property_id)
        if property_obj:
            return make_response(property_obj.to_dict(), 200)
        else:
            return make_response({"error": "Property not found"}, 404)





class PropertyEditResourcePut(Resource):
    def put(self, property_id):
        data = request.get_json()
        property_obj = Property.query.get(property_id)

        if property_obj:
            try:
                for key in data:
                    setattr(property_obj, key, data[key])
                db.session.commit()
                return make_response(property_obj.to_dict(), 200)
            except ValueError as error:
                new_error = {"error": str(error)}
                return make_response(new_error, 400)
        else:
            return make_response({"error": "Property not found"}, 404)

class PropertyEditResource(Resource):
    def delete(self, property_id):
        property_obj = Property.query.get(property_id)

        if property_obj:
            db.session.delete(property_obj)
            db.session.commit()
            return make_response({}, 200)
        else:
            return make_response({"error": "Property not found"}, 404)

        
class PropertyListResource(Resource):
    def get(self):
        # Retrieve all properties
        property_list = [
            {
                'id': property_obj.id,
                'title': property_obj.title,
                'description': property_obj.description,
                'price': property_obj.price,
                'image_url': property_obj.image_url,
            }
            for property_obj in Property.query.all()
        ]
        return make_response(property_list, 200)




    



class ContactGet(Resource):
    def get(self, contact_id):  
        contact = Contact.query.filter(Contact.id == contact_id).first()
        if contact:
            return make_response(contact.to_dict(), 200)
        else:
            return make_response({"error": "Contact not found"}, 404)


class ContactResource(Resource):
    def post(self):
       parser = reqparse.RequestParser()
       parser.add_argument('username', type=str, required=True, help='Username is required')
       parser.add_argument('message', type=str, required=True, help='Message is required')
       args = parser.parse_args()

       
       agent_with_username = Agent.query.filter_by(username=args['username']).first()
       if not agent_with_username:
           return make_response({"error": "Username does not exist"}, 403)

       new_contact = Contact(username=args['username'], message=args['message'])
       db.session.add(new_contact)

       try:
            db.session.commit()
            
            return make_response({
                "id": new_contact.id,
                "username": new_contact.username,
                "message": new_contact.message
            }, 201)
       except Exception as error:
            db.session.rollback()
            return make_response({"error": str(error)}, 400)



   



api.add_resource(AgentLogin, '/agentlogin')
api.add_resource(Agentget, '/agents/<int:agent_id>')
api.add_resource(Agents, '/agents')
api.add_resource(PropertyPostResource, '/properties')
api.add_resource(PropertyGetResource, '/properties/<int:property_id>')
api.add_resource(PropertyEditResource, '/properties/<int:property_id>/delete')
api.add_resource(PropertyListResource, '/properties-list')
api.add_resource(PropertyEditResourcePut,'/putproperties/<int:property_id>')
api.add_resource(ContactGet ,'/contacts/<int:contact_id>')
api.add_resource(ContactResource,'/contacts-list')
api.add_resource(AgentProperties, '/agent-properties')






if __name__ == '__main__':
    app.run(port=5555, debug=True)