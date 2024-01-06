import unittest
from unittest.mock import patch
from io import StringIO
import pygame1

class pygameTestCase(unittest.TestCase):
    def setUp(self):
        pygame1.reset_counter()
        pygame1.word()

    def test_counter_down(self):
        pygame1.counter_down()
        self.assertEqual(pygame1.counter, 6)

    def test_reset_counter(self):
        pygame1.counter = 3
        pygame1.reset_counter()
        self.assertEqual(pygame1.counter, 7)

    def test_guessed_correctly(self):
        result = pygame1.guessed('a', pygame1.answer, pygame1.guessed_answer)
        self.assertTrue(result)
        self.assertIn('a', pygame1.guessed_answer)

    def test_guessed_incorrectly(self):
        result = pygame1.guessed('x', pygame1.answer, pygame1.guessed_answer)
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()