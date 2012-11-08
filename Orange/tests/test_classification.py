import unittest
import numpy as np

from Orange import data
import Orange.classification.naive_bayes as nb

class NaiveBayesTest(unittest.TestCase):

    def test_NaiveBayes(self):
        nrows = 1000
        ncols = 10
        x = np.random.random_integers(1, 3, (nrows, ncols))
        col = np.random.randint(ncols)
        y = x[:nrows,col].reshape(nrows,1)+100

        x1, x2 = np.split(x,2);
        y1, y2 = np.split(y,2);
        t = data.Table(x1, y1)
        learn = nb.BayesLearner()
        clf = learn(t)
        z = clf(x2)
        self.assertTrue((z.reshape((-1,1))==y2).all())

    def test_class_variable(self):
        nrows = 20
        ncols = 10
        x = np.random.random_integers(1, 3, (nrows, ncols))

        # multiple class variables
        y = np.random.random_integers(10, 11, (nrows, 2))
        t = data.Table(x, y)
        learn = nb.BayesLearner()
        with self.assertRaises(TypeError):
            clf = learn(t)

        # single class variable
        y = np.random.random_integers(10, 11, (nrows, 1))
        t = data.Table(x, y)
        learn = nb.BayesLearner()
        clf = learn(t)

        # TODO
        # test with a classifier that supports mmultiple class vars
