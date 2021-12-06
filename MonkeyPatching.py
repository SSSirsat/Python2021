class MonkeyPatch:
    def inside(self):
        print("This is inside Function")

def outside():
    print("This is outside function")

print(MonkeyPatch().inside())

MonkeyPatch.inside = outside
print(MonkeyPatch.inside())
