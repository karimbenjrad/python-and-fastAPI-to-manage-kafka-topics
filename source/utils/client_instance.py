class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        try:
            return self._instance

        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError("Singletons must be accessed through instance()")

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class KafkaClient:
    def __init__(self):
        self.kafka_client = None

    def __str__(self):
        return "Initiating models"


kafka_client = KafkaClient.instance()
