from lib.builders.builder import TrainBuilder
from lib.analyzers.analyzer import Analyzer


class Agent:
    def run(self, config):
        dataset = TrainBuilder(config).build()
        analyzer = Analyzer(config)
        analyzer.verify(dataset)
