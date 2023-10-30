# don't have to work in a class, can just write code in the file
color_list = ["red", "blue"]
print(color_list)

# classes don't need to be in their own files; can have multiple classes and code in one file
class ElectionRecord:
    # set up constructor, which also sets up the fields/instance variables
    def __init__(self, name : str, candidates : list):
        self.name = name  # creates field and sets the value
        self.candidates = candidates
        self.votes = list() # could also write []

    # this is the equivalent of toString in Java; Python needs the __str__ name
    def __str__(self) -> str:
        return str(self.name) + " has " + str(len(self.votes)) + " votes"

    # this is a regular method, rather than one Python looks for, so no __ in name
    # note that every method takes self as a first arg (self is akin to this in Java)
    def cast_vote(self, for_cand: str):
        if for_cand in self.candidates:
            self.votes.append(for_cand) # append is the mutable operation on lists, + is immutable
        else: raise("Unknown candidate " + str(for_cand))

    def count_votes_for(self, for_cand: str) -> int:
        total = 0
        for v in self.votes:
            if v == for_cand:
                total = total + 1
        return total

# the class ends when Python finds a line of code that is NOT indented within the class
e = ElectionRecord("Choose colors", color_list)
print(str(e))
e.cast_vote("red")
e.cast_vote("blue")
e.cast_vote("red")
print(str(e))

# Here to let us interact with the program; we'll discuss this next time
pass