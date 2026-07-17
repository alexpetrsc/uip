from folders import CATEGORIES


class Classifier:

    def group(
        self,
        files
    ):

        result = {}

        for file in files:

            for folder, extensions in CATEGORIES.items():

                if file.extension in extensions:

                    result.setdefault(

                        folder,

                        []

                    ).append(file)

        return result
