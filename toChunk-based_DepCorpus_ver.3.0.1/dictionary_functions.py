"""
[ dictionary_functions ]
make dictionaries.

:dumped pickle files:
match_id(): id_dict_list
reverse_id(): reverse_id_list
match_uposrel(): old_uposrel_list
"""
import dump_pickle
from load_pickle import load_whole_table, load_match_id, load_lemma


def match_id():
    """
    make dictionary
    id_dict = {new_head_1: [old_head_1, old_head_2], new_head_2: [old_head_3]}
    :return:
    """
    # global whole_table, lemma
    whole_table = load_whole_table()
    lemma = load_lemma()

    id_dict_list = []
    for sent, lem in zip(whole_table, lemma):
        chunk_unit = []
        i = 1
        id_dict = {}
        for eojeol in sent:
            try:
                id_dict[i]
                # print("try_id_dict: ", id_dict[i])
            except KeyError:
                # print("error", file=sys.stderr)
                id_dict[i] = []

            chunk_unit.extend(eojeol[2].split())
            id_dict[i].append(eojeol[0])  # ?ㅅ? 어떻게 1부터 넣게 한거지?
            # print("id_dict[{}]: {}".format(i, id_dict[i]))

            if chunk_unit == lem[i - 1]:  # 문장성분(한 행)의 끝인지 check
                # print("chunk_unit: ", chunk_unit)
                i += 1
                chunk_unit = []
        id_dict_list.append(id_dict)

    dump_pickle.dump_match_id(id_dict_list)


def reverse_id():
    """
    {old_head_1: new_head_1, old_head_2: new_head_1, old_head_3: new_head_2}
    :return:
    """
    id_dict_list = load_match_id()
    reverse_id_list = []
    for sent in id_dict_list:
        reverse_id_dict = {}
        for old_h, new_h in sent.items():
            for each_new_h in new_h:
                reverse_id_dict[each_new_h] = old_h
        # print(reverse_id_dict)
        reverse_id_list.append(reverse_id_dict)

    dump_pickle.dump_reverse_id(reverse_id_list)


def match_uposrel():
    """
    make dictionary
    {old_head_1: [upos_1, rel_1], old_head_2: [upos_2, rel_2], old_head_3: [upos_3, rel_3]}
    :return:
    """
    whole_table = load_whole_table()

    old_uposrel_list = []
    for sent in whole_table:
        uposrel_dict = {}
        for eojeol in sent:
            # eojeol[0]: ID
            # eojeol[2]: LEMMA
            # eojeol[3]: UPOSTAG
            # eojeol[6]: HEADS
            # eojeol[7]: DEPREL
            uposrel_dict[eojeol[0]] = [eojeol[2], eojeol[3], eojeol[6], eojeol[7]]
        old_uposrel_list.append(uposrel_dict)

    dump_pickle.dump_match_uposrel(old_uposrel_list)


if __name__ == "__main__":
    # match_id()
    # reverse_id()
    match_uposrel()
