from searcher.factory.abstractfactory import Factory
from searcher.search.indeedsearch import Indeed

class IndeedFactory(Factory):
    def create(self):
        return Indeed()


