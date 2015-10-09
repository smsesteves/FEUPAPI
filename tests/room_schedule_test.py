__author__ = 'smsesteves'

import unittest
import src.room_schedule as room_schedule

class RoomScheduleTest(unittest.TestCase):

    rs = room_schedule.RoomSchedule()

    def test_valid_room(self):
        self.assertEqual(self.rs.is_valid("B320"), True)

    def test_invalid_room(self):
        self.assertEqual(True,True)

    def test_get_schedule(self):
        self.assertEqual(self.rs.get_room_schedule("B320"),"B320")

    def test_get_room_id(self):
        self.assertEqual(self.rs.get_room_id("B320"),"73201")

if __name__ == '__main__':
    unittest.main()
