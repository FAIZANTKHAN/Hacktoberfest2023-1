from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Create a graph and calculate in-degrees for each character
    graph = defaultdict(list)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(1, len(words)):
        w1, w2 = words[i - 1], words[i]
        min_len = min(len(w1), len(w2))

        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                in_degree[w2[j]] += 1
                break

    # Step 2: Perform topological sorting using Kahn's algorithm
    result = []
    queue = deque([char for char in in_degree if in_degree[char] == 0])

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Check for cycles
    if len(result) != len(in_degree):
        return ""

    return ''.join(result)

# Example usage
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))  # Output: "wertf"
