import os
import pickle
from config import DIR_NAME


def dump_extract_table(orgfile, orgtext, whole_table):
    with open(os.path.join(DIR_NAME, "origin_file.pickle"), 'wb') as f:
        pickle.dump(orgfile, f)
    with open(os.path.join(DIR_NAME, "origin_text.pickle"), 'wb') as f:
        pickle.dump(orgtext, f)
    with open(os.path.join(DIR_NAME, "whole_table.pickle"), 'wb') as f:
        pickle.dump(whole_table, f)


def dump_constituent_unit(form_conts, form_funcs, lemma, xpostag, chunktag, error, bi_chunktag):
    with open(os.path.join(DIR_NAME, "form_conts.pickle"), 'wb') as f:
        pickle.dump(form_conts, f)
    with open(os.path.join(DIR_NAME, "form_funcs.pickle"), 'wb') as f:
        pickle.dump(form_funcs, f)
    with open(os.path.join(DIR_NAME, "lemma.pickle"), 'wb') as f:
        pickle.dump(lemma, f)
    with open(os.path.join(DIR_NAME, "xpostag.pickle"), 'wb') as f:
        pickle.dump(xpostag, f)
    with open(os.path.join(DIR_NAME, "chunktag.pickle"), 'wb') as f:
        pickle.dump(chunktag, f)
    with open(os.path.join(DIR_NAME, "error.pickle"), 'wb') as f:
        pickle.dump(error, f)
    with open(os.path.join(DIR_NAME, "bi_chunktag.pickle"), 'wb') as f:
        pickle.dump(bi_chunktag, f)


def dump_match_id(id_dict_list):
    with open(os.path.join(DIR_NAME, "id_dict_list.pickle"), 'wb') as f:
        pickle.dump(id_dict_list, f)


def dump_reverse_id(reverse_id_list):
    with open(os.path.join(DIR_NAME, "reverse_id_list.pickle"), 'wb') as f:
        pickle.dump(reverse_id_list, f)


def dump_match_uposrel(old_uposrel_list):
    with open(os.path.join(DIR_NAME, "uposrel_list.pickle"), 'wb') as f:
        pickle.dump(old_uposrel_list, f)


def dump_save_heads_info(old_head_list, old_upos_list, old_rel_list):
    with open(os.path.join(DIR_NAME, "old_head_list.pickle"), 'wb') as f:
        pickle.dump(old_head_list, f)
    with open(os.path.join(DIR_NAME, "old_upos_list.pickle"), 'wb') as f:
        pickle.dump(old_upos_list, f)
    with open(os.path.join(DIR_NAME, "old_rel_list.pickle"), 'wb') as f:
        pickle.dump(old_rel_list, f)


def dump_save_heads_supplements(upostag, heads, deprel):
    with open(os.path.join(DIR_NAME, "upostag.pickle"), 'wb') as f:
        pickle.dump(upostag, f)
    with open(os.path.join(DIR_NAME, "heads.pickle"), 'wb') as f:
        pickle.dump(heads, f)
    with open(os.path.join(DIR_NAME, "deprel.pickle"), 'wb') as f:
        pickle.dump(deprel, f)

