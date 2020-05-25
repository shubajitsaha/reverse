import unittest
from reverse import *

class TestRevrseFile(unittest.TestCase):
    def setUp(self):
        self.ip_file = 'temp.txt'
        self.text = 'apple\ncat\n123\n!234#$%^'
        self.setup_file(self.ip_file)
        self.mod = reverse.ReverseFile(self.ip_file,sep='\n')
        
        
    def setup_file(self,fname):
        with open(fname,'w') as fop:
            fop.write(self.text)
            
    def test_init(self):
        self.assertRaises(ValueError,reverse.ReverseFile,self.ip_file,sep='app')
                
    def test_split(self):
        text = 'apple\ncat\n123\n!234#$%^'
        
        self.assertListEqual(self.mod._split(text),['apple','cat','123','!234#$%^'],"_split Method Failed.")
    
    def test_reverse(self):
        text = 'apple\ncat'
        ground_truth = 'tac\nelppa'
        revrse_text = self.mod._reverse(text)
        
        self.assertEqual(ground_truth,revrse_text,"_reverse Method Failed.")
        
    def test_join(self):
        text_list = ['apple','\ncat']
        ground_truth = 'apple\n\ncat'
        joined_text = self.mod._join(text_list)
        
        self.assertEqual(ground_truth,joined_text,"_join Method Failed.")
        
    def test_workflow(self):
        ground_truth = 'elppa\ntac\n321\n^%$#432!'
        revrese_text = self.mod.reverse()
        
        self.assertEqual(ground_truth,revrese_text,"reverse Workflow Failed.")
                
if __name__ == '__main__':
    unittest.main()