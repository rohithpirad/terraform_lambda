def handler(event, context):
    message = "successfully invoked api gateway!!".format(event.get("key"))
    return {'status': 200, 'message': message}
