class User:
    def __init__(self, id, name):
        # Initialize attributes
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


danny = User('01', 'Danny')
angela = User('02', 'Angela')
print(danny.name)

danny.follow(angela)

print(danny.followers)
print(danny.following)

print(angela.followers)
print(angela.following)
