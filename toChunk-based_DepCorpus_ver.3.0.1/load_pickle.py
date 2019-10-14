import os
import pickle
from config import DIR_NAME


########################################################################################################################
# [toConstituent]-[extract_table]
def load_whole_table():
    # [[1, ..., _], [2, ..., _], ..., [n, ..., _]]
    with open(os.path.join(DIR_NAME, "whole_table.pickle"), 'rb') as f:
        whole_table = pickle.load(f)
    return whole_table


def load_origin_info():
    with open(os.path.join(DIR_NAME, "origin_file.pickle"), 'rb') as f:
        origin_file = pickle.load(f)
    with open(os.path.join(DIR_NAME, "origin_text.pickle"), 'rb') as f:
        origin_text = pickle.load(f)
    return origin_file, origin_text


########################################################################################################################
# [toConstituent]-[constituent_unit]
def load_form():
    with open(os.path.join(DIR_NAME, "form_conts.pickle"), 'rb') as f:
        form_conts = pickle.load(f)
    with open(os.path.join(DIR_NAME, "form_funcs.pickle"), 'rb') as f:
        form_funcs = pickle.load(f)
    return form_conts, form_funcs


def load_lemma():
    # [['한데'], ['요즈음', '도시', '의'], ..., ['딱하', '기', '만', '하', '다', '.']]
    with open(os.path.join(DIR_NAME, "lemma.pickle"), 'rb') as f:
        lemma = pickle.load(f)
    return lemma


def load_xpostag():
    with open(os.path.join(DIR_NAME, "xpostag.pickle"), 'rb') as f:
        xpostag = pickle.load(f)
    return xpostag


def load_chunktag():
    with open(os.path.join(DIR_NAME, "chunktag.pickle"), 'rb') as f:
        chunktag = pickle.load(f)
    return chunktag


def load_bi_error():
    with open(os.path.join(DIR_NAME, "bi_chunktag.pickle"), 'rb') as f:
        bi_chunktag = pickle.load(f)
    with open(os.path.join(DIR_NAME, "error.pickle"), 'rb') as f:
        error = pickle.load(f)
    return bi_chunktag, error


########################################################################################################################
# [dictionary_functions]
def load_match_id():
    # [dictionary_functions]
    # id_dict = {new_id_1: [old_id_1, old_id_2], new_id_2: [old_id_3]}
    with open(os.path.join(DIR_NAME, "id_dict_list.pickle"), 'rb') as f:
        id_dict_list = pickle.load(f)
    return id_dict_list


def load_reverse_id():
    # reverse_id_dict = {old_id_1: new_id_1, old_id_2: new_id_1, old_id_3: new_id_2}
    with open(os.path.join(DIR_NAME, "reverse_id_list.pickle"), 'rb') as f:
        reverse_id_list = pickle.load(f)
    return reverse_id_list


def load_match_uposrel():
    # uposrel_dict = {old_id_1: [LEMMA, UPOSTAG, HEADS, DEPREL]}
    with open(os.path.join(DIR_NAME, "uposrel_list.pickle"), 'rb') as f:
        uposrel_list = pickle.load(f)
    return uposrel_list


########################################################################################################################
# [select_head]
def load_select_head():
    # [select_head]
    with open(os.path.join(DIR_NAME, "old_head_list.pickle"), 'rb') as f:  # [2, 0]
        old_head_list = pickle.load(f)
    with open(os.path.join(DIR_NAME, "old_upos_list.pickle"), 'rb') as f:  # ['NOUN', 'VERB']
        old_upos_list = pickle.load(f)
    with open(os.path.join(DIR_NAME, "old_rel_list.pickle"), 'rb') as f:   # ['nmod', 'root']
        old_rel_list = pickle.load(f)
    return old_head_list, old_upos_list, old_rel_list


########################################################################################################################
# [define_supplements]
def load_define_supplements():
    # [define_supplements]
    with open(os.path.join(DIR_NAME, "upostag.pickle"), 'rb') as f:    # ['NOUN', 'VERB']
        upostag = pickle.load(f)
    with open(os.path.join(DIR_NAME, "heads.pickle"), 'rb') as f:      # [2, '0']
        heads = pickle.load(f)
    with open(os.path.join(DIR_NAME, "deprel.pickle"), 'rb') as f:     # ['nmod', 'root']
        deprel = pickle.load(f)
    return upostag, heads, deprel


########################################################################################################################
def open_pickle():
    """
    This function is for checking the contents of the saved pickle file directly.
    """
    print("deprel")
    _, _, deprel = load_define_supplements()
    for i, ele in enumerate(deprel, 1):
        print(i, ele)
        if i % 12 == 0:
            input()


if __name__ == "__main__":
    open_pickle()
