import unittest

from ex2 import Ticket, reconstruct_trip


class TestEx2(unittest.TestCase):

    def test_short_case(self):
        ticket_1 = Ticket("NONE", "PDX")
        ticket_2 = Ticket("PDX", "DCA")
        ticket_3 = Ticket("DCA", "NONE")

        tickets = [ticket_1, ticket_2, ticket_3]

        expected = ["PDX", "DCA", "NONE"]
        result = reconstruct_trip(tickets, 3)

        self.assertTrue(expected == result)

    def test_long_case(self):
        ticket_1 = Ticket("PIT", "ORD")
        ticket_2 = Ticket("XNA", "SAP")#3
        ticket_3 = Ticket("SFO", "BHM")
        ticket_4 = Ticket("FLG", "XNA")
        ticket_5 = Ticket("NONE", "LAX")
        ticket_6 = Ticket("LAX", "SFO")#1
        ticket_7 = Ticket("SAP", "SLC")
        ticket_8 = Ticket("ORD", "NONE")#5
        ticket_9 = Ticket("SLC", "PIT")#4
        ticket_10 = Ticket("BHM", "FLG")#2

        tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

        expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                    "SLC", "PIT", "ORD", "NONE"]
        result = reconstruct_trip(tickets, 10)

        self.assertTrue(expected == result)


if __name__ == '__main__':
    unittest.main()
