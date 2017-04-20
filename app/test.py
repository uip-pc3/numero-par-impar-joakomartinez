import unittest
from app.par_impar import tipo_numero


class Testpar(unittest.TestCase):
    def test_tipo_numero(self):
        self.assertEquals(tipo_numero(4),'par')
        self.assertEquals(tipo_numero(5),'impar')

if __name__ == '__main__':
    unittest.main()
