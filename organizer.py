from classifier import Classifier
from mover import Mover


class Organizer:

    def build(self, files):

        grouped = Classifier().group(files)

        return Mover().organize(grouped)
