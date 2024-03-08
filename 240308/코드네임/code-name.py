class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

# 5명의 요원 객체 생성
agents = []
for _ in range(5):
    code_name, score = input().split()
    score = int(score)
    agents.append(Agent(code_name, score))

# 점수가 제일 낮은 요원 찾기
lowest_score_agent = min(agents, key=lambda x: x.score)

# 결과 출력
print(lowest_score_agent.code_name, lowest_score_agent.score)