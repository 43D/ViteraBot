class Observer:
    def __init__(self, action_class):
        self._action_class = action_class

    def update(self, message):
        self._action_class.do_action(message)