"""
[ define supplements ]
Select the right UPOSTAG and DEPREL depend on HEADS through reverse_id_list.

:dumped pickle files:
save_heads_supplements(): upostag, heads, deprel
UPOSTAG: upostag.pickle
HEADS: heads.pickle
DEPREL: deprel.pickle
"""
from load_pickle import load_select_head, load_reverse_id  # old_head_list, old_upos_list, old_rel_list, reverse_id_list
import dump_pickle

upostag = []
heads = []
deprel = []


def save_heads_supplements():
    old_head_list, old_upos_list, old_rel_list = load_select_head()
    reverse_id_list = load_reverse_id()
    for old_head_sent, old_upos_sent, old_rel_sent, id_sent \
            in zip(old_head_list, old_upos_list, old_rel_list, reverse_id_list):
        upostag_sent = []
        heads_sent = []
        deprel_sent = []
        for head, upos, rel in zip(old_head_sent, old_upos_sent, old_rel_sent):
            if head == 0:  # 기존 table의 head가 0(root)일 때
                upostag_sent.append(upos)
                heads_sent.append('0')
                deprel_sent.append(rel)
            else:
                head = str(head)
                upostag_sent.append(upos)
                heads_sent.append(id_sent[head])
                deprel_sent.append(rel)
        upostag.append(upostag_sent)
        heads.append(heads_sent)
        deprel.append(deprel_sent)

    dump_pickle.dump_save_heads_supplements(upostag, heads, deprel)

