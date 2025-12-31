"""Simple Hack Assembler (Python)

Provides assemble_text and assemble_file utilities.
"""
from __future__ import annotations
import re
from typing import List, Dict

# Predefined symbols
PREDEFINED = {
    **{f'R{i}': i for i in range(16)},
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'SCREEN': 16384,
    'KBD': 24576,
}

COMP_TABLE = {
    # a=0
    '0': '0101010','1': '0111111','-1':'0111010','D':'0001100','A':'0110000',
    '!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111','A+1':'0110111',
    'D-1':'0001110','A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101',
    # a=1 (M instead of A)
    'M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101',
}

DEST_TABLE = {
    '': '000', 'M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'
}

JUMP_TABLE = {
    '': '000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'
}

A_INSTR = re.compile(r"^@(.+)$")
LABEL = re.compile(r"^\(([^)]+)\)$")

def clean_line(line: str) -> str:
    line = line.split('//')[0]
    return line.strip()


class Assembler:
    def __init__(self):
        self.symbols: Dict[str,int] = PREDEFINED.copy()
        self.next_variable = 16

    def first_pass(self, lines: List[str]) -> None:
        rom_addr = 0
        for raw in lines:
            line = clean_line(raw)
            if not line:
                continue
            m = LABEL.match(line)
            if m:
                label = m.group(1)
                if label not in self.symbols:
                    self.symbols[label] = rom_addr
            else:
                # A or C instruction
                rom_addr += 1

    def _parse_A(self, symbol: str) -> int:
        if symbol.isdigit():
            return int(symbol)
        if symbol in self.symbols:
            return self.symbols[symbol]
        # new variable
        addr = self.next_variable
        self.symbols[symbol] = addr
        self.next_variable += 1
        return addr

    def _translate_C(self, line: str) -> str:
        dest = ''
        comp = line
        jump = ''
        if '=' in line:
            parts = line.split('=')
            dest = parts[0].strip()
            comp = parts[1].strip()
        if ';' in comp:
            parts = comp.split(';')
            comp = parts[0].strip()
            jump = parts[1].strip()
        comp_bits = COMP_TABLE.get(comp)
        if comp_bits is None:
            raise ValueError(f'Unknown comp: {comp}')
        dest_bits = DEST_TABLE.get(dest)
        if dest_bits is None:
            raise ValueError(f'Unknown dest: {dest}')
        jump_bits = JUMP_TABLE.get(jump)
        if jump_bits is None:
            raise ValueError(f'Unknown jump: {jump}')
        return '111' + comp_bits + dest_bits + jump_bits

    def assemble_text(self, src: str) -> List[str]:
        lines = src.splitlines()
        self.first_pass(lines)
        out: List[str] = []
        for raw in lines:
            line = clean_line(raw)
            if not line:
                continue
            if LABEL.match(line):
                continue
            m = A_INSTR.match(line)
            if m:
                symbol = m.group(1)
                addr = self._parse_A(symbol)
                out.append(f'{addr:016b}')
            else:
                out.append(self._translate_C(line))
        return out

    def assemble_file(self, in_path: str, out_path: str) -> None:
        with open(in_path, 'r', encoding='utf-8') as f:
            src = f.read()
        out = self.assemble_text(src)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(out) + '\n')


def assemble_text(src: str) -> List[str]:
    return Assembler().assemble_text(src)


def assemble_file(in_path: str, out_path: str) -> None:
    return Assembler().assemble_file(in_path, out_path)
