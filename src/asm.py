"""CLI wrapper for the Assembler"""
from __future__ import annotations
import sys
from pathlib import Path
from assembler import assemble_file


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print('Usage: python -m src.asm input.asm [output.hack]')
        return 2
    inp = Path(argv[1])
    out = Path(argv[2]) if len(argv) > 2 else inp.with_suffix('.hack')
    assemble_file(str(inp), str(out))
    print(f'Wrote {out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
