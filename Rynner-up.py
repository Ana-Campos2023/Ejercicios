n = int(input())
arr = map(int, input().split())
numerosValidos=list(arr)[:n]
scores=set(numerosValidos)
mayor=max(scores)
scores.remove(mayor)
print(max(scores))