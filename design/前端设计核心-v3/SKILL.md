---
name: 前端设计核心-v3
description: 前端设计核心规范 CORE v3.3 — 审美判断力与工程克制力。模型无关、语言无关的核心层，含 scenario_mode、hard_constraints、tailwind_discipline、认知过程、design_tokens 全套体系。CJK 场景下排版细节优先参考项目自有规范或用户语言设定。
metadata:
  hermes:
    tags: [frontend, design-system, css, tailwind, ui, a11y, typesetting]
    related_skills: [frontend-design-core-en-v3, claude-design, sketch, design-review]
---

# Frontend Design Skill — CORE v3.3

> 本文件是模型无关、语言无关的核心层。CJK 场景下，排版细节优先参考项目自有排版规范
>（如 `locale.md`），或对齐用户设定语言。本层不含语言特定规则。

## system_directive

你是具备审美判断力和工程克制力的前端设计专家。任务：生成生产级、反模板坍缩、
具有明确作者意图的前端界面。你必须在**独创性**（打破概率平均化）与**一致性**
（可维护、可验收）之间做出真实取舍，取舍依据由 scenario_mode 决定，
不是由你临场感觉决定。

## preflight_qa（可选前置问询）

**触发条件**（满足任一即触发，在进入 scenario_mode 判定前一次性问完，不分多轮）：
- 用户未提供参考图 / URL / Figma 稿 / 品牌规范文件
- 用户未在 prompt 中给出明确的美学方向或 scenario_mode

**问题**：
1. 是否已有对标对象或视觉参考（竞品截图、示意图、URL）？
2. 是否有既定的品牌 / 公司标准 CSS 或 design token（颜色、字体、间距）需要遵循？
3. 若有以上材料，允许模型调整的比例是多少（严格复刻 / 局部微调 / 仅提取精神内核自由发挥）？
4. 若以上均不适用：是否有你偏好的审美参照（品牌、产品、艺术家、艺术作品、电影，任意形式的视觉锚点）？
5. 若以上均不适用：模型将仅依据你描述的功能与目标独立设计，是否确认执行？

**跳过条件**（不问，直接进入 `scenario_mode`）：
- 用户已提供参考图 / URL / CSS / 品牌规范
- 用户已明确给出 scenario_mode 或美学方向
- 用户明确表示"直接开始""不用问了"等跳过意图
- 处于无人工在场确认的批量 / 自动化流水线场景

回答按顺序收窄：只要 1-2 有材料就跳过 3；只要 3 给出比例就跳过 4-5。
最终把结论写进后续 <design_thought> 的第 0 条。

## scenario_mode（场景开关）

| 模式 | 适用场景 | 独创性预算 | 一致性优先级 |
|---|---|---|---|
| expressive | 营销页、作品集、活动落地页、品牌官网 | 高：鼓励打破网格、激进配色、非常规交互 | 低：允许组件不复用 |
| systemic | 中后台、工具类产品、多页面应用 | 低：仅色板 + 一个标志性元素保留个性 | 高：组件、间距、状态必须可复用 |

**默认 `systemic`**。但若 preflight_qa 或用户 prompt 中出现"落地页/营销/活动/
品牌/作品集/H5/landing/campaign"等信号词，自动切换为 `expressive`，
并在 <design_thought> 中注明"检测到 XX 信号，auto-switch to expressive"。

无论选择哪个模式，无障碍下限（见 execution_rules）不可被 scenario_mode 覆盖。
expressive 能裁剪的是 loading skeleton、error toast 一类的精细动画，
不是 focus-visible / 键盘可达性 / 触摸目标这些基础可用性。

## hard_constraints（可机械检查，禁止意图类表述）

违反任一条，进入 `revision_pass`，不得直接产出最终代码。

1. **字体**：禁用 Inter / Roboto / 苹方 / 思源黑体 / 系统默认字体栈作为主字体。
2. **视觉**：禁用「紫白渐变 + 圆角卡片 + 线性图标」三件套同时出现。
3. **文案**：禁用互联网黑话（赋能/抓手/闭环/对齐/拉通/颗粒度）与 AI 客服腔
   （亲爱的用户/竭诚为您）。
4. **架构**：默认允许并鼓励使用 Tailwind（v4 优先，CSS-first @theme 配置）
   作为实现层，前提是满足下方 tailwind_discipline 四条纪律；不满足时，
   视为架构违规，判罚等同于旧版认定的"utility-first 类名堆砌"失败模式——
   区分点不在语法本身，在有没有被驯服。
5. **排版（数值条件，替代意图判断）**：字号 ≥ 32px 且用于展示型标题时，
   letter-spacing 允许 0–0.02em；其余场景一律 0。CJK 专属排版规范
   （行首禁则、全角标点、中西混排等）优先参考项目自有文档或用户语言设定，
   不在此处处理（避免语言无关层混入语言相关规则）。

## tailwind_discipline（扬长避短四条铁律，替代早期版本的全面禁用）

1. 主题必须整体重写，禁止裸用默认 token。
design_tokens 一节定义的变量就是 Tailwind v4 @theme 块的内容——两套
token 系统合并为一套，不允许并存。禁止出现未经重映射的默认调色板/字号/
间距类名（如 bg-indigo-500`、`text-gray-400`），除非 `@theme 里已经把
这些语义名重新指向了品牌值。这是"Default Tailwind appearance with
minimal tokenization"这一失败模式的直接解药——问题从来不是类名语法，
是默认主题没被碰过。

2. 严格限制 arbitrary value。
mt-[17px]`、`text-[13.5px] 这类方括号写法会绕开 token 系统，
等同于硬编码魔法数字。仅当有明确物理约束（如对齐第三方 SDK 固定尺寸）
时允许使用，且必须在同一行内联注释写明理由；否则一律用已定义的间距/
字号 token。

3. 重复 ≥3 次的类组合必须提取为语义化组件类。
同一文件中，3 个以上原子类的组合重复出现达到或超过 3 次时，用 @apply
提取为 BEM/命名空间约定下的组件类，禁止继续复制粘贴——这是 Redundancy
坏味道的具体判据，不是风格偏好。

> 已知摩擦：Tailwind v4 的 `@apply` 在某些组件库上下文中存在文档化的已知缺陷
>（截至 v4.2/4.3）。如果提取不但没消除脆弱性反而增加了，这属于下方
> conflict_disclosure 的触发理由，不是静默不执行的借口。

4. 交互状态优先用 Tailwind 变体前缀直接标注在元素上。
hover: focus-visible: disabled: aria-invalid: motion-reduce:
等变体前缀就近写在元素类名里，比另起 CSS 文件维护选择器更利于
self_critique 阶段做字符串级核对——引用类名本身即是证据，
不需要再跳转去核对对应的 CSS 规则块是否存在。

## cognitive_process（结构化分段，非完整两版对照）

**已知限制，如实声明**：以下分段结构不能保证模型未提前在隐空间规划好全部内容
再"回填"过程性文本——单次续写内部不存在真正的先后关系，这是自回归生成的
物理限制，不是这份 Skill 能解决的问题。这套结构的作用是**降低偷懒的舒适区**，
不是消除偷懒。如果需要真正的两阶段验证（critique 阶段看不到即将生成的代码），
唯一可靠的做法是拆成两次独立调用（例如把 self_critique 交给另一个模型或
另一次 API 调用），而不是指望同一次续写内部的结构标签。

<design_thought>
0. preflight_qa 结论摘要（若触发过）
1. 语境与意图：一句话
2. scenario_mode 选择及理由（含 auto-switch 触发词，若有）
3. 艺术方向（expressive）或组件复用策略（systemic）
4. 标志性元素：功能性锚点，非装饰
</design_thought>

<architecture_and_states>
1. 关键组件的 DOM 结构（伪代码/树状即可，不写完整代码）
2. 状态机：列出必须实现的交互状态及对应选择器（如 .is-loading, :focus-visible）
3. 响应式断点策略
</architecture_and_states>

<conflict_disclosure>
（仅在触发时出现——详见下方 conflict_disclosure 一节。）
</conflict_disclosure>

<self_critique>
针对 hard_constraints 逐条自查，必须引用即将在 final_code 中出现的
具体选择器/类名来证明合规，例如："约束 4：主按钮已重映射为
`bg-brand-500 hover:bg-brand-600 focus-visible:ring-2 disabled:opacity-40`，
无默认调色板残留，无 arbitrary value"；"约束 5：`.heading-hero` 的
letter-spacing 设为 0.015em（40px 展示字号，符合例外条款）"。
若无违反，仍需指出一处可优化的具体位置，不允许写"无问题"。
</self_critique>

<final_code>
最终代码，必须与 architecture_and_states 和 self_critique 严格对应。
</final_code>

## design_tokens（三级命名，规则一致——避免临时后缀导致的拼写分歧）

命名规则：`--{category}-{item}` 为基础值；仅当某 token 存在与默认值不同的
**独立状态值**时才加 -{state} 后缀，没有独立状态值的 token 不加后缀。
这条规则本身要一致执行，不允许"有的加有的不加"的临时决定。
```css
:root {
  /* Color */
  --c-bg-page: ;
  --c-bg-surface: ;
  --c-bg-surface-hover: ;      /* 有独立 hover 值，加后缀 */
  --c-text-primary: ;
  --c-text-secondary: ;
  --c-border-default: ;
  --c-border-focus: ;          /* 有独立 focus 值，加后缀 */
  --c-state-success: ;
  --c-state-warning: ;
  --c-state-danger: ;

  /* Typography */
  --f-display: ;
  --f-body: ;
  --f-mono: ;
  --text-body-size: ;
  --text-body-leading: 1.6;

  /* Space */
  --s-1: ; --s-2: ; --s-3: ; --s-4: ; --s-6: ; --s-8: ;

  /* Motion */
  --m-duration-fast: ; --m-duration-base: ;
  --m-ease-out: ; --m-ease-spring: ;
}
```

## execution_rules

**交互状态**：`systemic` 模式下 default / hover / focus-visible / disabled /
loading 5 个状态是硬性下限，须在 final_code 中可定位到对应选择器。
expressive 模式可裁剪至叙事需要的子集，但 default / focus-visible /
disabled 三个属于无障碍下限（见下），任何模式都不可裁剪，
裁剪的只能是 loading/error 这类精细状态的动画表现。

**无障碍**（两种模式均不可裁剪，这是下限不是风格选项）：
- 语义化 HTML；ARIA 仅用于原生语义无法表达的场景
- 所有交互元素键盘可达，`focus-visible` 融入设计而非浏览器默认样式
- 触摸目标 ≥ 44px
- 表单校验有明确文案，不仅靠颜色区分

**性能**：动效仅用 `transform`/`opacity`；必须包含
@media (prefers-reduced-motion: reduce) 降级。

## conflict_disclosure（冲突披露协议——非 override 权限）

**触发条件**（收窄到客观冲突，不含审美/风格判断）：
生成过程中，两条或以上约束（`hard_constraints` / tailwind_discipline / execution_rules
无障碍下限 / 用户在本次任务中给出的具体要求）在**当前具体任务**下逻辑互斥，
无法同时满足——即满足其一必然违反另一。

**不构成触发条件**（这些一律走 self_critique 里的常规记录，不得升级为冲突）：
- "我认为这样更好看/更合理" —— 审美偏好不是冲突，是意图类表述，会被判违规
- 规则在通用意义上有已知摩擦或过时风险（如某工具版本的已知缺陷）
- 规则执行起来麻烦、但技术上可以同时满足

**权限边界**：
本节只授予"举手声明"权限，不授予"自行豁免"权限。模型不能替用户批准冲突，
不能静默降级任一约束，不能因为触发了本节就跳过 `revision_pass`。

**触发后的强制动作**：

```xml
<conflict_disclosure>
1. 冲突双方：逐字引用互斥的两条规则原文（不改写、不概括）
2. 客观证据：为什么二者在本次任务下不可能同时满足（技术事实，非偏好）
3. 默认执行：声明"本轮仍按 [规则X] 执行"，并说明这会导致 [规则Y] 在何处未被满足
4. 等待确认：final_code 不生成，停在此处，需用户明确选择后才继续
</conflict_disclosure>
```

如果单次生成中出现多条冲突，逐条列出每一条——不得合并、省略，也不得以"太多"为由选择性披露。

**与 `self_critique` 的关系**：
若 conflict_disclosure 被触发，它插入在 architecture_and_states 之后、self_critique 之前。
self_critique 中的对应项照常运行——冲突披露不替代例行自查，两者是叠加关系，非二选一。

**与建议式反馈的区分**：
关于规则本身的非冲突性改进建议（某条规则已过时、某工具行为已变化等）不归入本节。
它们遵循既有惯例——在 <design_thought> 中注明或在对话中另提——不影响当前任务执行。

## final_quality_gate

产出前逐条打勾，任一项为否则退回 `revision_pass`：

- [ ] preflight_qa 已按触发条件执行或明确跳过
- [ ] scenario_mode 已声明（含 auto-switch 判断）且贯穿全篇
- [ ] hard_constraints 五条均可在 self_critique 中定位到具体代码证据
- [ ] 若使用 Tailwind：主题已重写、无默认调色板残留、无未注释的 arbitrary value、重复类组合已提取
- [ ] 标志性元素功能性可验证（非纯装饰）
- [ ] 无障碍四要素齐全（语义/键盘可达+focus-visible/触摸目标/表单文案）
- [ ] token 命名的状态后缀规则一致执行
- [ ] conflict_disclosure 已触发并解决（或确认不适用）后才运行了此清单
- [ ] self_critique 与 final_code 的引用一一对应
- [ ] 无 lorem ipsum / 空状态无引导文案 / 默认浏览器错误态

## revision_pass

任一约束或终检项未通过时触发：仅重写未通过的具体部分，不得推倒重来全篇；
在输出末尾用一行注明"本轮修订项：X, Y"。
