여기 있는 test_error_xc.sent가 BI 오류까지 수정하고 출력한 최종 dep_corp 임.
이걸 가지고 어절이 나누어진 경우 찾음
아래 프로젝트에서 진행.
E:\Chunking\DependencyCorpus\toChunk_based_DepCorpus_02

그 결과가 divided_dojeol.sent 임
나눠지는 문장의 수: (10,806 문장)

이를 이용해서 아래 코퍼스 정제를 함
E:\Chunking\DependencyCorpus\toChunk-based_DepCorpus_ver.3.0.0\result_0820_2\chunk_dep_corpus.conllc (62,343 문장)
아래 프로젝트에서 진행.
E:\CorpusRefining

그 결과가 chunk_dep_corpus(refine).conllc 이며 (51,537 문장)
여기서 root가 포함 안 되어 있는 코퍼스도 제거 후 최종 완성된 코퍼스가 다음과 같음

chunk_dep_corpus(refine_root).conllc (49,301 문장)

여기서 CoNLL 형식으로 변환한 corpus 작성
마지막 줄만 추가해주면 될 듯
그리고 빈칸 없게 할 것

pointer net을 먼저 공부하는게 좋을지도
그래도 일단 코퍼스는 만들어 놓기 (O)