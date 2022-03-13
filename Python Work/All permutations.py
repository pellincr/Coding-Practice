from itertools import permutations

#all_permutations: string -> list-of-strings
#purpose: to output all the permutations of a given string
def all_permutations(str):
    return ["".join(p) for p in permutations(str)]


if __name__ == "__main__":
    print(all_permutations("abc"))
#test