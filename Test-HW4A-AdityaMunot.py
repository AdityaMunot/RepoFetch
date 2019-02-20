import unittest

from HW4A_AdityaMunot import Repocheck


class testrepos(unittest.TestCase):

    def testrepos(self):
        repos = Repocheck('AdityaMunot')
        expect = [['Anagram-Variety', 14], ['hello-world', 3], ['RepoFetch', 15], ['Repositoryprogram', 9], ['SSW-555-Group-Project', 13], ['SSW567', 1], ['Triangle567', 6]]
        self.assertEqual(repos, expect)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
