"""
[ select_head ]
Select the head of each constituent.
Save UPOSTAG, HEAS, DEPREL in original table format.

:dumped pickle files:
save_heads_info(): old_head_list, old_upos_list, old_rel_list
"""
import dump_pickle
from load_pickle import load_match_id, load_match_uposrel  # id_dict_list, uposrel_list

# id_dict = {new_id_1: [old_id_1, old_id_2], new_id_2: [old_id_3]}
# reverse_id_dict = {old_id_1: new_id_1, old_id_2: new_id_1, old_id_3: new_id_2}
# uposrel_dict = {old_id_1: [LEMMA, UPOSTAG, HEADS, DEPREL]}


def save_heads_info():
    old_head_list = []
    old_upos_list = []
    old_rel_list = []
    id_dict_list = load_match_id()
    uposrel_list = load_match_uposrel()
    for sent_id, (id_sent, uposrel_sent) in enumerate(zip(id_dict_list, uposrel_list), 1):
        head_of_content = []
        upos_of_content = []
        rel_of_content = []
        i = 1
        # 한 문장 단위
        # print("# sent_id:", sent_id)
        for new_id, old_id in zip(id_sent, uposrel_sent):
            const_id = []  # old_id를 구성성분 단위로 저장
            const_head = {}  # head 선별 시 사용할 리스트.
                             # 한 구성성분 안에 head인 old_id가 있으면 이는 핵심어의 head가 아니다. ex)[2, 16, '_']
            # 한 구성성분(한 행) 단위
            for new_old_id in id_sent[new_id]:  # id_sent[new_id]: [1, 2, 3]
                const_id.append(i)  # i: old_id, const_id = [1, 2, 3]
                i += 1
                if uposrel_sent[new_old_id][0] in ['"',"'",'(',')','{','}','[',']']:  # LEMMA가 쌍이 있는 기호이면
                    # const_head.append('_')  # head로 선정 안 하기 위해 underbar로 대체
                    const_head.update({'_': '_'})
                else:
                    const_head.update({uposrel_sent[new_old_id][2]: [uposrel_sent[new_old_id][1], uposrel_sent[new_old_id][3]]})

                    # uposrel_sent[new_old_id][2]: HEADS, ['2', '16', '_']
                    # uposrel_sent[new_old_id][1]: UPOSTAG, [PROPN, PROPN, PUNCT]
                    # uposrel_sent[new_old_id][3]: DEPREL, [nmod, nsubj, punct]

            # print("const_head:", const_head)  # const_head = [2, 16, '_']
            for c_h in const_head:  # 핵심어의 head 선별하는 과정
                try:
                    c_h = int(c_h)
                except ValueError:  # c_h == '_'
                    pass

                # head 를 선발하는 곳
                # const_id = [1, 2, 3]
                # print("c_h:", c_h)
                # print("const_id:", const_id)
                if c_h in const_id:  # head가 한 구성성분 안에 있으므로 head 아님. pass
                    pass
                elif c_h == '_':  # 쌍이 있는 기호 자리. pass
                    pass
                else:
                    head_of_content.append(c_h)  # head_of_content: old_head 중 핵심어의 head만 선별한 list  # c_h: 16
                    print("head_of_content:", head_of_content)

                    c_h = str(c_h)
                    upos_of_content.append(const_head[c_h][0])
                    rel_of_content.append(const_head[c_h][1])
                input()

        old_head_list.append(head_of_content)  # head_of_content: [10, 3, 9, 5, 6, 7, 8, 9, 10, 0]
        old_upos_list.append(upos_of_content)
        old_rel_list.append(rel_of_content)

    dump_pickle.dump_save_heads_info(old_head_list, old_upos_list, old_rel_list)
