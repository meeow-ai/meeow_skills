# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 用途

这是一个个人 Claude Skills 库，用于沉淀各类工作中的 Claude 使用经验、工作偏好和最佳实践。

## skills/ 目录结构

`skills/` 目录下每个文件对应一个独立的技能或最佳实践主题。文件命名采用 `<主题>.md` 格式。

当前索引：

<!-- 新增 skill 文件后，在此处添加一行：- [文件名](skills/文件名) — 一句话说明 -->

- [meta-skill.md](skills/meta-skill.md) — 如何判断、创建和维护 skill 文件的元规范
- [multi-agent-design.md](skills/multi-agent-design.md) — multi-agent 架构设计：4 个失败模式与 Orchestrator 分工原则

## 加载规则

启动时只读本文件（CLAUDE.md）作为索引。需要某个 skill 的具体内容时，再按需读取对应文件，不要一次性将 skills/ 目录下所有文件全部读入。
