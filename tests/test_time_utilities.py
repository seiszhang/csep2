import datetime
from unittest import TestCase
from csep.utils.time import strptime_to_utc_datetime, datetime_to_utc_epoch, utc_epoch_time_from_strptime, epoch_time_to_utc_datetime


class TestTimeUtilities(TestCase):

    def test_strptime_to_utc_datetime(self):
        timestring = '1984-04-24 21:15:18.760'
        # note, the microseconds. .760 = 760000 microseconds
        dt_test = datetime.datetime(1984,4,24,21,15,18,760000, tzinfo=datetime.timezone.utc)
        dt = strptime_to_utc_datetime(timestring)
        self.assertEqual(dt, dt_test)

    def test_datetime_to_utc_epoch(self):
        epoch = datetime.datetime(1970,1,1)
        test_time = datetime_to_utc_epoch(epoch)
        self.assertEqual(test_time, 0)

    def test_datetime_to_utc_epoch_one_year(self):
        epoch = datetime.datetime(1970,1,1,1,0,0,0)
        test_time = datetime_to_utc_epoch(epoch)
        self.assertEqual(test_time, 60*60*1000)

    def test_utc_epoch_time_from_strptime(self):
        timestring = '1970-1-1 0:0:0.0'
        test_time = utc_epoch_time_from_strptime(timestring)
        self.assertEqual(test_time, 0)

    def test_for_consistency_epoch_to_epoch(self):
        epoch = 709732845000.0
        test_epoch = datetime_to_utc_epoch(epoch_time_to_utc_datetime(epoch))
        self.assertEqual(epoch, test_epoch)

    def test_for_consistency_dt_to_dt(self):
        dt = datetime.datetime(1984,4,24,21,15,18,760000, tzinfo=datetime.timezone.utc)
        dt_test = epoch_time_to_utc_datetime(datetime_to_utc_epoch(dt))
        self.assertEqual(dt, dt_test)
