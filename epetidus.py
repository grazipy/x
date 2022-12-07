def remove_repetidos(l):
    l.sort()
    no_reps = []
    for e in l:
        if e not in no_reps:
            no_reps.append(e)
    return no_reps

