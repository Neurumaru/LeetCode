# 시간 복잡도 : O(n)
# 공간 복잡도 : O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 파싱된 문자열 해쉬값을 키로, 원래 문자열을 값으로 가지는 딕셔너리
        # Dict[Tuple[Tuple[str, int], ...], List[str]]의 구조를 가짐 
        parsed_to_raw_dict = dict()

        # a 부터 z 까지를 키로 가지며 값으로 0을 가지는 딕셔너리 생성
        # O(1)
        chr_count_dict = {chr(i):0 for i in range(97, 123)}

        # 문자열을 파싱해서 딕셔너리에 넣어줌
        # O(n * m) = O(n)
        for s in strs:
            # 딕셔너리 재활용을 위한 초기화
            # O(1)
            for key in chr_count_dict:
                chr_count_dict[key] = 0

            # 각각의 문자에 대해서 파싱
            # O(m)
            for c in s:
                chr_count_dict[c] += 1
            
            # parsed_to_raw_dict에 파싱된 문자열 해쉬값을 키로 해서 문자열 삽입
            # O(1)
            key = tuple(chr_count_dict.values())
            parsed_to_raw_dict.setdefault(key, list())
            parsed_to_raw_dict[key].append(s)

        # Dict[int, List[str]] 형태를 List[List[str]] 형태로 변환
        # O(n)
        return parsed_to_raw_dict.values()