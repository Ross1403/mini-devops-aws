import json
import unittest
from lambda_function import lambda_handler


class TestLambda(unittest.TestCase):

    def test_saludo(self):
        evento = {
            "queryStringParameters": {
                "nombre": "Pedro"
            }
        }

        respuesta = lambda_handler(evento, None)
        cuerpo = json.loads(respuesta["body"])

        self.assertEqual(respuesta["statusCode"], 200)
        self.assertEqual(
            cuerpo["mensaje"],
            "Hola Pedro, bienvenido a DevOps!"
        )


if __name__ == "__main__":
    unittest.main()
