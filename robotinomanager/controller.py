from robotinomanager import sockets

@sockets.route('/control')
def control(ws):
    while not ws.closed:
        message = ws.receive()
        if message is None:  # message is "None" if the client has closed.
            continue
        # Send the message to all clients connected to this webserver
        # process. (To support multiple processes or instances, an
        # extra-instance storage or messaging system would be required.)
        clients = ws.handler.server.clients.values()
        for client in clients:
            client.ws.send(message)
