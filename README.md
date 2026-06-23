# SCI-writer

> **面向 Claude Code 的全流程综述论文编排系统**
> *从研究空白到投稿就绪的 LaTeX —— 一个 Skill 串联整条学术综述写作流水线，内置反幻觉协议、确认闸门、术语分类账、AI 伦理红绿灯、迭代质量循环、模型自适应脚手架与 Nature 级写作标准。*

[![Version](https://img.shields.io/badge/version-5.2.0-blue)](SKILL.md)
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

**v5.2 核心升级：** 生态系统吸收大版本 —— 吸收了 skills.sh 上 20+ 个优质科研辅助 skill 的最佳实践（nature-skills 11 件套、literature-review、peer-review、scientific-writing、citation-management、infographics、markdown-mermaid-writing 等），新增确认闸门（缺失前提即硬停）、术语分类账（写前主动提取规范词汇）、故障模式层级（L1→L5 严格修复优先级）、AI 伦理红绿灯、审稿红线等 6 项安全网机制。

---

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git
cd SCI-writer-skill

# Windows
.\install.ps1

# Mac/Linux
chmod +x install.sh && ./install.sh
```

安装脚本自动完成：复制 SKILL.md + 模板 + 脚本到 `~/.claude/skills/SCI-writer/` → 验证所有文件完整性。

### 启动

在 Claude Code 中运行：

```
/sciw load microneedle      ← 加载内置微针/电化学传感配置，直接开始
/sciw init                   ← 交互式配置任意领域
```

### 常用操作

```
/sciw auto                   ← 全自动模式（在每道 Gate 暂停等待确认）
/sciw stage 2                ← 跳转到指定阶段
/sciw resume                 ← 从上次断点继续
/sciw status                 ← 查看进度
/sciw export                 ← 生成投稿包
```

---

## 项目结构

```
SCI-writer/
├── SKILL.md                         ← 主技能文件（完整流水线逻辑，3088 行）
├── BOOTSTRAP.md                     ← 轻量引导（按需加载 SKILL.md 对应节）
├── README.md                        ← 本文件
├── install.ps1                      ← Windows 一键安装
├── install.sh                       ← Mac/Linux 一键安装
├── scripts/
│   ├── verify_stage65.py            ← Stage 6.5 图表挂载 + 交叉引用验证
│   ├── verify_gate_b.py             ← Gate B 引用完整性 + BibTeX 审计
│   ├── verify_gate_c.py             ← Gate C 投稿就绪检查
│   └── download_templates.py        ← Elsevier LaTeX 模板下载
└── templates/
    ├── microneedle-sensing.yaml     ← 内置领域配置：微针/电化学传感
    ├── generic-review.yaml          ← 通用领域空白模板（填空即用）
    └── cover-letter-template.md     ← Cover letter 模板
```

---

## 11 阶段流水线

```
PHASE I  — 基础建设
  Stage 1   │ 领域情报与空白映射（+ 技术历史 + 统一框架）
  Stage 2   │ 文献获取与语料库构建（7 种搜索模式 + 引用链 + Mermaid PRISMA 流程图）
  ▓▓▓▓▓▓▓▓▓ GATE A: 语料库完整性 ▓▓▓▓▓▓▓▓▓

PHASE II — 内容构建
  Stage 3   │ 深度综合与知识提取（+ 概念地图 + 正式研究质量评估）
  Stage 3.5 │ 术语分类账（写前主动提取规范词汇，全篇强制一致）
  Stage 4   │ 叙事架构与大纲设计（+ 论证地图 + 过渡矩阵）
  Stage 5   │ 迭代式逐节撰写（Think→Draft→Review→Revise 循环，5 维评分）
  Stage 6   │ 图表与视觉叙事（图形摘要强制 + 色盲友好协议 + Mermaid 图优先）
  Stage 6.5 │ 图表挂载与交叉引用验证
  ▓▓▓▓▓▓▓▓▓ GATE B: 引用完整性 + 方法类型审计 + 多源验证 ▓▓▓▓▓▓▓▓▓

PHASE III — 精打磨
  Stage 7   │ 多角色同行评审模拟（8 位审稿人：R1–R8 + 结构化报告 + 审稿红线）
  Stage 8   │ 修稿与回复信工程
  Stage 9   │ 期刊格式化与 LaTeX 编译
  ▓▓▓▓▓▓▓▓▓ GATE C: 投稿就绪检查（期刊层级自适应阈值）▓▓▓▓▓▓▓▓▓

PHASE IV — 交付
  Stage 10  │ 投稿包组装
```

---

## 核心特性

### 反幻觉 + AI 伦理双重安全网

| 机制 | 内容 |
|------|------|
| **四条反幻觉规则** | 引用溯源 · 数字溯源 · 最高级词必引用 · 方法类型一致性（Always active） |
| **AI 伦理红绿灯** | 🟢 绿（语法/大纲/翻译）· 🟡 黄（方法撰写需人控）· 🔴 红（严禁自编论点/文献/上传未发表手稿） |
| **确认闸门** | 写作前 claim/evidence/boundary 三项缺一即硬停，不在错误前提下盲目写 |
| **三道 Gate** | Gate A 语料库 · Gate B 引用+多源验证 · Gate C 投稿就绪 |

### 三道 Gate

| 门 | 检查内容 | 通过标准 |
|----|---------|---------|
| **Gate A** | 语料库完整性 | ≥150 篇论文，每节 ≥20 篇，近 3 年 ≥40% |
| **Gate B** | 引用完整性 + 方法类型一致性 + 多源验证 | 零 `[NOT_FOUND]`、零 `[MISMATCH]`、零 `[METHOD_X]` |
| **Gate C** | 投稿就绪（期刊层级自适应） | Tier 1 (Nature/Science): ≥85 · Tier 2 (Q1): ≥80 · Tier 3-4: ≥70-75 |

### 迭代写作质量循环

```
┌─────────┐   ┌─────────┐   ┌──────────┐   ┌──────────┐
│  思考    │──▶│  初稿    │──▶│  自审     │──▶│  修订     │
│ (1 min) │   │ (20 min)│   │ (5 min)  │   │ (10 min) │
└─────────┘   └─────────┘   └──────────┘   └────┬─────┘
     ▲                                           │
     │           评分 < 70                        │
     └───────────────────────────────────────────┘
```

5 维评分（每维 20 分，满分 100）：论证强度 · 证据质量 · 叙事流畅 · 教学价值 · Nature 级文笔

**故障模式层级（v5.2）：** 修复严格按 L1→L5 顺序 —— Paper Type → Section Job → Paragraph Logic → Claim/Evidence/Boundary → Sentence Polish。永远不在结构错误时润色句子。

### 8 位审稿人

| 审稿人 | 职责 |
|--------|------|
| R1 领域专家 | 技术准确性、深度 |
| R2 相邻领域专家 | 跨学科定位 |
| R3 方法/严谨性专家 | 综述方法论 |
| R4 临床/转化专家 | 临床相关性 |
| R5 魔鬼代言人 | 中心论点挑战 |
| R6 格式审计 | LaTeX / 交叉引用 |
| R7 新手模拟器 | 研一新生能否读懂？ |
| R8 写作质量审计 | Nature Comms 级散文质量 |

**审稿红线（v5.2）：** 7 条绝对禁令 —— 不编审稿人身份、不编实验、不编引用、不做编辑决定。

### 模型适配层

| 模型层级 | 代表模型 | 迭代次数 | 脚手架策略 |
|---------|---------|---------|-----------|
| Tier 1 Frontier | Claude Opus, GPT-4o | 1 | 最小 |
| Tier 2 Strong | Claude Sonnet, DeepSeek-V3 | 2 | 中等 |
| Tier 3 Efficient | DeepSeek-V4-Pro, Mimo-v2.5-pro | 2-3 | 重型：模板 + 推理链 |
| Tier 4 Lightweight | DeepSeek-V4-Flash | 3 | 最大：填空式 + 强制核查 |

### v5.1 → v5.2 新增（Nature-Skills 吸收）

| 新特性 | 说明 |
|--------|------|
| **确认闸门** | claim/evidence/boundary 缺失即硬停，不在错误前提下盲目写 |
| **术语分类账** | Stage 3.5 写前主动提取规范词汇，全篇强制一致 |
| **故障模式层级** | L1→L5 严格修复优先级，永远不在结构错误时润色句子 |
| **AI 伦理红绿灯** | 🟢🟡🔴 三级 AI 学术写作边界 |
| **审稿红线** | Stage 7 7 条绝对禁令 |
| **按需加载原则** | detect context → load only what's needed |

### v5.0 → v5.1 新增（生态系统吸收）

| 新特性 | 说明 |
|--------|------|
| **Mermaid PRISMA 流程图** | 文本即源码，git-diff 友好，零外部依赖 |
| **图形摘要强制** | 1200×600px 首先生成，色盲友好协议 |
| **引用链搜索 (Pattern G)** | 前向引用 + 后向引用 |
| **正式研究质量评估** | Cochrane RoB / AMSTAR 2 / Newcastle-Ottawa / GRADE |
| **领域语言一致性检查** | 同义词漂移、基因命名、IUPAC、SI 单位 |
| **多源引用验证** | CrossRef + PubMed + arXiv + DataCite |
| **期刊层级质量阈值** | Tier 1 (≥85) → Tier 4 (≥70) |
| **结构化审稿报告** | Summary→Major→Minor→Line-by-Line→Questions |

---

## 命令参考

| 命令 | 功能 |
|------|------|
| `/sciw init` | 交互式配置标题、期刊、领域 |
| `/sciw load microneedle` | 加载内置微针配置 |
| `/sciw start` | 从 Stage 1 开始 |
| `/sciw auto` | 全自动模式（Gate 处暂停） |
| `/sciw stage [1-10]` | 跳转到指定阶段 |
| `/sciw stage 6.5` | 仅运行图表挂载审计 |
| `/sciw gate [a/b/c]` | 仅运行指定质量门 |
| `/sciw search [query]` | 文献搜索 |
| `/sciw write [section]` | 撰写指定章节 |
| `/sciw review` | 同行评审模拟 |
| `/sciw verify` | 引用审计 |
| `/sciw resume` | 从断点继续 |
| `/sciw status` | 查看进度 |
| `/sciw export` | 生成投稿包 |
| `/sciw detect-model` | 检测模型层级 |
| `/sciw set-model [1-4]` | 手动覆盖模型层级 |

---

## 验证脚本

所有脚本在论文项目目录下运行，纯 Python 标准库，零依赖：

```bash
python ~/.claude/skills/SCI-writer/scripts/verify_stage65.py     # Stage 6.5: 图表 + 交叉引用
python ~/.claude/skills/SCI-writer/scripts/verify_gate_b.py      # Gate B: BibTeX + DOI + NEEDS_REF
python ~/.claude/skills/SCI-writer/scripts/verify_gate_c.py      # Gate C: 摘要/正文/字数/图表
python ~/.claude/skills/SCI-writer/scripts/download_templates.py  # 下载 elsarticle.cls + .bst
```

---

## 内置领域：可穿戴电化学传感 / 微针阵列

针对 **Biosensors and Bioelectronics** 投稿深度优化，使用**测量仪器链框架**统一叙事：

```
被测量 → 前端感知 → 信号产生 → 信号调理 → 数据处理 → 临床输出
分析物    微针制造    电化学模态    AFE电路    嵌入式AI    诊断/治疗
```

| 配置项 | 内容 |
|--------|------|
| 文献搜索集群 | 8 个：制造材料 / 电化学模态 / 系统集成 / 嵌入式智能 / 临床验证 / 基础教程 / 中文文献 / 商业工业 |
| 性能指标基准 | 14 项：LOD、灵敏度、线性范围、MARD、选择性系数等 |
| 商业 CGM 基准 | 4 款：Dexcom G7 / FreeStyle Libre 3 / Guardian 4 / Eversense 365 |
| 关键研究团队 | 17+ 组：国际 10 组 + 中国 7 组 |
| 开放问题 | 15 个：含优先级和难度评级 |

---

## 可选伴侣技能

零安装时流水线完整运行，以下技能提供额外加速：

| 技能 | 增强阶段 |
|------|---------|
| `academic-paper` | Stage 5 — 12 agent 并行写作 |
| `academic-paper-reviewer` | Stage 7 — 自动化评审 |
| `deep-research` | Stage 2 — 多数据库 PRISMA 搜索 |
| `literature-review` | Stage 2 — 结构化系统综述 |
| `paper-verification` | Gate B — 批量 DOI 检查 |
| `citation-management` | Gate B — 多源 DOI→BibTeX 转换 |
| `paper-lookup` | Stage 2 — 10 数据库论文搜索 |
| `arxiv-search` | Stage 2 — arXiv 实时搜索 |
| `scientific-visualization` | Stage 6 — 专业图表生成 |
| `scientific-writing` | Stage 5 — 领域特定语言指导 |
| `infographics` | Stage 6 — 出版物级信息图生成 |
| `markdown-mermaid-writing` | Stage 2/4 — Mermaid 图表生成 |
| `nature-polishing` | Stage 5 — Nature 风格片段 + 短语库 |
| `nature-writing` | Stage 5 — 四轴路由 + stance/ethics |
| `nature-reviewer` | Stage 7 — 3 审稿人 + 综合报告 |
| `latex-document` | Stage 9 — LaTeX 编译 |

---

## 流水线状态持久化

每次阶段完成后自动写入 `sci_writer_state.md`，流水线可跨会话、跨天数运行。使用 `/sciw resume` 从断点继续。

状态文件记录：流水线位置、Gate 结果、Stage 7 评分历史、语料库状态、图表状态、v5.2 新增的术语分类账/PRISMA 流程图/确认闸门状态。

---

## 引用

```bibtex
@software{SCI-writer2026,
  author = {Zhang, Yuanjie and Wang, Kan},
  title  = {SCI-writer: Full-Chain Scientific Review Paper Orchestration System},
  year   = {2026},
  url    = {https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill}
}
```

---

*SCI-writer v5.2.0 — 为想写论文而非管工具的研究者设计。*
*v5.2: Nature-Skills 吸收 · 确认闸门 · 术语分类账 · 故障模式层级 · AI 伦理红绿灯 · 审稿红线*
*v5.1: 生态系统吸收 · Mermaid PRISMA · 图形摘要强制 · 引用链 · 多源验证 · 领域语言检查*
*v5.0: 迭代写作循环 · 叙事引擎 · 论证模板 · 多尺度质量 · 模型适配层*
*SJTU Wang Lab | 张元杰 + 王侃 | Updated: 2026-06-23*
