"""
[ toChunk-based_DepCorpus ]
morpheme-based dependency corpus를 chunk-based dependency corpus로 변환하는 프로그램
2019-06-13
2019-06-24_ver.2.0.0
2019-07-09_ver.3.0.0
Y. Namgoong

< modification >
:heads.pickle: root('0') str -> int
:toConstituent: modularization
"""
import os
from config import DIR_NAME

from toConstituent import read_file, extract_table, constituent_unit, save_supplements
from dictionary_functions import match_id, match_uposrel, reverse_id
from select_head import save_heads_info
from define_supplements import save_heads_supplements
from new_table import save_corpus, save_error, temp_error


if __name__ == "__main__":
    if not os.path.isdir(DIR_NAME):
        os.mkdir(DIR_NAME)

    dep_corp, chk_corp, mor_corp = read_file()

    extract_table(dep_corp)
    constituent_unit(chk_corp, mor_corp)
    save_supplements()  # form_conts, form_funcs, lemma, xpostag, chunktag, error, bi_chunktag

    match_id()  # id_dict_list
    match_uposrel()  # uposrel_list

    reverse_id()  # reverse_id_list
    save_heads_info()  # old_head_list, old_upos_list, old_rel_list

    save_heads_supplements()  # upostag, heads, deprel

    save_error()  # BI_error.sent
    save_corpus()  # chunk_dep_corpus.conllc
    temp_error()  # test_error_xc.sent
