# 문제
# 상근이는 N개국을 여행
# 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
# 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
# 상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.

# 입력
# 테스트 케이스의 수 T
# 국가의 수 N , 비행기의 종류 M  
# 이후 M개의 줄에 a와 b 쌍들이 입력된다. 
# a와 b를 왕복하는 비행기가 있다는 것을 의미한다. 
# 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

# 출력
# 테스트 케이스마다 한 줄을 출력한다.
# 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.

# 로직
# 최소 신장 트리에서는 항상 간선(비행기)의 수는 국가의 수 N에서 1을 뺀 N−1이 됩니다.

# 입력 처리
T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    N, M = map(int, input().split())  # 국가의 수 N, 비행기의 종류 M
    for _ in range(M):
        a, b = map(int, input().split())  # 비행기 정보 입력
    # 최소한의 비행기 종류는 국가의 수 - 1
    print(N - 1)
