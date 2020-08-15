ic = 1000
vp = 10000
n = 4
keys = [2, 4, 8, 2]


def get_degree(keys):

    deg = {}
    max_deg = 0
    for key in keys:
        div_ct = 0
        if not deg.get(key):
            for i in keys:
                if key%i == 0:
                    div_ct += 1
            deg[key] = div_ct
            max_deg = max(max_deg, div_ct)
    return max_deg

max_deg = get_degree(keys)
encrypt_str = max_deg * pow(10, 5)
hijack_keys = ic * vp

if encrypt_str < hijack_keys:
    print(1, encrypt_str)
else:
    print(0, encrypt_str)

