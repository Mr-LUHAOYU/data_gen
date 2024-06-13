def surface(name: str) -> str:
    return f"""# {name}

    时间限制：$1s$

    空间限制：$256MB$

    ## 题目描述



    ## 数据格式

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


    """


def stdcpp() -> str:
    return """#include <bits/stdc++.h>
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
    """


def stdpy() -> str:
    return """
    def solve() -> None:
        return None


    # T = 1
    T = int(input())
    for i in range(T):
        solve()
    """


def createpy() -> str:
    return """from random import randint
    from tqdm import trange


    def create() -> str:
        out = ""
        return out


    for i in trange(1, 11):
        with open(f"Input/{i}.in", 'w') as os:
            os.write(create())
    """