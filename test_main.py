"""
The test main module does the following:
1. The connection to the database server function is tested here.
2. It also tests the query function in the mylib/query.py module.
3. It finally tests the main function in the main.py module.

"""
from mylib.query import query
from mylib.mydbconn import setConn
from main import main
import unittest


# load the data
results = query()
myConn = setConn()


# test the data
class TestMain(unittest.TestCase):
    def test_conn(self):
        # assert if the connection is set
        self.assertEqual("Success", myConn[1])

    def test_col_exist(self):
        message = "column names does not exist"
        # assert if columns exist
        assert {"companyname", "totalpurchaseamount"}.issubset(results.columns), message

    def test_main(self):
        # assert if the main function is running
        self.assertEqual(main(), "Success")


if __name__ == "__main__":
    unittest.main()
