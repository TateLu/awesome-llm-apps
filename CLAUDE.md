# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

这是一个 **Awesome LLM Apps** 精选集合，展示 RAG、AI Agents、Multi-agent Teams、MCP、Voice Agents 等技术的实际应用。既作为学习资源，也是构建 LLM 应用的生产级模式库。

## 架构

### 目录结构

```
awesome-llm-apps/
├── starter_ai_agents/              # 入门级 AI Agent 教程
├── advanced_ai_agents/             # 复杂 Agent 实现
│   ├── single_agent_apps/          # 单智能体系统
│   ├── multi_agent_apps/           # 多智能体协调模式
│   │   └── agent_teams/            # 协作型 Agent 团队
│   └── autonomous_game_playing_agent_apps/  # 游戏 AI Agent
├── rag_tutorials/                  # 检索增强生成 (RAG) 教程
├── voice_ai_agents/                # 语音 Agent
├── mcp_ai_agents/                  # Model Context Protocol Agent
├── advanced_llm_apps/              # 高级 LLM 应用
│   ├── llm_apps_with_memory_tutorials/  # 持久化内存模式
│   ├── chat_with_X_tutorials/      # 与各类数据源对话
│   ├── llm_optimization_tools/     # Token/上下文优化
│   └── llm_finetuning_tutorials/   # 模型微调示例
├── ai_agent_framework_crash_course/  # 框架速成课程
│   ├── openai_sdk_crash_course/    # OpenAI Agents SDK (11 个教程)
│   └── google_adk_crash_course/    # Google ADK 框架
└── awesome_agent_skills/           # 可复用的 Agent 技能模块
```

### 核心 Agent 框架

本项目演示了多种 Agent 框架：

1. **Agno (`agno` 包)** - 轻量级 Agent 框架，用于入门项目
2. **OpenAI Agents SDK** - 生产级框架，支持结构化输出、工具调用、Agent 交接
3. **Google ADK (Agent Development Kit)** - Google 的 Gemini Agent 开发框架

### Agent 模式

#### 单智能体模式
入门项目通常采用此模式：
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    name="AgentName",
    role="角色描述",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[...],
    tools=[...]
)
```

#### 多智能体团队模式
高级项目使用协调的多智能体团队：
- **顺序流水线 (Sequential Pipeline)**: Agent 按顺序执行，输出传递给下一阶段
- **并行执行 (Parallel Execution)**: 多个 Agent 同时处理不同方面
- **Agent 委派 (Agent Delegation)**: 高级 Agent 将任务委派给专业 Agent
- **Agent 交接 (Agent Handoffs)**: 根据任务需求智能路由到不同 Agent

#### 常见多智能体架构

**研究-规划模式** (如 AI Travel Agent):
- `Researcher` Agent: 通过网络搜索收集信息
- `Planner` Agent: 将研究结果综合为可执行的输出

**流水线模式** (如 Sales Intelligence Agent Team):
- 7+ 阶段顺序执行
- 每个阶段有特定的模型、工具和输出约定
- 通过 `output_key` 机制在阶段间传递状态

### RAG (检索增强生成) 架构

RAG 项目通常使用：
- **LangChain** 处理文档和链编排
- **ChromaDB** 等向量数据库存储嵌入
- **嵌入模型** (Gemini embedding-001, OpenAI embeddings 等)
- **文档加载器**: PyPDFLoader, Web loaders 等
- **文本分割器**: SentenceTransformersTokenTextSplitter

**RAG 变体示例**:
- Basic RAG Chain - 基础 RAG 链
- Agentic RAG - Agent 决定检索策略
- Corrective RAG (CRAG) - 验证检索信息
- Hybrid Search RAG - 语义搜索 + 关键词搜索
- Autonomous RAG - 自纠错检索
- Knowledge Graph RAG with citations - 带引用的知识图谱 RAG

## 开发工作流

### 运行单个项目

每个项目都是独立的：

```bash
# 进入具体项目目录
cd starter_ai_agents/ai_travel_agent/

# 安装依赖
pip install -r requirements.txt

# 运行 Streamlit 应用
streamlit run travel_agent.py
```

### 环境配置

大多数项目需要 API 密钥。典型配置：

```bash
# 在项目目录创建 .env 文件
echo "OPENAI_API_KEY=your_key_here" > .env
echo "GOOGLE_API_KEY=your_key_here" >> .env
echo "SERPAPI_KEY=your_key_here" >> .env
```

Google ADK 项目：
```bash
export GOOGLE_API_KEY=your_key
adk web  # 启动 Web UI (localhost:8000)
```

### 依赖管理

- 需要 Python 3.8+ (语音功能需 3.9+)
- 建议每个项目使用独立虚拟环境避免冲突
- 常用核心依赖: `streamlit`, `agno>=2.2.10`, `openai`, `langchain-*`

## 关键技术分类

### AI/ML 框架
- **agno** - 轻量级 Agent 框架
- **openai** - OpenAI API 客户端
- **langchain-*** - LangChain RAG 生态
- **google-adk** - Google Agent 开发框架

### Web/UI
- **streamlit** - 所有应用的主要 Web 框架
- **icalendar** - 旅行应用的日历生成

### 数据/存储
- **chromadb** - RAG 向量数据库
- **sentence-transformers** - 本地嵌入模型
- **PyPDF2** - PDF 处理

### 工具/集成
- **google-search-results** - SerpAPI 网络搜索
- **browser-use** - 浏览器自动化
- **playwright** - 网页抓取自动化

## 支持的模型提供商

项目支持多种 LLM 提供商：
- **OpenAI**: GPT-4o, GPT-4o-mini, o1 (复杂推理)
- **Google**: Gemini 1.5/2.0/3 (flash/pro 版本)
- **Anthropic**: Claude 系列模型
- **xAI**: Grok 模型
- **本地模型**: Ollama 运行 Llama、Qwen、DeepSeek

## 重��架构决策

### 状态管理
- **Streamlit session_state** - UI 状态持久化
- **SQLite sessions** - OpenAI SDK 对话记忆
- **Agent memory** - 框架内置记忆系统

### 工具设计
- 自定义工具定义为 Python 函数，带清晰文档字符串
- 工具接收结构化输入，返回结构化输出
- 框架自动处理工具调用

### 输出生成
- **结构化输出**: 使用 Pydantic 模型确保类型安全
- **Artifacts**: Agent 生成的文件 (HTML, PNG, ICS 等)
- **Streaming**: 支持实时响应流

### 代码组织模式
- **单文件应用**: 简单教程常用 (UI + Agent 在一起)
- **多文件模块**: 复杂多智能体系统使用
  - `agent.py` - Agent 定义
  - `tools.py` - 自定义工具
  - `__init__.py` - 导出 root_agent
  - `outputs/` - 生成的 artifacts

## 常见代码模式

### Agent 定义模式
```python
from textwrap import dedent
from agno.agent import Agent

agent = Agent(
    name="AgentName",
    role="角色描述",
    description=dedent("""\
        详细的系统提示词
    """),
    instructions=[
        "具体指令 1",
        "具体指令 2"
    ],
    tools=[...],
    add_datetime_to_context=True
)
```

### 顺序 Agent 模式 (多阶段流水线)
```python
# 通过 output_key 在阶段间传递状态
stage1 = Agent(..., output_key="research_data")
stage2 = Agent(..., output_key="analysis")
pipeline = SequentialAgent(agents=[stage1, stage2])
```

### Streamlit 应用模式
```python
import streamlit as st

st.title("应用标题")
api_key = st.text_input("API Key", type="password")
user_input = st.text_input("提示词")

if st.button("提交"):
    with st.spinner("处理中..."):
        response = agent.run(user_input)
    st.write(response.content)
```

## 添加新项目指南

1. **放入合适目录** - 根据复杂度和类型选择
2. **遵循命名规范**: `ai_[领域]_agent` 或描述性名称
3. **包含 README.md**:
   - 功能概述
   - 安装/运行说明
   - API 密钥要求
   - 使用示例
4. **包含 requirements.txt** - 列出所有依赖
5. **文档化 Agent 架构** - 如果是多智能体系统
6. **说明模型选择** 及原因

## 框架特定说明

### OpenAI SDK 项目
- 使用 `openai-agents-python` 包
- 支持: function tools, handoffs, sessions, voice, tracing
- 进阶: 11 个教程从基础到高级

### Google ADK 项目
- 使用 `adk` CLI 工具
- 命令: `adk web` 启动开发服务器
- 擅长: SequentialAgent, google_search, artifacts

### Agno 框架
- 轻量级替代方案，适合简单项目
- 适合学习和原型开发
- 功能不如 OpenAI SDK 或 Google ADK 丰富