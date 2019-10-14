"""
[toChunkForm]
ver.2.0.0
dependency corpus를 chunk tagger를 이용해 chunk label을 부착하기 위해
chunk form으로 변환하는 프로그램
(일단은 NAX label 부착)

이 프로그램의 결과물을 파일로 만든 뒤 chunk tagger에 돌려서 결과 확인
"""
import pandas as pd
import sys

DEP_PATH = r"E:\Users\NLP86\Documents\세종말뭉치\Dependency corpus\sejong-non_head_final.conll"
SAVE_PATH = r".\corpus\dep2chunk.conllc"


def read_data():
    with open(DEP_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()


def pre_processing():
    data = read_data()

    text = ''
    num = 0  # chunk-based dependency corpus의 형태소 id

    # sfile = open("save_file_NAX.conllc", 'a', encoding='utf-8')  # 0710 주석처리
    sfile = open(SAVE_PATH, 'a', encoding='utf-8')
    for line in data:
        # information part
        line = line.strip()
        text = text.strip()
        if line:
            if line[0] == "#":
                info_title, *info_content = line.split(":")
                info_content = ''.join(info_content).strip()
                if info_title == "#SENTID":
                    sent_num = info_content
                    print("# sent_num = ", sent_num)
                    sfile.write("\n\n# sent_num =" + sent_num)
                elif info_title == "#FILE":
                    sent_id = info_content
                    print("# sent_id = ", sent_id)
                    sfile.write("\n# sent_id =" + sent_id)
                elif info_title == "#ORGSENT":
                    text = info_content
                    print("# text = ", text)
                    sfile.write("\n# text =" + text)
                else:
                    print("Error in sentence information part.", file=sys.stderr)
                num = 0

            # sentence part
            elif text:
                num_id, form, lemma, upos, xpos, feats, head, deprel, deps, misc = line.split('\t')
                for word, pos in zip(lemma.split(), xpos.split('+')):
                    num += 1
                    space = 0
                    chunk = 'NAX'
                    if word == lemma.split()[-1]:  # 띄어쓰기 정보
                        space = 1
                    print("{}\t{}\t{}\t{}\t{}".format(num, word, pos, space, chunk))
                    sfile.write("\n{}\t{}\t{}\t{}\t{}".format(num, word, pos, space, chunk))
    sfile.close()


if __name__ == "__main__":
    pre_processing()






