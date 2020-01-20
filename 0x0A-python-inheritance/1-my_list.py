class MyList(list):
    def print_sorted(self):
        a = self[:]
        a.sort()
        print(a)
