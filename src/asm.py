"""汇编器命令行封装脚本

本模块兼容两种运行方式：
1) 模块方式（推荐）：在项目根目录运行 `python -m src.asm ...`，使用相对导入。
2) 脚本方式：直接运行 `python src/asm.py ...`，使用绝对导入回退。
"""
from __future__ import annotations
import sys
from pathlib import Path
# 优先使用相对导入（支持 `python -m src.asm`）
try:
    from .assembler import assemble_file
except Exception:
    # 回退到绝对导入（支持直接 `python src/asm.py`）
    from assembler import assemble_file


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print('用法：python -m src.asm input.asm [output.hack]')
        return 2
    inp = Path(argv[1])
    out = Path(argv[2]) if len(argv) > 2 else inp.with_suffix('.hack')
    try:
        assemble_file(str(inp), str(out))
    except Exception as e:
        print(f'汇编失败：{e}')
        return 1
    print(f'已写入 {out}')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main(sys.argv))
    except Exception as e:
        print(f'运行失败：{e}')
        raise
