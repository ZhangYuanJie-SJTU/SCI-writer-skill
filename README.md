# SCI-writer

> **面向 Claude Code 的全流程综述论文编排系统**
> *从研究空白到投稿就绪的 LaTeX —— 一个 Skill 串联整条学术综述写作流水线，内置反幻觉协议、迭代质量循环、模型自适应脚手架与 Nature 级写作标准。*

[![Version](https://img.shields.io/badge/version-5.0.0-blue)](SKILL.md)
[![Target](https://img.shields.io/badge/target-Nature%20Comms%20%2F%20Q1%20%2F%20CAS--TOP-red)](SKILL.md)
[![Pipeline](https://img.shields.io/badge/pipeline-11%20stages-purple)](SKILL.md)
[![Gates](https://img.shields.io/badge/gates-A%20%2F%20B%20%2F%20C-green)](SKILL.md)
[![Reviewers](https://img.shields.io/badge/reviewers-8%20persona-orange)](SKILL.md)
[![Models](https://img.shields.io/badge/models-4--tier%20adaptive-yellow)](SKILL.md)
[![Affiliation](https://img.shields.io/badge/Affiliation-SJTU-blue)](https://www.sjtu.edu.cn)

---

## 这是什么

SCI-writer 是一个 **Claude Code Skill**，通过结构化的 11 阶段流水线 + 3 道强制质量门，将你的研究想法变成投稿就绪的综述论文。

**内置领域专精：** 可穿戴电化学传感 / 微针阵列研究（Biosensors and Bioelectronics、ACS Nano 等期刊完整配置）

**v5.0 核心升级：** 从"正确性系统"升级为"质量系统" —— 不仅保证不出错，更通过迭代循环、论证模板、叙事引擎和模型适配层，确保即使搭配 DeepSeek-V4-Flash / Mimo-v2.5-pro 等非顶尖模型，也能产出领域内高水平的综述文章。

---

## v5.0 更新日志

### 新增模块（v4.2 → v5.0）

| 模块 | 解决的问题 | 核心机制 |
|------|-----------|---------|
| **Thinking-First 协议** | 模型倾向于直接写、不先想 | 每个阶段强制显式推理后再行动，防止浅层分析 |
| **迭代写作循环** | 写完就走，不回头检查质量 | 每节循环 Think → Draft → Self-Review → Revise，5 维评分 ≥70 才通过 |
| **叙事流动引擎** | 各章节像"钉在一起"而非一个完整故事 | 论证弧线映射 + 过渡矩阵 + 桥接句协议 |
| **论证结构模板** | 事实正确但论证薄弱 | AREI 模式（主张 → 证据 → 推理 → 启示）嵌入每个主要小节 |
| **多尺度质量系统** | 只在最后才检查质量 | 段落级(7 项) → 节级(5 维×20 分) → 论文级(10 项) |
| **模型适配层** | 一套 prompt 无法适应所有模型 | 4 级自动检测：Frontier / Strong / Efficient / Lightweight |
| **写作质量词库** | 模型不知道"好文章"长什么样 | 精选范句：开头钩子、证据整合、过渡句、结论写法 |
| **R8 写作质量审稿人** | 现有 7 位审稿人不评估文笔质量 | 第 8 位审稿人按 Nature Comms 标准评估散文质量 |
| **自纠正协议** | 弱模型容易生成自信但错误的内容 | 自动不确定性检测 → 针对性再验证 |
| **Nature 级写作基准** | 缺乏具体的"好文章"评判标准 | 开头钩子、视觉叙事、启示优先结论、精密数据解读 |

### 继承自 v4.2

统一教学-严谨框架 · 测量仪器链认知模型 · 搜索模式 D/E/F（基础/中文/商业）· 知识脚手架(Sub-stage 4.5) · 教学增强(Pass 2.5) · R7 新手模拟器 · 决策流程图 · 商业基准 · 中国研究团队

---

## 快速开始

### 第一步 — 安装

**Windows：**
```powershell
./install.ps1
```

**Mac / Linux：**
```bash
chmod +x install.sh && ./install.sh
```

**手动安装：**
```bash
cp -r skills/SCI-writer ~/.claude/skills/
```

### 第二步 — 启动流水线

```
/sciw load microneedle      ← 加载内置微针/电化学传感配置
/sciw init                   ← 交互式配置任意领域
```

### 第三步 — 运行

```
/sciw auto                   ← 全自动模式（在每道 Gate 暂停等待确认）
/sciw stage 2                ← 跳转到指定阶段
/sciw resume                 ← 从上次断点继续
/sciw status                 ← 查看进度
```

---

## 11 阶段流水线

```
PHASE I  — 基础建设
  Stage 1   │ 领域情报与空白映射（+ 技术历史 + 统一框架）
  Stage 2   │ 文献获取与语料库构建（8 种搜索模式）
  ▓▓▓▓▓▓▓▓▓ GATE A: 语料库完整性 ▓▓▓▓▓▓▓▓▓

PHASE II — 内容构建
  Stage 3   │ 深度综合与知识提取（+ 概念地图）
  Stage 4   │ 叙事架构与大纲设计（+ 论证地图 + 过渡矩阵）
  Stage 5   │ 迭代式逐节撰写（Think→Draft→Review→Revise 循环，5 维评分）
  Stage 6   │ 图表与视觉叙事
  Stage 6.5 │ 图表挂载与交叉引用验证
  ▓▓▓▓▓▓▓▓▓ GATE B: 引用完整性 + 方法类型审计 ▓▓▓▓▓▓▓▓▓

PHASE III — 精打磨
  Stage 7   │ 多角色同行评审模拟（8 位审稿人：R1–R8）
  Stage 8   │ 修稿与回复信工程
  Stage 9   │ 期刊格式化与 LaTeX 编译
  ▓▓▓▓▓▓▓▓▓ GATE C: 投稿就绪检查 ▓▓▓▓▓▓▓▓▓

PHASE IV — 交付
  Stage 10  │ 投稿包组装
```

---

## 核心特性

### 反幻觉三道门

三道强制停止点，不可跳过：

| 门 | 检查内容 | 通过标准 |
|----|---------|---------|
| **Gate A** | 语料库完整性 | ≥150 篇论文，每节 ≥20 篇，近 3 年 ≥40% |
| **Gate B** | 引用完整性 + 方法类型一致性 | 零 `[NOT_FOUND]`、零 `[MISMATCH]`、零 `[METHOD_X]` |
| **Gate C** | 投稿就绪 | 审稿人均分 ≥80，R7 ≥70，R8 ≥70，零未解决引用 |

### 迭代写作质量循环（v5.0 新增）

每节通过 Think → Draft → Self-Review → Revise 循环，直到质量达标：

```
┌─────────┐   ┌─────────┐   ┌──────────┐   ┌──────────┐
│  思考    │──▶│  初稿    │──▶│  自审     │──▶│  修订     │
│ (1 min) │   │ (20 min)│   │ (5 min)  │   │ (10 min) │
└─────────┘   └─────────┘   └──────────┘   └────┬─────┘
     ▲                                           │
     │           评分 < 70                        │
     └───────────────────────────────────────────┘
```

**5 维评分体系（每维 20 分，满分 100）：**

| 维度 | 评估内容 |
|------|---------|
| 论证强度 | 本节是否证明了其中心论点？ |
| 证据质量 | 每个论点是否有验证过的数据支撑？ |
| 叙事流畅 | 是否读起来像一个连贯的故事，而非事实罗列？ |
| 教学价值 | 新手能否从中学到东西？概念是否渐进引入？ |
| Nature 级文笔 | 开头是否有钩子？句式是否多样？是否有空话废话？ |

### 8 位审稿人同行评审模拟

| 审稿人 | 职责 | 攻击向量示例 |
|--------|------|------------|
| R1 领域专家 | 技术准确性、深度 | "你遗漏了 [重要团队] 的关键工作" |
| R2 相邻领域专家 | 跨学科定位 | "这在 [相邻领域] 已经做得更好了" |
| R3 方法/严谨性专家 | 综述方法论 | "没有描述搜索方法（不符合 PRISMA）" |
| R4 临床/转化专家 | 临床相关性 | "体外结果被引用为临床证据" |
| R5 魔鬼代言人 | 中心论点挑战 | "这真的是一篇统一的综述还是 N 个相邻主题拼凑的？" |
| R6 格式审计 | LaTeX / 交叉引用 | "图 X 在文中引用了但没有显示" |
| R7 新手模拟器 | 可读性 | "研一新生读完能画出系统框图吗？" |
| R8 写作质量审计 | 散文质量 | "§X 的开头是'本节将讨论...' —— 与 Nature 级质量格格不入" |

### 模型适配层（v5.0 新增）

自动检测模型能力等级，调整脚手架深度：

| 模型层级 | 代表模型 | 迭代次数 | 脚手架策略 |
|---------|---------|---------|-----------|
| **Tier 1 Frontier** | Claude Opus | 1 | 最小 — 信任模型判断 |
| **Tier 2 Strong** | Claude Sonnet, DeepSeek-V3 | 2 | 中等 — 结构化提示 + 自审清单 |
| **Tier 3 Efficient** | DeepSeek-V4-Pro, Mimo-v2.5-pro | 2-3 | 重型 — 段落模板 + 推理链 + 填空式 |
| **Tier 4 Lightweight** | DeepSeek-V4-Flash | 3 | 最大 — 句首提示 + 强制逐条事实核查 |

使用 `/sciw detect-model` 查看当前检测结果，`/sciw set-model [1-4]` 手动覆盖。

---

## 完整命令参考

| 命令 | 功能 |
|------|------|
| `/sciw init` | 交互式配置标题、期刊、领域 |
| `/sciw load microneedle` | 加载内置微针/电化学传感配置 |
| `/sciw start` | 从 Stage 1 开始运行 |
| `/sciw auto` | 全自动模式（Gate 处暂停） |
| `/sciw stage [1-10]` | 跳转到指定阶段 |
| `/sciw stage 6.5` | 仅运行图表挂载 + 交叉引用审计 |
| `/sciw gate [a/b/c]` | 仅运行指定质量门 |
| `/sciw search [query]` | 文献搜索模式 |
| `/sciw write [section]` | 撰写指定章节 |
| `/sciw review` | 运行同行评审模拟 |
| `/sciw verify` | 引用审计 |
| `/sciw resume` | 从上次断点继续 |
| `/sciw status` | 查看流水线进度 |
| `/sciw export` | 生成投稿包 |
| `/sciw detect-model` | 显示模型层级检测结果 |
| `/sciw set-model [1-4]` | 手动覆盖模型层级 |

---

## 项目结构

```
SCI-writer/
├── SKILL.md                         ← 主技能文件（2600+ 行，完整流水线逻辑）
├── BOOTSTRAP.md                     ← 轻量引导文件（~80 行，按需加载 SKILL.md 对应节）
├── README.md                        ← 本文件
├── install.ps1                      ← Windows 一键安装脚本
├── install.sh                       ← Mac/Linux 一键安装脚本
├── scripts/
│   ├── verify_stage65.py            ← Stage 6.5 图表挂载 + 交叉引用验证
│   ├── verify_gate_b.py             ← Gate B 引用完整性 + BibTeX 审计
│   ├── verify_gate_c.py             ← Gate C 投稿就绪检查（摘要/正文/图表）
│   └── download_templates.py        ← Elsevier LaTeX 模板下载
└── templates/
    ├── microneedle-sensing.yaml     ← 内置领域配置：微针/电化学传感（v2.0）
    ├── generic-review.yaml          ← 通用领域空白模板（填空即用）
    └── cover-letter-template.md     ← Cover letter 模板
```

**安装方式：**

```powershell
# Windows
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git
cd SCI-writer-skill
.\install.ps1

# Mac/Linux
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git
cd SCI-writer-skill
chmod +x install.sh && ./install.sh
```

安装脚本会自动将所有文件复制到 `~/.claude/skills/SCI-writer/` 并验证完整性。

**验证脚本使用：**

```bash
# 在论文项目目录下运行
python ~/.claude/skills/SCI-writer/scripts/verify_stage65.py   # Stage 6.5 检查
python ~/.claude/skills/SCI-writer/scripts/verify_gate_b.py    # Gate B 检查
python ~/.claude/skills/SCI-writer/scripts/verify_gate_c.py    # Gate C 检查
python ~/.claude/skills/SCI-writer/scripts/download_templates.py  # 下载 Elsevier 模板
```

所有脚本纯 Python 标准库，零依赖。

---

## 内置领域：可穿戴电化学传感 / 微针阵列

针对 **Biosensors and Bioelectronics** 投稿深度优化，使用**测量仪器链框架**统一叙事：

```
被测量 → 前端感知 → 信号产生 → 信号调理 → 数据处理 → 临床输出
分析物    微针制造    电化学模态    AFE电路    嵌入式AI    诊断/治疗
```

**领域配置亮点：**

| 配置项 | 内容 |
|--------|------|
| 文献搜索集群 | 8 个：制造材料 / 电化学模态 / 系统集成 / 嵌入式智能 / 临床验证 / 基础教程 / 中文文献 / 商业工业 |
| 性能指标基准 | 14 项：LOD、灵敏度、线性范围、MARD、选择性系数等 |
| 商业 CGM 基准 | 4 款：Dexcom G7 / FreeStyle Libre 3 / Guardian 4 / Eversense 365 |
| 关键研究团队 | 17+ 组：国际 10 组（Wang/Javey/Gao/Lee 等）+ 中国 7 组（常凌乾/李卓/朱勇等） |
| 技术里程碑 | 9 个：2000→2026 年关键节点 |
| 决策流程图 | 2 个：材料×构型选择 + 感知模态选择矩阵 |
| 开放问题 | 15 个：含优先级（高/中/低）和难度评级 |

---

## 可选伴侣技能

以下技能增强能力但**不是必需的** —— 零安装时流水线完整运行，所有能力内置于 SKILL.md：

| 技能 | 增强阶段 | 提供的能力 |
|------|---------|-----------|
| `academic-paper` | Stage 5 | 12 agent 并行写作 |
| `academic-paper-reviewer` | Stage 7 | 自动化 5 角色评审 |
| `deep-research` | Stage 2 | 多数据库 PRISMA 系统搜索 |
| `paper-verification` | Gate B | 批量 DOI 检查 |
| `arxiv-search` | Stage 2 | arXiv 实时搜索 |
| `scientific-visualization` | Stage 6 | 专业图表生成 |
| `latex-document` | Stage 9 | LaTeX 编译 |

---

## 流水线状态持久化

每次阶段完成后自动写入 `sci_writer_state.md`，记录：
- 当前流水线位置和已完成阶段
- 三道 Gate 的通过/失败状态
- Stage 7 每轮评分历史
- 语料库验证状态
- 图表生成状态
- 待办事项列表

流水线可跨会话、跨天数运行。使用 `/sciw resume` 从断点继续。

---

## 引用

如果你在研究中使用了 SCI-writer，请引用：

```bibtex
@software{SCI-writer2026,
  author = {Zhang, Yuanjie and Wang, Kan},
  title  = {SCI-writer: Full-Chain Scientific Review Paper Orchestration System},
  year   = {2026},
  url    = {https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill}
}
```

---

*SCI-writer v5.0.0 — 为想写论文而非管工具的研究者设计。*
*SJTU Wang Lab | 张元杰 + 王侃 | Updated: 2026-05-29*
