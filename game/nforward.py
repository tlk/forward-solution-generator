from game import ngame

def substitute(c):
    d = dict()
    for j in range(32):
        d[j] = ngame.sbox[c[j]]
    return list(d.values())

def permute(inp):
    out = dict()
    for j in range(32):
        out[j] = 0

    for j in range(32):
        for k in range(32):
            if (ngame.pbox[j]>>k)&1:
                out[j] = out[j] ^ inp[k]

    return list(out.values())

def mix(c):
    out = dict()
    half_length = int(len(c) / 2)
    for i in range(half_length):
        out[i] = ngame.sbox[c[i*2]] ^ ngame.sbox[c[i*2+1]+256]
    return list(out.values())

def forward_single_round(c):
    s = substitute(c)
    return permute(s)

def forward(c, rounds=256):
    for _ in range(rounds):
        c = forward_single_round(c)

    mixed = mix(c)

    return "".join([chr(letter) for letter in mixed])