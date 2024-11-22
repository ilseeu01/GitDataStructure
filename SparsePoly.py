from LinkedList import *

class Term:
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef

class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def read(self):
        while True:
            user_input = input("계수 차수 입력(종료 -1): ")

            # 숫자 추출 로직 (split() 없이 직접 처리)
            coef, expo = 0, 0
            sign = 1  # 부호 처리용
            num = 0   # 현재 읽고 있는 숫자
            is_coef = True  # 첫 번째 숫자는 coef(계수), 두 번째는 expo(차수)
            
            for char in user_input:
                if char == ' ':  # 공백을 만나면 현재 숫자 완료
                    if is_coef:
                        coef = sign * num
                        is_coef = False  # 다음 숫자는 expo
                    else:
                        expo = sign * num
                    sign = 1  # 부호 초기화
                    num = 0
                elif char == '-':  # 음수 처리
                    sign = -1
                elif char in '1234567890':  # 숫자인 경우
                    num = num * 10 + int(char)
            
            # 마지막 숫자 처리 (expo)
            if is_coef:
                coef = sign * num
            else:
                expo = sign * num
            
            # 종료 조건
            if coef == -1 and expo == -1:
                break
            
            # Term 객체 생성
            term = Term(expo, coef)

            # Term을 연결 리스트에 추가
            self.insert_sorted(term)
    
    def insert_sorted(self, term):
        """차수(expo)에 따라 내림차순으로 Term을 삽입"""
        if self.head is None or self.head.data.expo < term.expo:
            # 새 노드가 가장 큰 차수일 때
            self.head = Node(term, self.head)
        else:
            # 적절한 위치를 찾아 삽입
            current = self.head
            while current.link is not None and current.link.data.expo >= term.expo:
                current = current.link
            current.link = Node(term, current.link)


    def display(self):
        if self.head is None:
            print("다항식이 비어 있습니다.")
            return

        result = []
        current = self.head
        while current is not None:
            term = current.data
            if term.coef != 0:
                result.append(f"{term.coef}x^{term.expo}" if term.expo != 0 else f"{term.coef}")
            current = current.link

        print(" + ".join(result))

    def __add__(self, polyB):
        """두 다항식을 더한 새로운 다항식을 반환"""
        result = SparsePoly()
        p1 = self.head
        p2 = polyB.head

        while p1 is not None or p2 is not None:
            if p1 is None:
                # p1이 끝났으면 p2의 항을 그대로 추가
                result.insert_sorted(p2.data)
                p2 = p2.link
            elif p2 is None:
                # p2가 끝났으면 p1의 항을 그대로 추가
                result.insert_sorted(p1.data)
                p1 = p1.link
            elif p1.data.expo > p2.data.expo:
                # p1의 차수가 더 크면 p1의 항을 추가
                result.insert_sorted(p1.data)
                p1 = p1.link
            elif p1.data.expo < p2.data.expo:
                # p2의 차수가 더 크면 p2의 항을 추가
                result.insert_sorted(p2.data)
                p2 = p2.link
            else:
                # 차수가 같으면 계수를 합산
                new_coef = p1.data.coef + p2.data.coef
                if new_coef != 0:  # 계수가 0이면 추가하지 않음
                    result.insert_sorted(Term(p1.data.expo, new_coef))
                p1 = p1.link
                p2 = p2.link

        return result

    def __equal__(self, polyB):
        """두 다항식이 동일한지 확인"""
        p1 = self.head
        p2 = polyB.head

        while p1 is not None and p2 is not None:
            # 계수나 차수가 다르면 False
            if p1.data.coef != p2.data.coef or p1.data.expo != p2.data.expo:
                return False
            p1 = p1.link
            p2 = p2.link

        # 하나의 다항식이 끝나지 않았다면 False
        return p1 is None and p2 is None

    def degree(self):
        """가장 높은 차수를 반환"""
        if self.head is None:
            return None  # 다항식이 비어 있으면 None 반환
        return self.head.data.expo  # 첫 노드의 expo가 가장 큼

    def coef(self):
        """모든 계수를 리스트로 반환"""
        coefficients = []
        current = self.head
        while current is not None:
            coefficients.append(current.data.coef)
            current = current.link
        return coefficients


if __name__ == '__main__':
    sp1 = SparsePoly()

    sp1.read()
    sp1.display()

    sp2 = SparsePoly()
    sp2.read()
    sp2.display()

    sp3 = sp1 + sp2
    print('합계 : ', end= '')
    sp3.display()

    print('계수: ', sp3.coef())
    print('차수: ', sp3.degree())
    print('sp1 == sp2 사실 여부:  ', sp1 == sp2)


