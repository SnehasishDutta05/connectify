import csv
import datetime

def get_todays_date():
    # Get today's date
    today = datetime.date.today()
    return today

def write_date_to_csv(filename, date):
    try:
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Date'])  # Write header
            csv_writer.writerow([date])  # Write today's date
        print(f"Today's date has been successfully written to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

def write_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
        print(f"Data has been successfully written to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
    todays_date = get_todays_date()
    filename = 'dates.csv'
    write_date_to_csv(filename, '2024-01-25')


filename = 'demo.csv'
data = [

    ['Topic', 'User ID', 'Username', 'Date', 'Likes', 'Shares', 'Comments', 'Views', 'Hashtags','Content'],
    ['Technology', '123456', 'john_doe', '2024-03-01', '50', '10', '5', '1000', '#tech #innovation',
     'Check out the latest tech gadgets!'],
    ['Technology', '789012', 'alice_smith', '2024-03-02', '80', '20', '8', '1500', '#gadgets #AI',
     'Excited to share my new project on AI!'],
    ['Technology', '345678', 'bob_jones', '2024-03-03', '120', '30', '15', '2000', '#technews #software',
     'Discussing the future of software development.'],
    ['Technology', '901234', 'emma_wilson', '2024-03-04', '70', '15', '6', '1200', '#coding #programming',
     'Coding is my passion!'],
    ['Technology', '567890', 'michael_davis', '2024-03-05', '90', '25', '10', '1800', '#innovation #IoT',
     'Exploring new innovations in IoT.'],
    ['Technology', '234567', 'olivia_white', '2024-03-06', '110', '35', '18', '2200', '#technology #future',
     'The future looks bright with technology!'],
    ['Technology', '987654', 'sophie_brown', '2024-03-07', '60', '12', '7', '1300', '#tech #coding',
     'Working on a new coding project!'],
    ['Technology', '654321', 'david_miller', '2024-03-08', '85', '18', '9', '1600', '#AI #machinelearning',
     'Exploring the possibilities of AI and machine learning.'],
    ['Technology', '112233', 'oliver_thomas', '2024-03-09', '95', '22', '12', '1900', '#technews #innovation',
     'Keeping up with the latest tech news!'],
    ['Technology', '998877', 'emma_jackson', '2024-03-10', '75', '14', '8', '1400', '#programming #software',
     'Software development is fascinating!'],
    ['Technology', '554433', 'mason_harris', '2024-03-11', '105', '28', '15', '2100', '#coding #webdevelopment',
     'Building a new website from scratch.'],
    ['Technology', '776655', 'ava_roberts', '2024-03-12', '115', '32', '17', '2300', '#tech #innovation',
     'Excited about the latest tech innovations!'],
    ['Technology', '443322', 'ethan_nelson', '2024-03-13', '65', '11', '6', '1100', '#coding #programming',
     'Coding challenges are my favorite!'],
    ['Technology', '665544', 'mia_clark', '2024-03-14', '88', '20', '10', '1700', '#gadgets #technology',
     'Geeking out over the latest gadgets!'],
    ['Technology', '220011', 'noah_hall', '2024-03-15', '80', '16', '9', '1500', '#AI #innovation',
     'AI is revolutionizing the tech industry!'],
    ['Technology', '889900', 'chloe_anderson', '2024-03-16', '70', '15', '8', '1250', '#software #development',
     'The future of software development looks promising!'],
    ['Food', '123456', 'foodlover123', '2024-03-01', '150', '50', '20', '5000', '#foodie #yum', 'Indulging in some delicious pasta tonight!'],
    ['Food', '789012', 'chefmike', '2024-03-02', '180', '60', '25', '6000', '#cheflife #cooking', 'Experimenting with new recipes in the kitchen.'],
    ['Food', '345678', 'healthy_eats', '2024-03-03', '120', '40', '15', '4000', '#healthyfood #cleaneating', 'Enjoying a nutritious salad for lunch today.'],
    ['Food', '901234', 'dessertlover', '2024-03-04', '200', '70', '30', '7000', '#dessert #sweettooth', 'Satisfying my sweet tooth with some decadent desserts!'],
    ['Food', '567890', 'foodieadventures', '2024-03-05', '160', '55', '22', '5500', '#foodtravel #foodblogger', 'Exploring the local food scene and documenting my culinary adventures.'],
    ['Food', '234567', 'organicchef', '2024-03-06', '140', '45', '18', '4500', '#organicfood #farmtotable', 'Cooking up farm-fresh ingredients for a wholesome meal.'],
    ['Food', '987654', 'foodiechef', '2024-03-07', '170', '58', '23', '5200', '#foodlover #homecooking',
     'Whipping up a delicious home-cooked meal for dinner tonight.'],
    ['Food', '654321', 'healthyliving', '2024-03-08', '130', '42', '17', '4200', '#nutrition #wellness',
     'Fueling my body with nutritious and wholesome foods.'],
    ['Food', '112233', 'streetfoodie', '2024-03-09', '190', '65', '28', '6200', '#streetfood #foodtruck',
     'Exploring the vibrant world of street food in the city.'],
    ['Food', '998877', 'bakingenthusiast', '2024-03-10', '220', '75', '32', '7500', '#baking #desserts',
     'Baking some mouthwatering treats to satisfy my sweet cravings.'],
    ['Food', '554433', 'foodcritic', '2024-03-11', '150', '50', '20', '5000', '#foodcritic #review',
     'Sampling dishes at a new restaurant and sharing my honest reviews.'],
    ['Food', '776655', 'spiceupyourlife', '2024-03-12', '180', '62', '25', '5500', '#spicyfood #flavorful',
     'Adding a kick of spice to my meals for some extra flavor!'],
    ['Food', '443322', 'plantbasedeats', '2024-03-13', '200', '70', '30', '7000', '#plantbased #vegan',
     'Embracing a plant-based lifestyle with delicious vegan meals.'],
    ['Food', '665544', 'sushiaddict', '2024-03-14', '160', '55', '22', '5500', '#sushi #japanesefood',
     'Craving some fresh and flavorful sushi rolls for lunch.'],
    ['Food', '220011', 'foodphotographer', '2024-03-15', '140', '45', '18', '4500', '#foodphotography #foodstyling',
     'Capturing the beauty of food through stunning photographs.'],
    ['Food', '889900', 'culinaryadventures', '2024-03-16', '175', '60', '25', '6000', '#foodadventures #culinary',
     'Embarking on culinary adventures to explore different cuisines and flavors.'],
    ['Travel', '123456', 'wanderlust', '2024-03-01', '200', '80', '30', '8000', '#travel #explore', 'Exploring the beautiful landscapes of a new destination.'],
    ['Travel', '789012', 'adventureseeker', '2024-03-02', '250', '100', '40', '10000', '#adventure #wanderlust', 'Embarking on an epic adventure to unknown territories.'],
    ['Travel', '345678', 'globetrotter', '2024-03-03', '180', '70', '25', '7000', '#globetrotter #travelbug', 'Indulging in the thrill of traveling to far-off places and experiencing different cultures.'],
    ['Travel', '901234', 'backpacker', '2024-03-04', '220', '90', '35', '9000', '#backpacking #adventure', 'Backpacking through exotic locations and immersing in the local culture.'],
    ['Travel', '567890', 'jetsetter', '2024-03-05', '190', '75', '28', '7500', '#jetsetter #luxurytravel', 'Jetting off to luxurious destinations for a lavish vacation experience.'],
    ['Travel', '234567', 'nomadlife', '2024-03-06', '210', '85', '32', '8500', '#digitalnomad #wanderlust', 'Living the nomad life and working remotely from stunning locations around the world.'],
    ['Travel', '987654', 'explorer', '2024-03-07', '230', '95', '38', '9500', '#explorer #adventure',
     'Venturing into uncharted territories and discovering hidden gems.'],
    ['Travel', '654321', 'wanderer', '2024-03-08', '270', '110', '45', '11000', '#wanderer #travelholic',
     'Wandering aimlessly through picturesque landscapes and soaking in the beauty of nature.'],
    ['Travel', '112233', 'discoverer', '2024-03-09', '180', '70', '25', '7000', '#discoverer #explore',
     'Discovering new cultures, traditions, and cuisines while traveling the world.'],
    ['Travel', '998877', 'dreamer', '2024-03-10', '240', '95', '40', '9500', '#dreamer #wanderlust',
     'Chasing dreams and creating unforgettable memories in breathtaking destinations.'],
    ['Travel', '554433', 'adventurer', '2024-03-11', '200', '80', '30', '8000', '#adventurer #explore',
     'Embracing adventure and seeking thrill in every journey embarked upon.'],
    ['Travel', '776655', 'roamfree', '2024-03-12', '220', '85', '35', '8500', '#roamfree #travelbug',
     'Roaming free and exploring the world with a curious and open mind.'],
    ['Travel', '443322', 'destinationseeker', '2024-03-13', '250', '100', '40', '10000',
     '#destinationseeker #wanderlust', 'Seeking new destinations and experiences to quench the thirst for adventure.'],
    ['Travel', '665544', 'gypsy_soul', '2024-03-14', '190', '75', '28', '7500', '#gypsysoul #traveler',
     'Embracing the gypsy soul and living a life filled with wanderlust and wonder.'],
    ['Travel', '220011', 'journeyman', '2024-03-15', '210', '85', '32', '8500', '#journeyman #adventure',
     'Embarking on a journey of self-discovery and exploration in distant lands.'],
    ['Travel', '889900', 'wanderlustvibes', '2024-03-16', '200', '80', '30', '8000', '#wanderlustvibes #explore',
     'Feeling the wanderlust vibes and craving new adventures in exotic destinations.'],
    ['Travel', '112233', 'passportready', '2024-03-17', '260', '105', '42', '10500', '#passportready #travelgoals',
     'Keeping the passport ready for spontaneous trips and fulfilling travel goals.'],
    ['Travel', '998877', 'escapeartist', '2024-03-18', '280', '115', '48', '11500', '#escapeartist #wanderlust',
     'Mastering the art of escapism and finding solace in travel experiences.'],
    ['Travel', '554433', 'wanderlustwarrior', '2024-03-19', '210', '85', '32', '8500', '#wanderlustwarrior #adventure',
     'Conquering new horizons and embracing challenges like a true wanderlust warrior.'],
    ['Travel', '776655', 'travelenthusiast', '2024-03-20', '240', '95', '38', '9500', '#travelenthusiast #explore',
     'Fueling the passion for travel and exploring the world one destination at a time.'],
    ['Travel', '443322', 'globetrotting', '2024-03-21', '270', '110', '45', '11000', '#globetrotting #wanderlust',
     'Embarking on a global adventure and collecting memories from every corner of the world.']
]




write_to_csv(filename, data)

