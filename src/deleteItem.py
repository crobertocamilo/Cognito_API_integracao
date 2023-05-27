import boto3
import json
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Paises')

def handler(event, context):

    logger.info(event)
    requestBody = event.get('body')

    if requestBody is None:
        return buildResponse(400, {'Mensagem': 'Corpo da solicitação ausente.'})

    try:
        requestBody = json.loads(event['body'])
        Pais = requestBody['Pais']
        
        table.delete_item(
            Key = {
                'Pais': Pais
            },
            ReturnValues='ALL_OLD'
        )

        body = {
            'Operação': 'DELETAR',
            'Mensagem': 'SUCESSO',
            'Item': requestBody
        }

        return buildResponse(200, body)
    
    except:
        logger.exception('Erro na tentativa de deletar o item!')
        return buildResponse(500, {'Mensagem': 'Erro ao processar a solicitação.'})

def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'ContentType': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response
