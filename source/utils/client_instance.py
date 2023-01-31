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
class Kafka:
    def __init__(self):
        self.kafka_client, self.kafka_consumer, self.kafka_producer = None, None, None

    def __str__(self):
        return "Initiating models"


kafka = Kafka.instance()
