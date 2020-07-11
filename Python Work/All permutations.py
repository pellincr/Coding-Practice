#all_permutations: string list -> list-of-strings
#purpose: to return all permutations of the given string
def all_permutations(string, res):
    if len(string) == 0:
        return res
    else:
        place_letter(string[0:1], all_permutations(string[1], res))

#place_letter: string list-of-strings