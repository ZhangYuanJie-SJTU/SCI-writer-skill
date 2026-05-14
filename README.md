# SCI-writer

> **全链路科学综述论文自动化编排系统**  
> *从文献检索到投稿级 LaTeX 包——全程自动化、全程审计、全程可复现。*

[![版本](https://img.shields.io/badge/版本-4.1.0-blue)](SKILL.md)
[![目标期刊](https://img.shields.io/badge/目标-Q1%20%2F%20CAS--TOP-red)](SKILL.md)
[![质量门控](https://img.shields.io/badge/门控-A%20%2F%20B%20%2F%20C-green)](SKILL.md)
[![反幻觉](https://img.shields.io/badge/反幻觉-内置-orange)](SKILL.md)
[![流水线](https://img.shields.io/badge/流水线-11%20阶段-purple)](SKILL.md)

---

## 这是什么？

SCI-writer 是一个 **Claude Code Skill**，将科学综述论文的完整生命周期自动化编排——从领域差距分析、系统性文献检索、逐节撰写、同行评审模拟、LaTeX 编译，到投稿包组装，全程一条龙。

本 skill 在**上海交通大学自动化与感知学院 王侃课题组**开发并经实战验证，首发论文：

> *"Wearable Electrochemical Sensing Systems Based on Microneedle Arrays: A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals"*  
> 目标期刊：*Biosensors and Bioelectronics*（中科院一区 TOP）

skill **完全自包含**——不依赖任何伴侣 skill 即可运行完整流水线。若安装了加速器 skill（deep-research、academic-paper、paper-verification 等），会被自动检测并调用，缩短运行时间。

---

## 核心能力

| 能力 | 说明 |
|------|------|
| **11 阶段流水线** | 基础 → 建构 → 精炼 → 交付，含 3 个强制质量门控 |
| **3 个质量门控** | Gate A（语料库完整性）· Gate B（引文完整性 + 方法类型一致性）· Gate C（投稿就绪） |
| **反幻觉协议** | 四规则体系：引文溯源、数值可追溯、最高级必引用、方法类型一致 · `[V]/[U]/[N]/[X]/[M]` 标签分类 |
| **6 角色同行评审模拟** | 领域专家 · 邻域专家 · 方法学专家 · 临床/转化专家 · 魔鬼代言人 · 格式/集成审核员（R6） |
| **图片挂载核查（Stage 6.5）** | 用 Python 脚本自动检测注释状态的 `\includegraphics`、无 `\ref{}` 的孤儿图片、表格图例一致性 |
| **流水线状态持久化** | 每阶段完成后写入 `sci_writer_state.md`——跨会话/跨天 context compaction 后可用 `/sciw resume` 恢复 |
| **领域配置系统** | 内置可穿戴 MNA 电化学传感领域 YAML 配置；可适配任意研究领域 |
| **交付任务分类** | `[AUTO]` 项由 Claude 主动完成，`[USER]` 项仅需用户填写私人信息（电话/基金号） |
| **三级引文核查** | Tier 1（全量格式）· Tier 2（[N]/[U] 标记）· Tier 3（高风险：数值 + 最高级） |
| **分轮评分升级** | Stage 7 最多三轮：R1 均分 ≥78 → R2 均分 ≥80（P0 修订后）→ R3 均分 ≥82（P1 修订后） |

---

## 11 阶段流水线

```
┌─────────────────────────────────────────────────────┐
│                  第一阶段组 — 基础                    │
├─────────────────────────────────────────────────────┤
│  Stage 1   │ 领域调研与差距定位                       │
│  Stage 2   │ 文献采集（PRISMA 系统性检索）             │
│  ▓▓▓▓▓▓ GATE A：语料库完整性门控 ▓▓▓▓▓▓▓▓           │
├─────────────────────────────────────────────────────┤
│                  第二阶段组 — 建构                    │
├─────────────────────────────────────────────────────┤
│  Stage 3   │ 深度综合与知识提炼                       │
│  Stage 4   │ 叙事架构与大纲设计                       │
│  Stage 5   │ 逐节撰写（四遍质量协议）                  │
│  Stage 6   │ 图表与视觉叙事                           │
│  Stage 6.5 │ 图片挂载与交叉引用核查 ★ 新增            │
│  ▓▓▓▓▓▓ GATE B：引文完整性 + 方法类型核查 ▓▓▓▓▓▓    │
├─────────────────────────────────────────────────────┤
│                  第三阶段组 — 精炼                    │
├─────────────────────────────────────────────────────┤
│  Stage 7   │ 六角色同行评审模拟                       │
│  Stage 8   │ 修订与反驳工程                           │
│  Stage 9   │ 期刊格式化与 LaTeX 编译                  │
│  ▓▓▓▓▓▓ GATE C：投稿就绪检查 ▓▓▓▓▓▓▓▓▓▓▓▓          │
├─────────────────────────────────────────────────────┤
│                  第四阶段组 — 交付                    │
├─────────────────────────────────────────────────────┤
│  Stage 10  │ 投稿包组装                              │
└─────────────────────────────────────────────────────┘
★ Stage 6.5 是 v4.0 新增阶段，专门消灭最高频的 LaTeX 空白框故障
```

---

## 快速开始

### 安装

```bash
# 克隆到 Claude Code skills 目录（Mac/Linux）
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git ~/.claude/skills/SCI-writer

# Windows
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git "C:\Users\<你的用户名>\.claude\skills\SCI-writer"
```

### 在 Claude Code 中调用

```
# 从零开始一篇新综述
/SCI-writer

# 加载内置微针/可穿戴传感领域配置，直接开跑
/sciw load microneedle

# 全自动模式（每个 Gate 暂停等待确认）
/sciw auto

# 恢复中断的流水线（读取 sci_writer_state.md）
/sciw resume

# 跳转到指定阶段
/sciw stage 7

# 仅运行图片挂载核查
/sciw mount-check

# 仅运行 Gate B 引文审计
/sciw gate b

# 运行所有 Gate C 自动化验证脚本
/sciw verify all
```

---

## 三个质量门控详解

### Gate A — 语料库完整性

确保在撰写前，文献语料库足够大、足够多样、足够新。

- 总论文数 ≥150 篇（领域文献稀少时有例外路径：≥80 篇 + 补偿控制措施）
- 每个主要章节 ≥20 篇
- 2023–2026 年论文占比 ≥40%
- 至少 5 个 DOI 人工验证
- 每篇论文记录检测方法类型（供 Gate B 方法类型核查使用）
- 所有 BibTeX key 符合 `AuthorYYYYKeyword` 命名规范

### Gate B — 引文完整性 + 方法类型核查

反幻觉防火墙，三级核查体系：

| 级别 | 范围 | 核查内容 |
|------|------|---------|
| **Tier 1** | 所有引用 | BibTeX key 格式 + DOI 字段存在性 |
| **Tier 2** | `[N]` 和 `[U]` 标记的引用 | 标题 + 作者 + 年份 + 期刊 逐一确认 |
| **Tier 3** | 高风险（含具体数值、"first"、2025–2026 年、格式异常 DOI） | 具体指标在原文中的存在性确认 |

**方法类型一致性核查（SCI-writer 独有）**：荧光法论文被引用在 EIS 段落 = 自动标记 `[METHOD_X]`。被引论文的检测模态必须与引用语句所描述的方法一致。

### Gate C — 投稿就绪

终检清单：零图片挂载故障、零孤儿图片、R2 均分 ≥80/100、正文字数 8,000–15,000、摘要 ≤300 字、所有亮点 ≤85 字符。全部通过 Python 脚本自动验证。

---

## 反幻觉协议

四条规则，始终激活，不可关闭：

**规则 1 — 引文溯源规则**  
每个关于具体研究的声明必须有可验证的来源。没有来源 = `[NEEDS_REF]`，不允许自造引用。

**规则 2 — 数值规则**  
每个量化数值（LOD、灵敏度、MARD、p值）必须可追溯到被验证论文的具体表格或图。

**规则 3 — 最高级规则**  
"first"、"highest"、"only"、"unprecedented" 等词必须附引用。没有引用则改为中性表述："among the reported approaches..."

**规则 4 — 方法类型规则**  
被引论文的检测方法必须与引用语句所声明的方法一致。光学法 ≠ 电化学法。

**验证标签分类：**
```
[V]  已验证 — DOI 已确认，方法类型已确认
[U]  未独立验证 — 用户提供，未自主核查
[N]  待核查 — 在语料库中但尚未审计
[X]  核查失败 — 未找到；从草稿中删除
[M]  方法类型不匹配 — 论文存在但方法类型与引用语境冲突
```

---

## 6 位审稿人面板（Stage 7）

| 审稿人 | 审查重点 | 主要攻击方向 |
|--------|---------|------------|
| **R1** 领域专家 | 技术准确性、深度、覆盖完整性 | 遗漏关键文献；性能基准与原始论文不符 |
| **R2** 邻域专家 | 跨学科背景、与邻近领域的定位 | "邻域早就做了"；新颖性声明过度 |
| **R3** 方法学专家 | 系统性覆盖、综述本身的方法论 | 无 PRISMA 合规；纳入标准不清晰 |
| **R4** 临床/转化专家 | 临床相关性、监管路径、体内证据质量 | 体外结果被引作临床证据；无与商业金标准的对比 |
| **R5** 魔鬼代言人 | 核心论题连贯性 | "这是一篇统一综述还是把几个主题凑在一起？" |
| **R6** 格式/集成审核员 ★ | LaTeX 质量、图片挂载、期刊合规 | 注释状态的 `\includegraphics`；孤儿图片；亮点超 85 字符 |

★ R6 在 v4.0 中新增，因为实战发现格式类故障持续逃过前 5 位审稿人的检查。

分轮评分升级：R1 均分 ≥78 → R2 均分 ≥80 → R3 均分 ≥82

---

## Stage 6.5 — 图片挂载核查

v4.0 最有影响力的新增阶段，全部通过 Python 脚本自动执行：

- **注释状态 `\includegraphics` 检测** — 扫描 `% \includegraphics` 模式并自动取消注释
- **孤儿图片检测** — 每个 `\label{fig:X}` 必须在正文中有 ≥1 个 `\ref{fig:X}`
- **孤儿表格检测** — 每个 `\label{tab:X}` 必须在正文中有 ≥1 个 `\ref{tab:X}`
- **标题完整性** — 每个 figure 环境必须有非空 `\caption{}`
- **表格图例一致性** — 表格正文中使用的每个符号必须在 caption 中定义

**为什么这很重要**：图片文件生成后，`\includegraphics` 命令很容易仍处于注释状态（来自早期草稿阶段）。最终 PDF 渲染为空白框——一个在编译成功之前完全无声无息的故障。

---

## 流水线状态持久化

一篇综述需要 3–10 天。Context compaction 会发生多次。`sci_writer_state.md` 在每个阶段完成后写入磁盘，记录：

- 当前阶段与已完成阶段列表
- 每个 Gate 的通过/失败历史（含日期）
- Stage 7 评分历史（三轮全记录）
- 语料库状态（`[V]/[N]/[X]/[M]` 计数）
- 图片状态表
- 待处理的 `[AUTO]` 和 `[USER]` 项目

`/sciw resume` 读取该文件并从上次检查点继续。

---

## 领域配置系统

### 使用内置微针/可穿戴传感配置

```
/sciw load microneedle
```

预配置内容：
- 目标期刊：*Biosensors and Bioelectronics*
- 5 个检索簇（制备、传感模态、系统集成、嵌入式智能、临床验证）
- 7 个领域专属性能指标（葡萄糖 LOD、灵敏度、MARD、离子斜率等）
- 6 个需确保覆盖的关键课题组
- 检测方法分类体系（安培法、DPV、SWV、EIS、ISE、FSCV、荧光、SERS）
- 3 篇需要差异化对比的已有综述

### 自定义领域配置

创建 `domain-config.yaml` 文件并通过 `/sciw config load domain-config.yaml` 加载。YAML schema 支持：
- 论文元数据（标题、期刊、字数目标、参考文献目标数）
- 多查询检索簇
- 带单位和阈值的性能指标
- 检测方法分类体系（供 Gate B 方法类型核查）
- 需差异化的已有综述列表
- 独特贡献声明

---

## Gate C 自动验证脚本

所有脚本使用 Python 标准库，无需外部工具。

| 验证项 | 命令 | 标准 |
|--------|------|------|
| 摘要字数 | `/sciw verify abstract` | ≤300 词 |
| 亮点字符数 | `/sciw verify highlights` | 每条 ≤85 字符 |
| 正文字数估算 | `/sciw verify wordcount` | 8,000–15,000 词 |
| 参考文献计数 | `/sciw verify references` | ≥130 条 |
| 图片挂载状态 | `/sciw mount-check` | 零注释/零孤儿 |
| 全部验证 | `/sciw verify all` | 以上全部 |

---

## 电化学传感公式银行

skill 内置可穿戴电化学传感领域的 LaTeX 公式，可直接插入对应章节：

| 公式 | 用途 |
|------|------|
| Cottrell 方程 | 安培法电流-时间响应 |
| Randles–Ševčík 方程 | 伏安法峰电流 vs 扫描速率 |
| Nernst 方程 | 电位法/离子选择电极（斜率 59.2/z mV/decade） |
| Butler–Volmer 方程 | 电极动力学 |
| Randles 等效电路（EIS） | 阻抗谱分析 |
| LOD 公式（IUPAC） | 检测限 = 3σ_b / S |
| 灵敏度公式 | S = Δi/ΔC [μA mM⁻¹ cm⁻²] |

---

## 更新日志

### v4.1.0（2026-05-14）
- **流水线状态持久化** — `sci_writer_state.md` + `/sciw resume` 命令，彻底解决跨会话 pipeline 位置丢失问题
- **BibTeX key 命名规范** — `AuthorYYYYKeyword` 强制标准 + 自动合规性检查
- **Gate A 例外路径** — 领域文献稀少时（≥80 篇）的文档化补偿控制方案
- **Gate B 三级核查体系** — Tier 1/2/3 协议替代模糊的"高风险"启发式判断
- **四个 Python 验证脚本** — 摘要字数、亮点字符数、LaTeX 正文字数、参考文献计数，Gate C 全自动化
- **Stage 6.5：表格图例一致性检查** — 自动扫描 caption 定义符号 vs. 表格正文使用符号
- **Elsevier 模板下载 URL 修复** — `mirrors.ctan.org` 直链 + HTML 内容校验（原 `www.ctan.org/tex-archive` 是页面 URL 非直链）
- **Stage 7 阈值逻辑修正** — R1/R2/R3 三轮阈值表统一清晰，消除 Scoring Protocol 与 Score Escalation Rule 之间的自相矛盾

### v4.0.0（2026-05-14）
- **Stage 6.5** — 图片挂载与交叉引用核查（强制新阶段）
- **R6 审稿人** — 格式/集成审核员加入五角色面板，补齐格式盲区
- **Gate B Part 2** — 方法类型一致性核查；`[METHOD_X]` 标签
- **Gate C** — 交叉引用完整性；`\includegraphics` 非注释状态检查
- **Stage 10** — `[AUTO]`/`[USER]` 交付任务分类

### v3.0.0
- 首次发布：10 阶段流水线、Gates A/B/C、PRISMA 协议、5 角色评审模拟、内置微针领域配置

---

## 完整流水线运行后的文件结构

```
[项目根目录]/           ← 所有文件平铺（Editorial Manager 要求）
├── sci_writer_state.md ← 流水线状态（断点续传检查点）
├── main.tex            ← LaTeX 源文件（约 700–900 行）
├── references.bib      ← BibTeX 数据库（≥130 条，AuthorYYYYKeyword key）
├── generate_figures.py ← Python 图片生成脚本（matplotlib）
├── fig_01_*.png        ← 所有图片，≥300 DPI
├── ...
├── fig_0N_*.png
├── graphical_abstract.png  ← 400×300 px 石墨摘要
├── elsarticle.cls      ← [AUTO] 从 mirrors.ctan.org 自动下载
├── elsarticle-num.bst  ← [AUTO] 从 mirrors.ctan.org 自动下载
├── highlights.txt      ← 3–5 条，每条 ≤85 字符
├── cover_letter.md     ← 含 [USER] 占位符（电话/基金号）
├── revision_log.md     ← P0/P1 修订记录
├── review_report.md    ← 6 位审稿人评分（R1/R2/R3 三轮）
├── gate_c_checklist.md ← 所有项目 ✓
└── submission_package.zip  ← 可直接上传的投稿压缩包
```

---

## 兼容性

| 工具 | 必须 | 说明 |
|------|------|------|
| Claude Code | ✅ 必须 | 已在 Claude Sonnet 4.6+ 上测试 |
| Python（仅标准库） | ✅ 必须 | 图片生成与验证脚本 |
| matplotlib + numpy | 推荐 | Stage 6 Python 图片生成 |
| pdflatex | 可选 | LaTeX 编译；不可用时自动回退到 matplotlib |
| tavily-search skill | 推荐 | Stage 2 文献检索（Tier 1 检索通道） |
| deep-research skill | 可选 | PRISMA 模式系统性检索加速器 |
| paper-verification skill | 可选 | 批量 DOI 核查加速器 |

---

## 关于

**张元杰**（第一作者）· **王侃**（通讯作者，副教授）  
上海交通大学 自动化与感知学院  
联系方式：wangkan@sjtu.edu.cn

> *为想写论文、不想管工具的研究者而设计。*

---

*SCI-writer v4.1.0 · 上海交通大学 王侃课题组 · 2026-05-14*
