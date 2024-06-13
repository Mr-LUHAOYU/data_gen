import os

base = r"F:\算法\施工中"
while True:
    choose = input(f"base={base}\tY/n:\t").strip()
    if choose == "Y":
        break
    elif choose == "n":
        base = input(f"input new base:\t\t")
    else:
        break
name = input(f"name:\t").strip()


def create_template_structure():
    folder = os.path.join(base, f'{name}')

    os.makedirs(folder, exist_ok=True)
    os.makedirs(os.path.join(folder, 'Input'), exist_ok=True)
    os.makedirs(os.path.join(folder, 'Output'), exist_ok=True)
    with open(os.path.join(folder, f'{name}（题解）.md'), 'w') as file:
        pass
    with open(os.path.join(folder, f'{name}（题面）.md'), 'w') as file:
        file.write(f"""# {name}

时间限制：$1s$

空间限制：$256MB$

## 题目描述



## 数据格式
·
### 输入



### 输出



## 样例

### 输入

```cpp

```

### 输出

```cpp

```

## 样例解释



## 数据范围及约定


""")

    with open(os.path.join(folder, 'std.cpp'), 'w') as file:
        file.write("""#include <bits/stdc++.h>
using namespace std;

void solve()
{
\t
\t
}

int main()
{
\tint T = 1; cin >> T;
\twhile (T--) solve();	
\treturn 0;
}
""")

    with open(os.path.join(folder, 'std.py'), 'w') as file:
        file.write("""
def solve() -> None:
    return None


# T = 1
T = int(input())
for i in range(T):
    solve()
""")

    with open(os.path.join(folder, 'create.py'), 'w') as file:
        file.write("""from random import randint
from tqdm import trange


def create() -> str:
    out = ""
    return out


for i in trange(1, 11):
    with open(f"Input/{i}.in", 'w') as os:
        os.write(create())
""")


create_template_structure()
