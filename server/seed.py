from app import app
from models import db, Agent, Property
import random

if __name__ == '__main__':
    with app.app_context():
        print("Seeding Agents and Properties....")

        # Create 10 agents
        agents = []
        for i in range(10):
            agent = Agent(username=f'Agent{i}', password=f'password{i}')
            agents.append(agent)
            db.session.add(agent)

        # List of predefined image URLs for the properties
        image_urls = [
            
        "https://images.freeimages.com/images/large-previews/e85/house-1224030.jpg",
        "https://images.pexels.com/photos/280235/pexels-photo-280235.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/4450429/pexels-photo-4450429.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/750697/pexels-photo-750697.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/210558/pexels-photo-210558.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3820420/pexels-photo-3820420.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/449461/pexels-photo-449461.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3555615/pexels-photo-3555615.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1105754/pexels-photo-1105754.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2888492/pexels-photo-2888492.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/280216/pexels-photo-280216.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/534228/pexels-photo-534228.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/209274/pexels-photo-209274.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/276593/pexels-photo-276593.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/210538/pexels-photo-210538.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2893177/pexels-photo-2893177.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2371975/pexels-photo-2371975.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2625766/pexels-photo-2625766.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2439595/pexels-photo-2439595.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2439595/pexels-photo-2439595.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/259685/pexels-photo-259685.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/164522/pexels-photo-164522.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/323776/pexels-photo-323776.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/259593/pexels-photo-259593.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/210617/pexels-photo-210617.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/221024/pexels-photo-221024.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/209315/pexels-photo-209315.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/323775/pexels-photo-323775.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/277667/pexels-photo-277667.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/259751/pexels-photo-259751.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/208736/pexels-photo-208736.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/206172/pexels-photo-206172.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/259588/pexels-photo-259588.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2980955/pexels-photo-2980955.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1795508/pexels-photo-1795508.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/1862402/pexels-photo-1862402.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/950058/pexels-photo-950058.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2510067/pexels-photo-2510067.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/463734/pexels-photo-463734.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/2104151/pexels-photo-2104151.jpeg?auto=compress&cs=tinysrgb&w=800",
        "https://images.pexels.com/photos/3958961/pexels-photo-3958961.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/8583736/pexels-photo-8583736.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/3195644/pexels-photo-3195644.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/7027846/pexels-photo-7027846.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/5105622/pexels-photo-5105622.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/5008394/pexels-photo-5008394.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/7710011/pexels-photo-7710011.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/209315/pexels-photo-209315.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/5071130/pexels-photo-5071130.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/3990589/pexels-photo-3990589.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/5178055/pexels-photo-5178055.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load",
        "https://images.pexels.com/photos/14459280/pexels-photo-14459280.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/8031883/pexels-photo-8031883.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5353890/pexels-photo-5353890.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/8031890/pexels-photo-8031890.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/3958961/pexels-photo-3958961.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/6035306/pexels-photo-6035306.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/7031408/pexels-photo-7031408.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/10486074/pexels-photo-10486074.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5524166/pexels-photo-5524166.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/1029599/pexels-photo-1029599.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/4682066/pexels-photo-4682066.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/8031882/pexels-photo-8031882.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/4832522/pexels-photo-4832522.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/7031414/pexels-photo-7031414.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/4258275/pexels-photo-4258275.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5502228/pexels-photo-5502228.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/8288954/pexels-photo-8288954.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/4044785/pexels-photo-4044785.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/10827221/pexels-photo-10827221.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/7031595/pexels-photo-7031595.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5524165/pexels-photo-5524165.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5524167/pexels-photo-5524167.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load", 
        "https://images.pexels.com/photos/164522/pexels-photo-164522.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/7578848/pexels-photo-7578848.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/5524205/pexels-photo-5524205.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load",
        "https://images.pexels.com/photos/4061979/pexels-photo-4061979.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/5071177/pexels-photo-5071177.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/3935328/pexels-photo-3935328.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",    
        "https://images.pexels.com/photos/11018238/pexels-photo-11018238.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/209315/pexels-photo-209315.jpeg",
        "https://www.pexels.com/photo/brown-wooden-house-near-trees-2360673/",
        "https://www.pexels.com/photo/brown-wooden-house-surrounded-by-grass-463734/",
        "https://www.pexels.com/photo/house-2581922/",
        "https://www.pexels.com/photo/yellow-concrete-house-2102587/",
        "https://www.pexels.com/photo/white-2-storey-house-near-trees-1115804/",
        "https://images.pexels.com/photos/3617496/pexels-photo-3617496.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",

        ]





    
    

    
          
        

        # Create 95 properties
        properties = []
        for i in range(95):
            property = Property(
                title=f'Property {i}',
                description=f'This is property {i} for sale/rent.',
                price=100000 + (i * 1000),  # Adjust price as needed
                image_url=image_urls[i % len(image_urls)]  # Use image URLs from the list
            )
            properties.append(property)
            db.session.add(property)

        # Shuffle the agents to distribute them evenly
        random.shuffle(agents)

        # Link 2 agents to each property, ensuring each agent has only 2 properties
        agent_property_count = {}  # Dictionary to keep track of the number of properties per agent
        for property in properties:
            for agent in agents:
                if agent_property_count.get(agent.id, 0) < 2:
                    agent.properties.append(property)
                    agent_property_count[agent.id] = agent_property_count.get(agent.id, 0) + 1
                    break

        db.session.commit()





# from app import app
# from models import db, Agent, Property

# if __name__ == '__main__':
#     with app.app_context():
#         print("Seeding Agents and Properties....")
        
#         # Define a list of 50 real image URLs
#         image_urls = [
#             'https://example.com/image1.jpg',
#             'https://example.com/image2.jpg',
#             'https://example.com/image3.jpg',
#             # Add the remaining URLs here
#         ]

#         # Create and add 50 agents
#         for i in range(50):
#             agent = Agent(username=f'Agent{i}', password=f'password{i}')
#             db.session.add(agent)

#             # Create and add 50 properties with image URLs from the list
#             property = Property(
#                 title=f'Property {i}',
#                 description=f'This is property {i} for sale/rent.',
#                 price=100000 + (i * 1000),  # Adjust price as needed
#                 image_url=image_urls[i % len(image_urls)]  # Use image URLs from the list
#             )
#             db.session.add(property)

#             # Associate each property with a random agent
#             agent.properties.append(property)

#         db.session.commit()
