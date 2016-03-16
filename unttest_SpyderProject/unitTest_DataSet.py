import unittest

def load_src(name, fpath):
    import os, imp
    p = fpath if os.path.isabs(fpath) \
        else os.path.join(os.path.dirname(__file__), fpath)
    return imp.load_source(name, p)


load_src("anlzr", "../SpyderProject/demo.py")

import anlzr
from anlzr import loadData

class TestAnalyzrMethods(unittest.TestCase):

 def test_poistive_dataLoad(self):
      #specify file path
      file = 'ds1.csv'

      #Execution
      dataFrameTest = anlzr.loadData(file)   
      
      #Asserts
      self.assertIsNotNone(dataFrameTest)
      self.assertEqual(len(dataFrameTest),151)
 
 def test_negative_UnsuportedExtensiondataLoad(self):
      #specify file path
      file = 'ds1Excl.xlsx'

      #Execution
      dataFrameTest = anlzr.loadData(file)   
      
      #Asserts
      #If file extension is not csv then the returned data frame must be null.
      self.assertIsNone(dataFrameTest)


#if __name__ == '__main__':
#    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestAnalyzrMethods)
unittest.TextTestRunner(verbosity=4).run(suite)