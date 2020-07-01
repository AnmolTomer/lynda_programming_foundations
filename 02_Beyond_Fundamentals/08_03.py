class Attendee:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print("Name:{}, Tickets:{}".format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print("{} tickets increased to {}".format(self.name, self.tickets))


attendee1 = Attendee('Cosmic', 4)
attendee2 = Attendee('Nacho', 1)

attendee1.displayAttendee()
attendee2.displayAttendee()
