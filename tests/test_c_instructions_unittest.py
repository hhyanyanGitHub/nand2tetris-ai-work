"""C 指令单元测试：覆盖 dest、comp、jump、空白与错误情况"""
import unittest
from src.assembler import assemble_text

class TestCInstructions(unittest.TestCase):
    def test_dest_only(self):
        src = """D=M
"""
        out = assemble_text(src)
        # D=M -> comp=M (1110000), dest=D (010), jump=000
        self.assertEqual(out[0], '1111110000010000')

    def test_comp_and_jump(self):
        src = """D;JGT
"""
        out = assemble_text(src)
        # D;JGT -> comp=D (0001100), dest=000, jump=001
        self.assertEqual(out[0], '1110001100000001')

    def test_full_dest_comp_jump(self):
        src = """AMD=D+1;JLE
"""
        out = assemble_text(src)
        # comp D+1 (0011111), dest AMD (111), jump JLE (110)
        self.assertEqual(out[0], '1110011111111110')

    def test_comp_with_M(self):
        src = """D=D+M
"""
        out = assemble_text(src)
        # D+M -> comp bits for D+M (1000010)
        self.assertEqual(out[0], '1111000010010000')

    def test_whitespace_and_comments(self):
        src = """  // 顶部注释
  D = A  // 行内注释
"""
        out = assemble_text(src)
        # D=A -> comp A (0110000), dest D (010)
        self.assertEqual(out[0], '1110110000010000')

    def test_unknown_comp_raises(self):
        src = """D=FOO
"""
        with self.assertRaises(ValueError) as cm:
            assemble_text(src)
        self.assertIn('未知的 comp', str(cm.exception))

if __name__ == '__main__':
    unittest.main()
