# 设计交付文档 · 小红书品牌版
## 给开发者和AI用的技术翻译

---

## 使用说明

这份文档是品牌灵魂备忘录的技术版本。
备忘录是给客户感受用的，这份是给执行用的。
用术语，要精确，可以直接复制进代码。

---

## CSS 设计令牌模板

```css
/* ============================================
   [项目名] · 设计令牌系统
   来源：品牌灵魂发现会话
   日期：[日期]
   平台：小红书 / Web / App
   ============================================ */

:root {

  /* --- 背景色系 ---
     感觉描述：[例如"像日落前的暖光，不是纯白也不是灰"] */
  --color-base:        [hex];   /* 主背景 · [感觉描述] */
  --color-surface:     [hex];   /* 卡片/内容区 · 微微区分 */
  --color-elevated:    [hex];   /* 悬浮层/弹窗 */

  /* --- 文字色系 --- */
  --color-text-primary:   [hex];   /* 主文字 · 不用纯黑 */
  --color-text-secondary: [hex];   /* 次要信息 */
  --color-text-muted:     [hex];   /* 标签/时间/辅助 */

  /* --- 品牌记忆色 ---
     这是用户在100条内容里认出你的那个颜色
     全屏最多占比：[X]% */
  --color-brand:       [hex];   /* [感觉] · 记忆色 */
  --color-brand-soft:  [hex];   /* 浅版 · 背景/标签用 */
  --color-brand-deep:  [hex];   /* 深版 · hover/强调用 */

  /* --- 情绪色 ---
     品牌的"那一刻" · 每页最多一处 */
  --color-moment:      [hex];   /* [感觉] · 最大一处/页 */

  /* --- 功能色 --- */
  --color-success:     [hex];
  --color-warning:     [hex];
  --color-error:       [hex];
  --color-info:        [hex];

  /* --- 边框 --- */
  --border-light:   rgba([r],[g],[b], 0.08);
  --border-default: rgba([r],[g],[b], 0.15);
  --border-brand:   rgba([r],[g],[b], 0.30);

  /* ============================================
     字体系统
     品牌调性：[例如"编辑感·不是日记感也不是理工感"]
     ============================================ */

  /* 字体 */
  --font-display:  '[展示字体]', '[备用]', serif;    /* 标题·有个性 */
  --font-body:     '[正文字体]', '[备用]', sans-serif; /* 正文·可读 */
  --font-mono:     '[等宽字体]', monospace;            /* 代码/数字 */

  /* 中文字体补充 */
  --font-cn-display: '[中文展示字体]', sans-serif;  /* 可选：有设计感的中文 */
  --font-cn-body:    '[中文正文字体]', sans-serif;  /* 可读性优先 */

  /* 字号 · 用clamp实现流体排版 */
  --text-hero:     clamp([min]rem, [vw]vw, [max]rem);  /* 大标题 */
  --text-h1:       clamp([min]rem, [vw]vw, [max]rem);
  --text-h2:       clamp([min]rem, [vw]vw, [max]rem);
  --text-h3:       [size]rem;
  --text-body-lg:  [size]rem;   /* 大号正文 */
  --text-body:     [size]rem;   /* 默认正文 · 移动端最小16px */
  --text-body-sm:  [size]rem;   /* 小字 · 标签/时间 */
  --text-eyebrow:  [size]rem;   /* 眉标 · 全大写小字 */

  /* 字间距 */
  --tracking-tight:  -0.02em;  /* 大标题收紧 */
  --tracking-normal:  0.01em;
  --tracking-wide:    0.08em;
  --tracking-xwide:   0.20em;  /* 眉标/全大写 */

  /* 行高 */
  --leading-display: [value];   /* 展示文字 · 通常1.1-1.2 */
  --leading-body:    [value];   /* 正文 · 通常1.6-1.8 · 中文推荐1.8 */
  --leading-relaxed: [value];   /* 宽松 · 长文阅读 · 通常1.9-2.0 */

  /* ============================================
     动效系统
     节奏描述：[例如"慢电影感，不是app弹窗感"]
     ============================================ */

  --ease-smooth:    cubic-bezier(0.25, 0.1, 0.25, 1);
  --ease-appear:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-disappear: cubic-bezier(0.4, 0, 1, 1);

  --duration-fast:     150ms;   /* hover状态切换 */
  --duration-normal:   350ms;   /* 标准过渡 */
  --duration-slow:     700ms;   /* 内容出现 */
  --duration-brand:   1200ms;   /* 品牌记忆时刻 · 全页最多用一次 */

  /* ============================================
     间距系统
     ============================================ */
  --space-1:  0.25rem;   /* 4px */
  --space-2:  0.5rem;    /* 8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-24: 6rem;      /* 96px */

  /* ============================================
     圆角
     ============================================ */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   20px;
  --radius-full: 9999px;   /* 胶囊形 */

}
```

---

## 小红书端特殊规则

```css
/* 移动端优先 · 小红书主要在手机上看 */
/* 所有设计以375px为基准，向上兼容 */

/* 安全区域 */
.content-safe {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
  padding-bottom: env(safe-area-inset-bottom);
}

/* 图片比例 · 小红书推荐 */
.image-xhs-vertical   { aspect-ratio: 3 / 4; }   /* 竖版笔记封面 */
.image-xhs-square     { aspect-ratio: 1 / 1; }   /* 方形 */
.image-xhs-horizontal { aspect-ratio: 16 / 9; }  /* 横版 */

/* 触摸目标 · 最小44px */
.touch-target {
  min-height: 44px;
  min-width: 44px;
}
```

---

## 开发者铁律

```
品牌规则 · [项目名]
来源：品牌发现会话
日期：[日期]

以下规则不可违背：

1. [来自brief的规则 · 例如"背景色永远不用纯白#ffffff，用--color-base"]
2. [例如"--color-brand 在任何屏幕上最多占 X%"]
3. [例如"--color-moment 每页最多出现一次"]
4. [例如"所有标题用--font-display，所有正文用--font-body，不混用"]
5. [例如"品牌记忆时刻动效只用--duration-brand，不可加速"]
6. [例如"不用纯黑色文字，用--color-text-primary"]
7. [例如"图片不过度精修，保留真实感"]
8. [例如"移动端正文字号最小16px，不可更小"]
```

---

## 字体层级速查

```
大标题/Hero：   --font-display · --text-hero · --leading-display
               letter-spacing: --tracking-tight

页面标题H1：    --font-display · --text-h1 · --leading-display

章节标题H2：    --font-display · --text-h2 · --leading-display

小标题H3：      --font-body (medium) · --text-h3 · --leading-body

眉标/标签：     --font-body · --text-eyebrow · --tracking-xwide
               text-transform: uppercase · color: --color-brand

正文：          --font-body · --text-body · --leading-body
               color: --color-text-primary

辅助文字：      --font-body · --text-body-sm · --leading-body
               color: --color-text-secondary

时间/标签：     --font-body · --text-body-sm
               color: --color-text-muted
```

---

## 动效速查

```
普通hover：     transition: [属性] var(--duration-normal) var(--ease-smooth)

内容出现：      opacity: 0 → 1, transform: translateY(12px) → 0
               transition: var(--duration-slow) var(--ease-appear)

品牌时刻：      [该页面最特别的那个元素]
               transition: var(--duration-brand) var(--ease-appear)
               全页只用一次，这是让用户停下来的那一刻

减弱动效：      @media (prefers-reduced-motion: reduce) {
                 --duration-brand: 0ms !important;
                 --duration-slow: 0ms !important;
               }
```

---

## 小红书内容尺寸规范

```
笔记封面（推荐）：  1242 × 1660px（3:4）
                    或 1080 × 1440px

方形封面：          1080 × 1080px

视频封面：          1080 × 1920px（9:16竖版）

头像：              圆形，200 × 200px最小

主页Banner：        不同手机显示不同，设计要居中安全区
```

---

## 组件备注

*品牌发现完成后，在这里补充项目特有的组件说明*

示例条目：
- 导航栏：[行为描述]
- 内容卡片：[风格方向]
- 品牌记忆元素：[是什么？在哪里？触发条件？]
- 彩蛋/隐藏惊喜：[位置？触发？展示什么？]
- 小红书笔记封面模板：[风格规范]

---

## 无障碍检查

```
对比度最低要求：
- 正文文字：4.5:1（WCAG AA）
- 大字/标题：3:1
- 图标/UI元素：3:1

重点检查色组合：
- --color-text-primary on --color-base
- --color-text-primary on --color-surface  
- --color-brand on --color-base
- 白字 on --color-brand

字号：移动端正文最小 16px
触摸目标：最小 44×44px
```
