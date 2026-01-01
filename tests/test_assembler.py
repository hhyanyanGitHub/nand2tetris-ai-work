from src.assembler import assemble_text

ADD_PROG = """// 计算 1 + 1
@2
D=A
@3
D=D+A
@0
M=D
"""

EXPECTED_ADD = [
    '0000000000000010',
    '1110110000010000',
    '0000000000000011',
    '1110000010010000',
    '0000000000000000',
    '1110001100001000',
]


def test_add_program():
    out = assemble_text(ADD_PROG)
    assert out == EXPECTED_ADD


def test_variable_allocation():
    src = """@i
M=1
@sum
M=0
@i
M=M+1
"""
    out = assemble_text(src)
    # 第一个 A 指令应将 i 分配到地址 16
    assert out[0] == '0000000000010000'
    # 第三个 A 指令引用 sum，应分配到 i 之后的地址 17
    assert out[2] == '0000000000010001' 
