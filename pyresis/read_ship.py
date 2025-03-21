_open = open


def open(file=None):
    out = {}
    try:
        f = _open(file, "r")
    except OSError:
        return out

    lines = f.readlines()
    for line in lines:
        line = line.strip().split("#")[0].strip()
        if len(line) > 0:
            res = line.split("=")
            key, value = res[0].strip(), res[1].strip()
            out[key] = float(value)
            #self.__keys.append(key)
    return out

def edit(file=None):
    return
