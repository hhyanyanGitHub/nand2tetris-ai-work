# Git 快速教学（与项目协作相关）

建议的工作流：

1. 初始化仓库（若尚未）

```bash
git init
git add .
git commit -m "chore: add assembler project"
```

2. 创建功能分支

```bash
git checkout -b feat/assembler
```

3. 小步提交，写清楚 commit message

```bash
git add src/ tests/ README.md
git commit -m "feat: add assembler and unit tests"
```

4. 在远程仓库上创建分支并推送

```bash
git remote add origin <url>
git push -u origin feat/assembler
```

5. 复习差异并发起 Pull Request

```bash
git diff main...feat/assembler
```

6. 建议用 `git rebase -i` 保持提交记录整洁（可选）

---

小贴士：每次完成一个小目标（例如实现 A 指令，或添加一组测试）就提交并推送，这样便于回滚和代码审查。
