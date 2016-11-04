from sys import maxsize


class Subjects:

    def __init__(self, screening = None, temporary_id = None, initials = None,
                 id = None, comments = None):
        self.screening = screening
        self.temporary_id = temporary_id
        self.initials = initials
        self.comments = comments
        self.id = id



    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.screening, self.temporary_id, self.initials, self.comments)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.screening == other.screening or self.temporary_id == other.temporary_id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize