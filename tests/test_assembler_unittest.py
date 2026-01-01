"""使用 Python 内置 unittest 运行的测试（避免依赖 pytest）"""
import unittest
from src.assembler import assemble_text

class TestAssembler(unittest.TestCase):
    def test_add_program(self):
        src = """// 计算 1 + 1
@2
D=A
@3
D=D+A
@0
M=D
"""
        expected = [
            '0000000000000010',
            '1110110000010000',
            '0000000000000011',
            '1110000010010000',
            '0000000000000000',
            '1110001100001000',
        ]
        out = assemble_text(src)
        self.assertEqual(out, expected)

    def test_variable_allocation(self):
        src = """@i
M=1
@sum
M=0
@i
M=M+1
"""
        out = assemble_text(src)
        # 第一个 A 指令应将 i 分配到地址 16
        self.assertEqual(out[0], '0000000000010000')
        # 第三个 A 指令引用 sum，应分配到 i 之后的地址 17
        self.assertEqual(out[2], '0000000000010001')

if __name__ == '__main__':
    unittest.main()
