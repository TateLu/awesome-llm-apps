# Web Scraping AI Agent - DeepSeek 版本

使用 DeepSeek API 的智能网页抓取工具，支持自然语言描述提取需求。

## 特性

- 🕷️ **智能抓取**: 使用 AI 理解网页结构，提取所需信息
- 💰 **超高性价比**: DeepSeek API 价格仅为 GPT-4 的 1/30
- 🎯 **自然语言提示**: 用中文描述你想要什么，AI 自动提取
- 📊 **结构化输出**: 自动返回 JSON 格式的结构化数据

## 依赖安装

```bash
pip install streamlit scrapegraphai playwright langchain-openai
```

## 配置

### 1. 获取 DeepSeek API Key

访问 [DeepSeek Platform](https://platform.deepseek.com/) 注册并获取 API Key

### 2. 设置环境变量

```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

## 使用方法

### 基本用法

```bash
python3 deepseek_agent.py --url "URL" --prompt "提取提示词"
```

### 参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| `--url` | ✅ | 要抓取的网站 URL |
| `--prompt` | ✅ | 用自然语言描述要提取的信息 |
| `--model` | ❌ | 模型选择 (deepseek-chat/deepseek-coder，默认: deepseek-chat) |
| `--api-key` | ❌ | API Key (也可通过环境变量设置) |
| `--temperature` | ❌ | LLM 温度参数 0.0-1.0 (默认: 0.0) |
| `--tokens` | ❌ | 上下文窗口大小 (默认: 2000) |
| `--output`, `-o` | ❌ | 将结果保存到 JSON 文件 |

## 爬取示例

### 示例 1: 抓取 Hacker News

```bash
python3 deepseek_agent.py \
  --url "https://news.ycombinator.com" \
  --prompt "提取新闻标题和链接"
```

**输出示例:**
```json
{
  "content": "1. 标题: WebAssembly (WASM)\n2. 标题: AI agents for codebases\n..."
}
```

### 示例 2: 抓取百度热搜

```bash
python3 deepseek_agent.py \
  --url "https://top.baidu.com/board?platform=pc&sa=pcindex_entry" \
  --prompt "提取热搜榜单，包括排名、标题、热度"
```

**输出示例:**
```json
{
  "content": "**新闻热搜榜**\n1. 排名: 1, 标题: 习近平强调充分发挥这一特有优势\n..."
}
```

### 示例 3: 抓取并保存到文件

```bash
python3 deepseek_agent.py \
  --url "https://news.ycombinator.com" \
  --prompt "提取新闻标题和链接" \
  --output result.json
```

### 示例 4: 使用 deepseek-coder 模型

```bash
python3 deepseek_agent.py \
  --url "https://github.com/trending" \
  --prompt "提取项目名称、描述和编程语言" \
  --model deepseek-coder
```

## 执行流程

```
┌─────────────────────────────────────────────────────────────┐
│                    deepseek_agent.py                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣  参数解析                                              │
│     ├─ 读取命令行参数 (--url, --prompt, etc.)              │
│     └─ 检查 API Key                                         │
│                                                             │
│  2️⃣  初始化 LLM                                            │
│     ├─ 创建 ChatOpenAI 实例                                 │
│     ├─ 设置 base_url: https://api.deepseek.com             │
│     └─ 配置模型: deepseek-chat                              │
│                                                             │
│  3️⃣  配置 ScrapeGraphAI                                    │
│     ├─ 设置 model_instance                                  │
│     ├─ 设置 model_tokens: 2000                              │
│     └─ 启用 verbose: True                                   │
│                                                             │
│  4️⃣  创建 SmartScraper                                     │
│     ├─ 传入 prompt (用户提示词)                             │
│     └─ 传入 source (目标 URL)                               │
│                                                             │
│  5️⃣  执行抓取 ─────────────────────────────────────┐       │
│     │                                                   │       │
│     ├─ Fetch Node      → 获取网页 HTML                │       │
│     ├─ ParseNode Node  → 解析 HTML 提取文本           │       │
│     └─ GenerateAnswer  → LLM 生成结构化数据           │       │
│                          │                               │       │
│                          └─ DeepSeek API 调用          │       │
│                                                             │
│  6️⃣  返回结果                                              │
│     ├─ 打印 JSON 格式结果                                   │
│     └─ 可选: 保存到文件 (--output)                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 详细执行过程

```bash
$ python3 deepseek_agent.py --url "https://news.ycombinator.com" --prompt "提取新闻标题"

======================================================================
🕷️  Web Scraping AI Agent - DeepSeek
======================================================================
📍 目标 URL: https://news.ycombinator.com
💬 提取提示: 提取新闻标题
🤖 使用模型: deepseek-chat
🌡️  Temperature: 0.0
----------------------------------------------------------------------
🔧 正在初始化 DeepSeek LLM...
✅ LLM 初始化完成
🔧 正在配置 ScrapeGraphAI...
✅ 配置完成
🕷️  正在创建 SmartScraper...
✅ 抓取器创建完成
----------------------------------------------------------------------
🚀 开始抓取数据...
----------------------------------------------------------------------
--- Executing Fetch Node ---
--- (Fetching HTML from: https://news.ycombinator.com/) ---
--- Executing ParseNode Node ---
--- Executing GenerateAnswer Node ---
Processing chunks: 100%|██████████| 5/5 [00:00<00:00, 114.27it/s]
----------------------------------------------------------------------
✅ 抓取完成！
======================================================================
📊 抓取结果:
======================================================================
{...JSON 结果...}
======================================================================
```

## DeepSeek API 优势

| 特性 | DeepSeek-V3 | GPT-4o | Claude 3.5 Sonnet |
|------|-------------|--------|-------------------|
| 输入价格 | ¥1/百万 tokens | ~¥36/百万 tokens | ~¥24/百万 tokens |
| 输出价格 | ¥2/百万 tokens | ~¥72/百万 tokens | ~¥96/百万 tokens |
| 上下文窗口 | 128K | 128K | 200K |

**价格对比**: DeepSeek 仅为 GPT-4o 的 **1/30**！

## 常用提示词示例

| 网站类型 | 提示���示例 |
|----------|-----------|
| 新闻网站 | "提取所有新闻标题、作者和发布时间" |
| 电商网站 | "提取产品名称、价格和评分" |
| 博客 | "提取文章标题、摘要和标签" |
| 论坛 | "提取帖子标题、作者和回复数" |
| GitHub | "提取项目名称、描述、Stars 数和编程语言" |

## 注意事项

1. **反爬虫保护**: 某些网站有反爬虫机制，可能需要使用代理或特殊处理
2. **JavaScript 渲染**: 动态内容可能需要使用 Playwright 等工具先渲染
3. **API 余额**: 确保 DeepSeek 账户有足够余额
4. **网络访问**: 确保能访问目标 URL

## 故障排查

### 错误: API Key 未设置
```bash
export DEEPSEEK_API_KEY="your-key"
```

### 错误: 余额不足
访问 DeepSeek 控制台充值

### 错误: 无法访问 URL
- 检查网络连接
- 尝试使用代理
- 确认 URL 可访问

### 结果为空或不准确
- 调整提示词，更具体地描述需求
- 增加 `--tokens` 参数
- 尝试降低 `--temperature`

## 相关文件

- `deepseek_agent.py` - 命令行版本（本文档）
- `ai_scrapper_deepseek.py` - 支持 Web 界面 + 命令行双模式
- `run_scraper.py` - 简化版命令行脚本

## 许可证

本项目遵循 awesome-llm-apps 仓库的许可证。
