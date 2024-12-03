from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A cold and damp room with a rat scurrying in the corner.")

#kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with wall sconces scattered around")

ballroom = Room("Ballroom")
ballroom.set_description("A vast open room with a skylight, a grand chandelier and a shiny wooden floor")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")         #we link the kitchen to the dining room and the dining room back to the kitchen because links only go one way , so if the player were to enter the dining room, they would be stuck there
ballroom.link_room(dining_hall, "west")
dining_hall.link_room(ballroom, "east")         #the room we are linking from is the object you call the method on, and the room you are linking to, is the object we pass into the method

#getting details of the room
#kitchen.get_details()

#Using the move method in a loop to move the player between rooms
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)

