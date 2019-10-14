"""
[toConstituent]
From dependency corpus, save the original file name, text and corpus table each. ~ extract_table()
Using chunk corpus and morph corpus(the results for the ChunkTagger),
arrange the morpheme information in a line by the constituent unit. ~ constituent_unit()

:dumped pickle files:
extract_table(): orgfile, orgtext, whole_table
constituent_unit(): form_conts, form_funcs, lemma, xpostag, chunktag, error, bi_chunktag
"""
import pickle
import dump_pickle

# [file path]
# dependency corpus
DEP_PATH = r"E:\Users\NLP86\Documents\세종말뭉치\DependencyCorpus\sejong-non_head_final.conll"
# chunking result file
# CHK_PATH = r"E:\Chunking\BiLSTM-CRF_Chunking_keras_ver.2.3.0\pickle\0617_02\ch_pred_sent.pickle"
# CHK_PATH = r"E:\Chunking\BiLSTM-CRF_Chunking_keras_ver.2.3.0\BI_correct\BI_correct_2.pickle"  # BI 수정한 chunktags
CHK_PATH = r"E:\Chunking\BIErrorAnalysis\correction_result\new_ch_pred_sent.pickle"  # BI 수동 수정까지 마친 chunktags
# morpheme file
MOR_PATH = r"E:\Chunking\BiLSTM-CRF_Chunking_keras_ver.2.3.0\pickle\0617_02\ch_test_sent.pickle"


def read_file():
    """
    < dependency corpus >
    #SENTID:3
    #FILE:BGAA0001.utf8.txt
    #ORGSENT:디자인 세계 넓혀
    1	디자인	디자인	NOUN	NNG	_	2	nmod	_	_
    2	세계	세계	NOUN	NNG	_	3	obj	_	_
    3	넓혀	넓히 어	VERB	VV+EC	_	0	root	_	_

    < chunking result file >
    ['B-NX', 'B-PX', 'B-EFX', 'B-SYX']

    < morpheme file >
    ['디자인/NNG', '세계/NNG', '넓히/VV', '어/EC']
    """
    with open(DEP_PATH, 'r', encoding="utf-8") as f:
        dep_corp = f.readlines()
    with open(CHK_PATH, 'rb') as f:
        chk_corp = pickle.load(f)
    with open(MOR_PATH, 'rb') as f:
        mor_corp = pickle.load(f)
    # dep_corp = open(DEP_PATH, 'r', encoding="utf-8")  # dependency corpus
    # chk_corp = pickle.load(open(CHK_PATH, 'rb'))  # chunk corpus
    # mor_corp = pickle.load(open(MOR_PATH, 'rb'))  # morpheme corpus
    return dep_corp, chk_corp, mor_corp


########################################################################################################################
# 엑셀 파일 참고
"""
필요한 container
[ extract_table(dep_corp) ]
# sent_id = the id of the sentence
# file_name = the original file name
# text = the original text

[ constituent_unit(chk_corp, mor_corp) ]
FORM(conts): content words 
FORM(func): functional words
LEMMA: morpheme unit ~ 띄어쓰기 허용 안 한다고 했는데 해 놓았음. 발표 때 언급
UPOSTAG: universal POS tags
XPOSTAG: sejong POS tags
CHUNKTAG: chunk tags
FEATS: _
HEADS: head id of the constituent
DEPREL: dependency relation of the constituent
DEPS: _
MICS: _
"""


def extract_table(dep_corp):
    """
    extract original sentences and sentence information(whole_table) from dependency corpus
    :param <type 'file_addr'> dep_corp: dependency corpus
    :file saving <type 'list'> origin_file.pickle: the origin file name of 세종 구문 태그 부착 말뭉치
                                                    <ex> ["BGAA0001.utf8.txt", ..., "..."]
    :file saving <type 'list'> origin_text.pickle: the origin text in the dependency corpus.
                                                    <ex> ["디자인 세계 넓혀", ..., "..."]
    :file saving <type 'list'> whole_table.pickle:
                                      <ex> [['1', '디자인', '디자인', 'NOUN', 'NNG', '_', '2', 'nmod', '_', '_'],
                                            ['2', '세계', '세계', 'NOUN', 'NNG', '_', '3', 'obj', '_', '_'],
                                            ['3', '넓혀', '넓히 어', 'VERB', 'VV+EC', '_', '0', 'root', '_', '_']]
    """
    orgtext = []  # contain the origin sentences(#ORGSENT).
    orgfile = []  # contain the origin file name(#FILE).
    whole_table = []  # contain the whole eojeol-based sentences.
    sent_table = []  # contain an eojeol-based sentence.
    for line in dep_corp:
        line = line.strip()
        if line:
            if line[0] == "#":
                info_title, *info_content = line.split(":")
                info_content = ''.join(info_content).strip()
                if info_title == "#FILE":
                    orgfile.append(info_content)
                elif info_title == "#ORGSENT":
                    orgtext.append(info_content)
                else: pass
            else:
                eojeol = line.split('\t')
                sent_table.append(eojeol)
                # eojeol[0]: ID
                # eojeol[2]: LEMMA
                # eojeol[3]: UPOSTAG
                # eojeol[6]: HEADS
                # eojeol[7]: DEPREL
        elif sent_table:
            whole_table.append(sent_table)
            sent_table = []

    dump_pickle.dump_extract_table(orgfile, orgtext, whole_table)


########################################################################################################################
# 변수를 전역으로 선언해야 할 듯 -> 함수로 변환 또는 가능하다면 더욱 깔금한 형태로 refactoring
# [the whole corpus]
form_conts = []
form_funcs = []
lemma = []
xpostag = []
chunktag = []
bi_chunktag = []  # for convenience

upostag = []
heads = []
deprel = []
error = []  # for convenience

# [sent]
form_conts_sent = []
form_funcs_sent = []
lemma_sent = []
xpostag_sent = []
chunktag_sent = []
bi_chunktag_sent = []  # for convenience

upostag_sent = []
heads_sent = []
deprel_sent = []
error_sent = []  # for convenience

# [line]
form_conts_line = []
form_funcs_line = []
lemma_line = []
xpostag_line = []
chunktag_line = []
bi_chunktag_line = []  # for convenience

upostag_line = []
heads_line = []
deprel_line = []
error_line = []  # for convenience


# 2)의 문장성분(-어) 단위로 한 줄씩 배치  -> chunk 내용어, 기능어 단위로 하면 될 것
def constituent_unit(chk_corp, mor_corp):
    """
    make a line by chunk unit
    말덩이 단위로 한 줄에 표현
    FORM(conts), FORM(func), LEMMA, XPOSTAG, CHUNKTAG
    :param <type 'list'> chk_corp, <type 'list'> mor_corp:
    :return:
    """
    syx_flag = 1
    for chk_sent, mor_sent in zip(chk_corp, mor_corp):
        # chk_sent: ['B-NX', 'B-PX', 'B-EFX', 'B-SYX']
        # mor_sent: ['디자인/NNG', '세계/NNG', '넓히/VV', '어/EC']
        # print("전체문장", mor_sent)
        # print("전체태그", chk_sent)
        for i, (chk, mor) in enumerate(zip(chk_sent, mor_sent)):
            ######################################################################
            # [현재 형태소 정보]
            bio_tag, chk_tag = chk.split('-')
            # //SP 구분하기 위하여
            if mor[0] == '/':
                morpheme, pos_tag = mor[0], mor[2:]
            else:
                if mor.count('/') > 1:
                    mor = mor.replace('/', '', 1)
                morpheme, pos_tag = mor.split('/')
            ######################################################################
            # print("morpheme:", morpheme)
            lemma_line.append(morpheme)
            xpostag_line.append(pos_tag)
            check_chunk_tag(chk_tag, chunktag_line)  # set쓰면 tag의 순서를 알 수 없으므로 따로 함수로 체크
            bi_chunktag_line.append(chk)
            error_line.append('')
            ######################################################################
            try:
                # [다음 형태소 정보]
                next_bio_tag, next_chk_tag = chk_sent[i+1].split('-')
                # //SP 구분하기 위하여
                if mor_sent[i+1][0] == '/':
                    next_morpheme, next_pos_tag = mor_sent[i+1][0], mor_sent[i+1][2:]
                else:
                    if mor_sent[i+1].count('/') > 1:
                        mor_sent[i+1] = mor_sent[i+1].replace('/', '', 1)
                    next_morpheme, next_pos_tag = mor_sent[i+1].split('/')
                ########################################################################
                # 한 line에 들어갈 정보
                # line ends일 경우
                # form_conts_sent.append('_'.join(form_conts_line))
                # form_funcs_sent.append('_'.join(form_funcs_line))
                # lemma_sent.append(' '.join(lemma_line))
                # xpostag_sent.append('+'.join(xpostag_line))
                # chunktag_sent.append('+'.join(chunktag_line))
                # error_sent.append(set(error_line))
                # line list 들 초기화

                if bio_tag == "B" and next_bio_tag == "B":
                    if len(chk_tag) == 2:
                        form_conts_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # B-NX, B-NX
                            form_funcs_line.append("-")
                            line_ends()
                        elif len(next_chk_tag) == 2:  # B-NX, B-PX
                            form_funcs_line.append("-")
                            line_ends()
                        elif len(next_chk_tag) == 3:  # B-NX, B-JKX
                            pass
                            # maybe ends or not. B-JKX 다음에 다른 B-내용어가 와야 end
                        else: pass  # 어떤 경우?
                    elif len(chk_tag) == 3:
                        form_funcs_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # B-JKX, B-JKX
                            # ? 있는지부터 확인, 여기서는 일단 맞다고 보고 진행
                            # line not ends
                            error_line[-1] = 'error1'
                        elif len(next_chk_tag) == 2:  # B-JKX, B-NX
                            line_ends()
                        elif len(next_chk_tag) == 3:  # B-JKX, B-JUX
                            pass # line not ends. B-JUX 다음에 다른 B-내용어가 와야 end
                        else: pass  # 어떤 경우?
                elif bio_tag == "B" and next_bio_tag == "I":
                    if len(chk_tag) == 2:
                        form_conts_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # B-NX, I-NX
                            pass  # line not ends
                        elif len(next_chk_tag) == 2:  # B-NX, I-PX
                            # ? 있는지부터 확인 -> maybe line ends
                            # form_funcs_line.append("-")  # 0715 BI error 수정 중 이 부분만 주석처리. error2 참고
                            error_line[-1] = 'error2'
                            line_ends()
                        elif len(next_chk_tag) == 3:  # B-NX, I-JKX
                            # ? 있는지 확인
                            error_line[-1] = 'error3'
                            # line not ends
                        else: pass  # 어떤 경우?
                    elif len(chk_tag) == 3:
                        form_funcs_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # B-JKX, I-JKX
                            pass # line not ends
                        elif len(next_chk_tag) == 2:  # B-JKX, I-NX
                            # ? 있는지 확인. 아마 없을 것. 없으면 pass or line_ends. 있으면 확인 후 추가
                            error_line[-1] = 'error4'
                            line_ends()
                        elif len(next_chk_tag) == 3:  # B-JKX, I-JUX
                            # 있는지 검토 -> 있으면 그냥 맞는 거로 상정하고 진행
                            error_line[-1] = 'error5'
                            # line not ends
                        else: pass  # 어떤 경우?
                elif bio_tag == "I" and next_bio_tag == "B":
                    if len(chk_tag) == 2:
                        form_conts_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # I-NX, B-NX
                            form_funcs_line.append("-")
                            line_ends()
                        elif len(next_chk_tag) == 2:  # I-NX, B-PX
                            form_funcs_line.append("-")
                            line_ends()
                        elif len(next_chk_tag) == 3:  # I-NX, B-JKX
                            pass
                            # line not ends
                        else: pass  # 어떤 경우?
                    elif len(chk_tag) == 3:
                        form_funcs_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # I-JKX, B-JKX
                            # line not ends, 여기서는 일단 맞다 치고 다 기능어로
                            error_line[-1] = 'error6'
                        elif len(next_chk_tag) == 2:  # I-JKX, B-NX
                            line_ends()
                        elif len(next_chk_tag) == 3:  # I-JKX, B-JUX
                            pass
                            # line not ends, B-JUX 다음에 다른 내용어가 와야 line ends
                        else: pass  # 어떤 경우?
                elif bio_tag == "I" and next_bio_tag == "I":
                    if len(chk_tag) == 2:
                        form_conts_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # I-NX, I-NX
                            pass  # line not ends
                        elif len(next_chk_tag) == 2:  # I-NX, I-PX
                            # 어떤 경우인지 확인하는 코드 삽입. 그에 따라 기능어 처리
                            form_funcs_line.append("-")
                            error_line[-1] = 'error7'
                            # 그냥 일단은 line ends로 보기
                            line_ends()
                        elif len(next_chk_tag) == 3:  # I-NX, I-JKX
                            # ? 있는지부터 확인
                            # 여기서는 맞다고 상정하고 I-JKX부터 기능어로 처리
                            error_line[-1] = 'error8'
                        else: pass  # 어떤 경우?
                    elif len(chk_tag) == 3:
                        form_funcs_line.append(morpheme)
                        if next_chk_tag == chk_tag:  # I-JKX, I-JKX
                            pass # line not ends
                        elif len(next_chk_tag) == 2:  # I-JKX, I-NX
                            error_line[-1] = 'error9'
                            line_ends()
                        elif len(next_chk_tag) == 3:  # I-JKX, I-JUX
                            # line not ends, 여기서는 일단 맞다 치고 다 기능어로
                            error_line[-1] = 'error0'
                        else: pass  # 어떤 경우?
            except IndexError:
                # 마지막 형태소에 대한 처리
                if len(chk_tag) == 2:  # B-NX or I-NX
                    form_conts_line.append(morpheme)
                    form_funcs_line.append("-")
                    line_ends()
                elif len(chk_tag) == 3:  # B-JKX or I-JKX
                    form_funcs_line.append(morpheme)
                    try:
                        if error_line[-2] == 'error':
                            error_line[-1] = 'error'
                    except IndexError:  # 2음절 이내 문장
                        if len(chk_tag) == 3:
                            error_line[-1] = 'error'
                    line_ends()
        sent_ends()


def check_chunk_tag(chk_tag, chunktag_line):
    """
    If there's already a same chunk tag, do not append a chunk tag in the list.
    In the case of SYX pair is in a line (ex.'겨울'), check only the last chunk in the list.
    :param chk_tag: a chunk tag to append
    :param chunktag_line: chunk tag list
    :return chunktag_line: chunk tag list after appending or not
    """
    if chk_tag in chunktag_line:
        pass
    else:
        return chunktag_line.append(chk_tag)


def line_ends():
    global form_conts_line, form_funcs_line, lemma_line, xpostag_line, chunktag_line, bi_chunktag_line, error_line

    # allocate line information to sent variables.
    form_conts_sent.append(form_conts_line)
    form_funcs_sent.append(form_funcs_line)
    lemma_sent.append(lemma_line)
    xpostag_sent.append(xpostag_line)
    chunktag_sent.append(chunktag_line)
    bi_chunktag_sent.append(bi_chunktag_line)
    error_sent.append(error_line)

    # initialize
    form_conts_line = []
    form_funcs_line = []
    lemma_line = []
    xpostag_line = []
    chunktag_line = []
    bi_chunktag_line = []
    error_line = []


def sent_ends():
    # global form_conts, form_funcs, lemma, xpostag, chunktag, error
    global form_conts_sent, form_funcs_sent, lemma_sent, xpostag_sent, chunktag_sent, bi_chunktag_sent, error_sent

    # allocate sent information to doc variables.
    form_conts.append(form_conts_sent)
    form_funcs.append(form_funcs_sent)
    lemma.append(lemma_sent)
    xpostag.append(xpostag_sent)
    chunktag.append(chunktag_sent)
    bi_chunktag.append(bi_chunktag_sent)
    error.append(error_sent)

    # initialize
    form_conts_sent = []
    form_funcs_sent = []
    lemma_sent = []
    xpostag_sent = []
    chunktag_sent = []
    bi_chunktag_sent = []
    error_sent = []


########################################################################################################################
def save_supplements():
    global form_conts, form_funcs, lemma, xpostag, chunktag, error, bi_chunktag
    dump_pickle.dump_constituent_unit(form_conts, form_funcs, lemma, xpostag, chunktag, error, bi_chunktag)


if __name__ == "__main__":
    dep_corp, chk_corp, mor_corp = read_file()

    extract_table(dep_corp)
    constituent_unit(chk_corp, mor_corp)




