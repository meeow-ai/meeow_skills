# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 用途

这是一个可复用的 Claude skills 与 agent 模板库，沉淀跨项目的工作经验、偏好和最佳实践。纯 Markdown 仓库——没有构建、测试或 lint 流程，唯一的验证手段是人工 review diff。

## 三棵内容树

| 目录 | 内容 | 约定 |
|------|------|------|
| `skills/` | 关于「如何与 Claude 协作」的元经验 | `skills/<名称>/SKILL.md` |
| `design/` | 创意与品牌工作流（访谈脚本、风格发现） | 双语时按 `design/<名称>/<cn\|en>/SKILL.md` 分目录，单语时 `design/<名称>/SKILL.md` |
| `SOUL/` | Agent 人格模板（思考方式、优先级、沟通风格） | `SOUL/<语言>_template/SOUL.md` |

`design/` 下的 skill 是**给用户跑的交互式流程**（分阶段提问、产出文档），`skills/` 下的是**给 Claude 读的规则**。写新文件前先确认属于哪一类。

## Skill 契约

每个 `SKILL.md` 以 YAML frontmatter 开头，三个字段缺一不可：

```yaml
---
name: <与所在目录名一致>
trigger: <一句话：什么情况下应该读这个文件>
last_updated: <YYYY-MM-DD>
---
```

`trigger` 是被检索的关键——写「设计 AI workflow、讨论 agent 架构时」，不写「关于 agent 的说明」。修改正文时同步更新 `last_updated`。

判断标准（什么值得沉淀、什么不值得）见 [meta-skill](skills/meta-skill/SKILL.md)，新增或整理 skill 前先读它。

## 索引即接口

下方索引不只是给人看的目录，`.claude/commands/` 下的两个 command 把它当作权威来源：

- `/update-skill` — 任务结束后判断本次对话是否有值得沉淀的经验，读索引查重，再决定新建还是更新现有 skill。
- `/audit-skills` — 取「索引条目」与「扫描 `skills/` 目录」的并集，标记 `last_updated` 超过 30 天的文件并检查内容重叠。

新增 skill 时必须同时在索引里加一行，否则 `/update-skill` 会重复创建。另注意 `/audit-skills` 只扫描 `skills/` 目录，`design/` 与 `SOUL/` 仅靠索引条目才可见。

## 索引

**skills/** — 与 Claude 协作的元经验

<!-- 新增后在此加一行：- [名称](skills/名称/SKILL.md) — 一句话说明 -->

- [meta-skill](skills/meta-skill/SKILL.md) — 如何判断、创建和维护 skill 文件的元规范
- [multi-agent-design](skills/multi-agent-design/SKILL.md) — multi-agent 架构设计：4 个失败模式与 Orchestrator 分工原则

**design/** — 创意与品牌工作流

- [client_discovery](design/client_discovery/SKILL.md) — 完整的 agency 客户访谈，产出 Client DNA 文档；任何设计项目开始前先跑
- [style_profiling](design/style_profiling/) — 视觉风格发现，适用于项目方向已定的场景（[cn](design/style_profiling/cn/SKILL.md) / [en](design/style_profiling/en/SKILL.md)）
- [style_self_profiling](design/style_self_profiling/) — 自我风格发现，内向者友好、无访谈者的自主探索（[cn](design/style_self_profiling/cn/SKILL.md) / [en](design/style_self_profiling/en/SKILL.md)）

**SOUL/** — Agent 人格模板

- [zh_CN_template](SOUL/zh_CN_template/SOUL.md) — 中文人格模板

## 加载规则

启动时只读本文件作为索引。需要某个 skill 的具体内容时再按需读取，不要一次性把所有 `SKILL.md` 读入上下文。

## 提交约定

Commit message：`skill(<名称>): <一句话描述变更>`
分支：`skill/<简短描述>`

`/update-skill` 会自动按此格式建分支和提交，并输出 `git diff main` 等待确认后再 merge。
