# Logan Hicks & Dominic Assia

import unittest
import app 

class final_project_tests(unittest.TestCase):
    ''' Function tests for app.py (final project) '''
    

    def test_convert_to_seconds(self):
        ''' Tests convert to seconds function '''

        self.assertEqual(app.convert_to_seconds('00:30:32'), 1832, 'Failed get convert test 1')
        self.assertEqual(app.convert_to_seconds('01:15:00'), 4500, 'Failed get convert test 2')
        self.assertEqual(app.convert_to_seconds('03:03:03'), 10983, 'Failed get convert test 3')


    def test_validate_athlete(self):
        ''' Tests validate athelete function '''

        a, b = app.validate_athlete('Logan', '1', {'Logan':'', 'Joe':''}, {'John':'', 'Joe':''})
        self.assertEqual(a, 'Logan', 'Failed validate athlete test 1')
        self.assertEqual(b, '1', 'Failed validate athlete test 2')

        a, b = app.validate_athlete('John', '2', {'Logan':'', 'Joe':''}, {'John':'', 'Gigi':''})
        self.assertEqual(a, 'John', 'Failed validate athlete test 3')
        self.assertEqual(b, '2', 'Failed validate athlete test 4')


    def test_sort_practice_competition(self):
        ''' Tests sort practice competition function '''
        
        # [Name, Prac/Comp, Date, Duration, Run/Track, miles/reps]
        x = {'Logan': [['Logan','1','01/01/2020','300','2','5'], ['Logan','2','01/02/2020','200','2','6']]}
        
        # c_duration, c_unit, c_date, p_duration, p_unit, p_date
        a,b,c,d,e,f = app.sort_practice_competition('Logan', x)
        
        self.assertEqual(a, [6], 'Failed sort p/c test 1')
        self.assertEqual(b, [200], 'Failed sort p/c test 2')
        self.assertEqual(c, ['01/02/2020'], 'Failed sort p/c test 3')
        self.assertEqual(d, [5], 'Failed sort p/c test 4')
        self.assertEqual(e, [300], 'Failed sort p/c test 5')
        self.assertEqual(f, ['01/01/2020'], 'Failed sort p/c test 6')


    def test_sort(self):
        ''' Tests sort function '''

        a,b,c = app.sort([912, 312, 432], [3, 12, 4], ['01/01/2020', '01/02/2020', '01/03/2020'])

        self.assertEqual(a, [312,432,912], 'Failed sort test 1')
        self.assertEqual(b, [12,4,3], 'Failed sort test 2')
        self.assertEqual(c, ['01/02/2020','01/03/2020','01/01/2020'], 'Failed sort test 3')


if __name__ == "__main__":
    unittest.main(exit=False)