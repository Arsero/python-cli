import unittest
import os
from todo import commands


class TestTodoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commands.filename = "./test_tasks.txt"

    @classmethod
    def tearDownClass(cls):
        os.remove(commands.filename)

    def setUp(self):
        commands.clear()

    def test_add_load(self):
        commands.add("hello")
        commands.add("hello")
        tasks = commands.load_tasks(commands.filename)
        self.assertEqual(len(tasks), 2)

    def test_clear(self):
        commands.add("hello")
        commands.clear()
        tasks = commands.load_tasks(commands.filename)
        self.assertEqual(len(tasks), 0)

    def test_done(self):
        commands.add("hello")
        commands.done(0)
        tasks = commands.load_tasks(commands.filename)
        self.assertEqual(tasks[0].done, True)

    def test_remove(self):
        commands.add("hello")
        commands.remove(0)
        tasks = commands.load_tasks(commands.filename)
        self.assertEqual(len(tasks), 0)

    def test_remove_done(self):
        commands.add("hello")
        commands.add("hello")
        commands.add("hello")
        commands.done(0)
        commands.done(1)
        commands.remove_done()
        tasks = commands.load_tasks(commands.filename)
        self.assertEqual(len(tasks), 1)


if __name__ == '__main__':
    unittest.main()
