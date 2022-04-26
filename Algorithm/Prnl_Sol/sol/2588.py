n = int(input())
m = int(input())

m_list = list(map(int, str(m)))
m_list.reverse()
r_list = []

for i in range(len(m_list)):
    r_list.append(n * m_list[i])

for i in range(len(r_list)):
    print(r_list[i])
print(n * m)