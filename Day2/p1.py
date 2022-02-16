fin = open("input.txt")
T = int(fin.readline())
with open("output.txt", "w") as fout:
    for t in range(1, T+1):
        n = int(fin.readline())
        tribes = dict()
        for i in range(n):
            s = fin.readline().split(' ')
            tribe = s[0]
            name = ' '.join(s[1:])
            if tribes.get(tribe) is None:
                tribes[tribe] = set([name])
            else:
                tribes[tribe].add(name)
        tribe_keys = list(tribes.keys())
        tribe_keys.sort()
        fout.write(f"Case: {t}\n")
        for key in tribe_keys:
            fout.write( f"{key} {len(tribes[key])}\n")
