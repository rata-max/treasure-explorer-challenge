# Treasure Explorer Bot Challenge — Week 1 Starter

Week 1 is **Keyed Tree Escape**. The public maps are connected tree mazes.
Students use DFS/BFS parent links to collect a key, choose useful batteries,
and reach the exit before energy runs out.

```bash
python -m treasure_explorer --map maps/week1_tree_easy.json --agent student/agent.py --view
```

See `docs/WEEK1_TREE_MAZE.md` for the complete student specification.

문제해결기법 수업의 1주차(실습 6시간)용 스타터 저장소입니다. 학생은 원칙적으로
`student/agent.py`만 수정합니다.

## 빠른 시작

요구 환경은 **Python 3.11 이상**뿐이며 외부 패키지는 없습니다.

```bash
python -m treasure_explorer --map maps/example_easy.json --agent student/agent.py
python -m unittest discover -s tests -v
```

소스 설치 없이 실행하려면 저장소 루트에서 위 명령을 실행하세요. Windows PowerShell,
macOS/Linux 터미널에서 동일하게 동작합니다.

## 저장소 구성

- `student/agent.py`: 학생 제출 대상
- `treasure_explorer/`: 고정 게임 엔진 및 실행기
- `maps/`: 공개 연습 맵 3개
- `tests/`: 공개 테스트
- `docs/ASSIGNMENT_WEEK1_KO.md`: 과제 명세와 시간 계획
- `docs/GITHUB_RELEASE_GUIDE_KO.md`: TA용 GitHub 배포 절차

## 실행 예

```bash
python -m treasure_explorer --map maps/example_medium.json --agent student/agent.py --seed 7 --verbose
```

마지막 줄의 JSON 결과가 채점에 사용됩니다. `--seed`는 동일 입력의 재현성을 위한
인터페이스이며, 1주차 공개 맵은 결정적입니다.

## 제출

`student/agent.py` 한 파일을 제출합니다. 파일 입출력, 네트워크, 프로세스 실행,
외부 패키지 사용은 금지합니다. 자세한 규칙은 과제 명세를 확인하세요.
