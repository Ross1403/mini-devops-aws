import json

def lambda_handler(event, context):
    parametros = event.get("queryStringParameters") or {}
    nombre = parametros.get("nombre") or "mundo"

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "mensaje": f"Hola {nombre}, bienvenido a DevOps!"
        })
    }
