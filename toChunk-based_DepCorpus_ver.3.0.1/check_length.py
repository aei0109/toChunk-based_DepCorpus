from load_pickle import load_lemma, load_define_supplements

lemma = load_lemma()
_, heads, _ = load_define_supplements()

count = 0
for id, (l_s, h_s) in enumerate(zip(lemma, heads), 1):
    # print(l,"\n", h, "\n")
    if len(l_s) == len(h_s):
        pass
    else:
        count += 1
        print("# sent_id:", id)
        print("len(I):", len(l_s), "len(h):", len(h_s))
        for l in l_s:
            print(l)
        for h in h_s:
            print(h)
    if id % 100 == 0:
        # print(id, id % 50)
        input()

# print(id)  # 62343
# print(count)  # 15880
