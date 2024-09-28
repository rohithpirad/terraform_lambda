def handler(event, context):
    message = "event received with information {}.".format(event.get("key"))
    print(message)
    return {'message': message}
