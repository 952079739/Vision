from flask_socketio import emit


def register_comment(socketio):
    namespace = "/comment"

    @socketio.on('startmessage', namespace=namespace)
    def pause_message(message):
        emit('message', {'data': message['data']}, broadcast=True, namespace=namespace)

    @socketio.on('pausemessage', namespace=namespace)
    def pause_message(message):
        emit('message', {'data': message['data']}, broadcast=True, namespace=namespace)

    @socketio.on('imessage', namespace=namespace)
    def test_message(message):
        emit('message', {'data': message['data']}, broadcast=True, namespace=namespace)

    @socketio.on('connect', namespace=namespace)
    def connected_msg():
        """socket client event - connected"""
        socketio.emit('message', {'data': '1'}, broadcast=True, namespace=namespace)
        print('client connected!')

    @socketio.on('disconnect', namespace=namespace)
    def disconnect_msg():
        """socket client event - disconnected"""
        socketio.emit('message', {'data': '系统消息：有人离开了！！！'}, broadcast=True, namespace=namespace)
        print('client disconnected!')

