class Room():
# defining a class
    def __init__ (self, room_name):
        self.name = room_name           #this gives the "Room" class attributes i.e. name and description
        self.description = None
        self.linked_rooms = {}       #This sets a blank dictionary
# Add your code here
#For every method within a class, the first parameter must be self, followed by any data you wish to pass in
    def set_name(self, room_name):      #This is the method to set the name of the room
        self.name = room_name
    def get_name(self):         #This is the method to get the name of the room
        return self.name
    def set_description(self, room_description):        #This is the method to set the description of the room
        self.description = room_description
    def get_description(self):      #This is the method to get the description of the room
        return self.description
    #Because we have not got a method to print the room description in main.py, instead of amending the get_description method, we are creating a new method
    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms: " + repr(self.linked_rooms) )

    def get_details(self):
        print(self.name)
        print("-------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)       #this method loops through the dictionary self.linked_rooms and for every defined direction, prints out the direction and the name of the room in that direction

    def move(self, direction):          #This method has a parameter for the direction the player would like to move. if the direction is one of the directions linked to, the method returns the room object in that direction. if not, the method returns self, i.e. the player doesnt move.
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
