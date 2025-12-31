# 课程要点 — Hack Assembler

本实现覆盖以下内容：

- Hack 指令格式：A 指令 `@value`（16 位），C 指令 `dest=comp;jump`。
- 两遍扫描算法：第一遍构建符号表（labels），第二遍生成机器码并分配变量地址（从 16 开始）。
- 符号表包含预定义符号（R0-R15, SP, LCL, ARG, THIS, THAT, SCREEN, KBD）。

实现说明与关键代码注释都在 `src/assembler.py` 中。

教学建议：在阅读代码时，请注意 `COMP_TABLE`、`DEST_TABLE` 和 `JUMP_TABLE` 的定义，这些是将汇编助记符映射为二进制位的关键。
