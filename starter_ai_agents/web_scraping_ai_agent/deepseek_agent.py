#!/usr/bin/env python3
"""
使用 DeepSeek API 的 Web Scraping AI Agent (命令行版本)
DeepSeek API 价格更便宜，性能优秀
"""

import os
import sys
import json
import argparse
from scrapegraphai.graphs import SmartScraperGraph
from langchain_openai import ChatOpenAI


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='Web Scraping AI Agent - 使用 DeepSeek API 智能抓取网页数据',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 抓取 Hacker News 新闻
  python3 deepseek_agent.py --url "https://news.ycombinator.com" --prompt "提取新闻标题和链接"

  # 抓取百度热搜
  python3 deepseek_agent.py --url "https://top.baidu.com/board?platform=pc&sa=pcindex_entry" --prompt "提取热搜榜单，包括排名、标题、热度"

  # 抓取 Python 官网
  python3 deepseek_agent.py --url "https://python.org" --prompt "提取所有Python版本的发布信息"
        '''
    )
    parser.add_argument('--url', required=True, help='要抓取的网站 URL')
    parser.add_argument('--prompt', required=True, help='用自然语言描述你想要抓取的信息')
    parser.add_argument('--model', default='deepseek-chat', choices=['deepseek-chat', 'deepseek-coder'],
                        help='模型选择 (默认: deepseek-chat)')
    parser.add_argument('--api-key', default=os.getenv('DEEPSEEK_API_KEY', ''),
                        help='DeepSeek API Key (也可通过 DEEPSEEK_API_KEY 环境变量设置)')
    parser.add_argument('--temperature', type=float, default=0.0,
                        help='LLM Temperature，0.0-1.0 (默认: 0.0)')
    parser.add_argument('--tokens', type=int, default=2000,
                        help='模型上下文窗口大小 (默认: 2000)')
    parser.add_argument('--output', '-o', help='将结果保存到指定的 JSON 文件')
    return parser.parse_args()


def check_api_key(api_key):
    """检查 API Key"""
    if not api_key:
        print("❌ 错误: 请设置 DEEPSEEK_API_KEY 环境变量或使用 --api-key 参数")
        print("\n获取 API Key:")
        print("  访问 https://platform.deepseek.com/ 注册并获取")
        print("\n设置方式:")
        print("  export DEEPSEEK_API_KEY='your-key-here'")
        print("  或: --api-key 'your-key-here'")
        sys.exit(1)
    return api_key


def print_header(args):
    """打印执行信息头"""
    print("=" * 70)
    print("🕷️  Web Scraping AI Agent - DeepSeek")
    print("=" * 70)
    print(f"📍 目标 URL: {args.url}")
    print(f"💬 提取提示: {args.prompt}")
    print(f"🤖 使用模型: {args.model}")
    print(f"🌡️  Temperature: {args.temperature}")
    print("-" * 70)


def create_llm(args):
    """创建 LLM 实例"""
    print("🔧 正在初始化 DeepSeek LLM...")
    llm = ChatOpenAI(
        model=args.model,
        api_key=args.api_key,
        base_url="https://api.deepseek.com",
        temperature=args.temperature,
    )
    print("✅ LLM 初始化完成")
    return llm


def create_graph_config(llm, args):
    """创建 ScrapeGraphAI 配置"""
    print("🔧 正在配置 ScrapeGraphAI...")
    config = {
        "llm": {
            "model_instance": llm,
            "model_tokens": args.tokens,
        },
        "verbose": True,
    }
    print("✅ 配置完成")
    return config


def create_scraper(args, config):
    """创建抓取器"""
    print("🕷️  正在创建 SmartScraper...")
    scraper = SmartScraperGraph(
        prompt=args.prompt,
        source=args.url,
        config=config
    )
    print("✅ 抓取器创建完成")
    return scraper


def run_scraper(scraper):
    """执行抓取"""
    print("-" * 70)
    print("🚀 开始抓取数据...")
    print("-" * 70)
    result = scraper.run()
    print("-" * 70)
    print("✅ 抓取完成！")
    return result


def print_result(result):
    """打印结果"""
    print("=" * 70)
    print("📊 抓取结果:")
    print("=" * 70)
    if isinstance(result, dict):
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result)


def save_result(result, output_file):
    """保存结果到文件"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"\n💾 结果已保存到: {output_file}")
    except Exception as e:
        print(f"\n⚠️  保存文件失败: {e}")


def main():
    """主函数"""
    # 解析参数
    args = parse_args()

    # 检查 API Key
    args.api_key = check_api_key(args.api_key)

    # 打印信息头
    print_header(args)

    # 创建 LLM
    llm = create_llm(args)

    # 创建配置
    config = create_graph_config(llm, args)

    # 创建抓取器
    scraper = create_scraper(args, config)

    # 执行抓取
    try:
        result = run_scraper(scraper)
        print_result(result)

        # 保存到文件
        if args.output:
            save_result(result, args.output)

        print("=" * 70)

    except Exception as e:
        print("-" * 70)
        print(f"❌ 抓取失败: {e}")
        print("\n请检查:")
        print("  1. API Key 是否正确")
        print("  2. 余额是否充足 (访问 DeepSeek 控制台查看)")
        print("  3. URL 是否可访问")
        print("  4. 网站是否有反爬虫保护")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
