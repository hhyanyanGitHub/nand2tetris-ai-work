from src.assembler import assemble_text

ADD_PROG = """// Adds 1 + 1
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
    # first A-instruction should allocate i at address 16
    assert out[0] == '0000000000010000'
    # third A-instruction references sum, allocated after i -> address 17
    assert out[2] == '0000000000010001'
