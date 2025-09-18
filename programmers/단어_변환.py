# 단어_변환


def have_path(word_1, word_2):
    diff = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            diff += 1
        if diff > 1:
            return False
    if diff == 1:
        return True

    return False


def bfs(target_idx):
    vis = [False for _ in range(len(graph))]
    queue = [0]
    vis[0] = True
    cnt  = 0
    while queue:
        cnt += 1
        new_queue = []
        for cur in queue:
            for nxt in graph[cur]:
                if vis[nxt]:
                    continue
                if nxt == target_idx:
                    return cnt
                new_queue.append(nxt)
                vis[nxt] = True
        queue = new_queue
    return 0


def solution(begin, target, words):
    global graph
    if target not in words:
        return 0

    graph = [[] for _ in range(len(words) + 1)]
    words = [begin] + words
    target_idx = 0
    for i, word_1 in enumerate(words):
        if word_1 == target:
            target_idx = i
        for j, word_2 in enumerate(words):
            if have_path(word_1, word_2):
                graph[i].append(j)

    return bfs(target_idx)
