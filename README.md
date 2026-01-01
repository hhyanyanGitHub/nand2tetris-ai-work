# nand2tetris 汇编器（Project 2）

本目录包含一个用 Python 实现的 Hack 汇编器（Project 2）、单元测试与教学笔记。

## 快速开始

要求：
- Python 3.11+
- 使用 `pytest` 运行测试

安装测试依赖：

```bash
python3 -m pip install -r requirements.txt
```

运行测试：

```bash
cd projects/assembler
pytest -q
```

汇编一个文件（两种方式，推荐在项目根目录使用模块方式）：

```bash
# 推荐：模块方式（在项目根目录运行）
python -m src.asm path/to/input.asm [path/to/output.hack]

# 脚本方式（在 src/ 目录或将 src 加入 PYTHONPATH 时也可直接运行）：
python src/asm.py path/to/input.asm [path/to/output.hack]
```

注意：如果使用模块方式（`-m`），请在包含 `src/` 目录的项目根目录下运行，这样 Python 能找到包；脚本方式则在某些环境下更宽容，但模块方式更符合包化实践。
---

## 教学笔记
请参阅 `NOTES.md` 和 `GIT.md`，其中包含课程要点与简短的 Git 教学。
