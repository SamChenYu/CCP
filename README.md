# This is a satirical project that mimics Python using Chinese syntax. It is not political and is intended purely for educational and comedic purposes

### Basic compiler that allows full Chinese python source code. All keywords available are inside translate.txt

Example .ccp source code
```python
# 主程序.ccp
类 人:
    定义 __初始化__(自己, 名字):
        自己.名字= 名字
    定义 __细绳__(自己):
        返回 自己.名字


如果 __标识__ == "__主程序__":
    朋友 = 人("小明")
    打印("你好世界,  " + 朋友.__细绳__() + "!")
```
Running the compiler
``` bash
python compiler.py <filename>.ccp
```
Output
``` bash
你好世界,  小明!
```