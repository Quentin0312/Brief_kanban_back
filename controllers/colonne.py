import hug

@hug.post('/')
def createColumn(body):
    columnTitle = body['columnTitle']
    return columnTitle + " post"

@hug.put('/')
def modifyColumn(body):
    columnTitle = body['columnTitle']
    return columnTitle + " put"

@hug.get('/{column_id}')
def modifyColumn(column_id:int):
    return str(column_id) + " get"