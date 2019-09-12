def check_legal(s1, s2):
    count = 0
    for a, b in zip(s1, s2):
        if a != b:
            count += 1
        if count > 1:
            return False
    return count == 1

