---
name: multi-agent-design
trigger: 设计 AI workflow、讨论 agent 架构、或判断是否需要拆分单一 agent 时
last_updated: 2026-06-26
---

## 核心心智模型

从「聊天」转向「委派」：chatbot 是被锁在桌前的全能实习生，multi-agent 是可以分工行动的团队。

> Generalists burn out, specialists scale.

## 4 个常见失败模式与解法

### 1. Context Saturation（上下文饱和）
**症状**：单个 agent 承担所有任务，跑着跑着开始「失忆」或走偏。  
**解法**：Orchestrator 模式——一个 orchestrator 负责拆解任务和协调，多个 specialist subagent 各自只做一件事。

### 2. 环境依赖地狱
**症状**：代码在 AI 环境里跑不起来，setup 失败。  
**解法**：专门部署一个 Sysadmin Subagent，只处理环境配置，不写任何业务逻辑。

### 3. God Prompt（巨型提示词）
**症状**：花大量时间打磨的复杂 prompt 只能靠复制粘贴传递，难以复用和维护。  
**解法**：把 prompt 保存为文件（Agent Skill），让 orchestrator 按需调用，交互从「粘贴长文」变成「高层指令」。

### 4. Glue Problem（应用孤岛）
**症状**：手动在 Notion、Gmail、Slack 等工具之间搬运数据。  
**解法**：为每个 API 部署一个轻量 subagent，单一职责，组合调用。

## 起步原则

**不要一上来就建十人团队，先建两人团队：**
- 开发者：Architect agent（出方案）+ Editor agent（写代码）
- 内容创作者：Draft agent（写脚本）+ Storyboard agent（转视觉）

验证分工模式有效后再扩展。
