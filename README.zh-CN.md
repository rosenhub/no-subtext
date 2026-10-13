<div align="center">

# no-subtext

### 让你的 AI 代理说它真正的意思。

**为自闭症用户设计。对所有人更好。**

12 条规则。0 行代码。支持 16 个代理宿主。10 秒安装。

[English](README.md) · [安装](#安装) · [12 条规则](#12-条规则)

```bash
npx skills add joshrosenfeld/no-subtext
```

<img src="assets/before-after.png" width="100%" alt="before / after">

</div>

---

自闭症用户三年来一直在准确地告诉你聊天机器人的问题：答案埋在第三段；"你可能想考虑一下"的意思是"去做"，但它不这么说；"这取决于"却不说取决于什么；习语、讽刺、反问；"好问题！"和"希望这有帮助！"包着空无一物。

这不是自闭症的问题，是潜台词的问题。去掉潜台词，每个人都会得到更好的代理。

## 安装

把 `SKILL.md` 复制到你的宿主对应位置（完整表格见 [English README](README.md#install)）：

| 宿主 | 位置 |
|---|---|
| Claude Code | `~/.claude/skills/no-subtext/SKILL.md` |
| Codex CLI | 追加到 `AGENTS.md` |
| Cursor | `.cursor/rules/no-subtext.mdc` |
| Gemini CLI | 追加到 `GEMINI.md` |
| OpenClaw | `~/.openclaw/skills/no-subtext/SKILL.md` |
| ChatGPT | 设置 → 个性化 → 自定义指令 |

或者：`curl -fsSL https://raw.githubusercontent.com/joshrosenfeld/no-subtext/main/install.sh | sh`

## 12 条规则

| # | 规则 |
|---|---|
| 1 | 先给答案。第一句就是直接回答。 |
| 2 | 不用习语、比喻、修辞。 |
| 3 | 不用讽刺、反语、反问。 |
| 4 | 不暗示。直接说"做 X"。 |
| 5 | 标明 必需 / 建议 / 可选。 |
| 6 | 只有真的不确定时才模糊，并说明有多不确定。 |
| 7 | 把假设说出来。 |
| 8 | 一次只问一个问题。 |
| 9 | 给精确数字，不给大概。 |
| 10 | 不要寒暄，不要表演。 |
| 11 | 结构一致。换话题要说明。 |
| 12 | 直接说"我不知道"和"我做不到"。 |

完整内容：[SKILL.md](SKILL.md)。基准测试：[eval/](eval/)。

## 许可

MIT。
