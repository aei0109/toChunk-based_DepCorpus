"""
[ new_table ]
Generate new table with each column lists.

:saved file:
chunk_dep_corpus.conllc
"""
from load_pickle import load_origin_info
from load_pickle import load_form, load_lemma, load_xpostag, load_chunktag, load_bi_error
from load_pickle import load_define_supplements


def save_corpus():
    origin_file, origin_text = load_origin_info()
    form_conts, form_funcs = load_form()
    lemma = load_lemma()
    xpostag = load_xpostag()
    chunktag = load_chunktag()
    upostag, heads, deprel = load_define_supplements()

    with open("chunk_dep_corpus.conllc", 'a', encoding='utf-8') as chunk_dep_corpus:
        for sent_id, (org_file, org_sent, fc_s, ff_s, l_s, u_s, x_s, c_s, h_s, d_s)\
                in enumerate(zip(origin_file, origin_text, form_conts, form_funcs, lemma, upostag, xpostag, chunktag, heads, deprel), 1):
            chunk_dep_corpus.write("# sent_id = " + str(sent_id) + "\n")
            chunk_dep_corpus.write("# file = " + org_file + "\n")
            chunk_dep_corpus.write("# text = " + org_sent + "\n")
            chunk_dep_corpus.write("ID\tFORM(conts)\tFORM(func)\tLEMMA\tUPOSTAG\tXPOSTAG\tCHUNKTAG\tHEADS\tDEPREL\n")
            for id, (fc, ff, l, u, x, c, h, d) in enumerate(zip(fc_s, ff_s, l_s, u_s, x_s, c_s, h_s, d_s), 1):
                chunk_dep_corpus.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(id, '_'.join(fc), '_'.join(ff), ' '.join(l), u, '+'.join(x), '+'.join(c), h, d))
            chunk_dep_corpus.write("\n\n")


def save_error():
    _, origin_text = load_origin_info()
    bi_chunktag, error = load_bi_error()
    form_conts, form_funcs = load_form()
    with open("BI_error.sent", 'a', encoding='utf-8') as error_corpus:
        for sent_id, (org_sent, fc_s, ff_s, bi_sent, err_sent) in enumerate(zip(origin_text, form_conts, form_funcs, bi_chunktag, error), 1):
            error_corpus.write("# sent_id = " + str(sent_id) + "\n")
            error_corpus.write("# text = " + org_sent + "\n")
            for id, (fc, ff, bi, err) in enumerate(zip(fc_s, ff_s, bi_sent, err_sent), 1):
                error_corpus.write("{}\t{}\t{}\t{}\t{}\n".format(id, '_'.join(fc), '_'.join(ff), ' '.join(bi), ''.join(err)))
            error_corpus.write("\n\n")


def temp_error():
    """
    오류 수정을 용이하게 하기 위해 출력물을 만들어 주는 함수
    :return:
    """
    _, origin_text = load_origin_info()
    bi_chunktag, error = load_bi_error()
    form_conts, form_funcs = load_form()
    xpostag = load_xpostag()
    chunktag = load_chunktag()
    with open("test_error_xc.sent", 'a', encoding='utf-8') as file:
        for sent_id, (org_sent, fc_s, ff_s, x_s, c_s, bi_s, err_s) in enumerate(
                zip(origin_text, form_conts, form_funcs, xpostag, chunktag, bi_chunktag, error), 1):
            file.write("# sent_id = " + str(sent_id) + "\n")
            file.write("# text = " + org_sent + "\n")
            # file.write("ID\tFORM(conts)\tFORM(func)\tHEADS\tBI_CHUNK\tERROR\n")
            for id, (fc, ff, x, c, bi, err) in enumerate(zip(fc_s, ff_s, x_s, c_s, bi_s, err_s), 1):
                file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(id, '_'.join(fc), '_'.join(ff), '+'.join(x), '+'.join(c), ' '.join(bi), ''.join(err)))
            file.write("\n\n")


if __name__ == "__main__":
    temp_error()

