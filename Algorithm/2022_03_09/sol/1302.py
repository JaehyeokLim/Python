n = int(input())
table = {}

for _ in range(n):
    book = input()
    if book not in table:
        table[book] = 1
    else:
        table[book] +=1

maximum = max(table.values())
bestseller=[]

for book, number in table.items():
    if number == maximum:
        bestseller.append(book)
print(sorted(bestseller)[0])