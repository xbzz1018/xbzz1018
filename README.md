<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/banner-compact-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/banner-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner.svg">
  <img src="assets/banner.svg" alt="kukuP / xbzz1018 · 大模型应用与后端开发" width="100%">
</picture>

用 Python、FastAPI 和 TypeScript 开发大模型应用与后端服务，关注 **Agent 工具调用、RAG 与任务编排**。

[精选项目](#精选项目) · [开源贡献](#开源贡献) · [English](README.en.md)

## 精选项目

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/agent-quality-gate">Agent Quality Harness</a></h3>
      <p>比较 Agent 版本的质量、延迟与成本，追踪调用并回放失败任务。</p>
      <p><sub>Python · FastAPI · PostgreSQL</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/agrigraph">AgriGraph</a></h3>
      <p>结合图像症状与知识图谱检索农作物病虫害资料，回答附带来源引用。</p>
      <p><sub>Python · LangGraph · Neo4j · Elasticsearch</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/workpilot">WorkPilot</a></h3>
      <p>将工作记录整理为带来源引用的周报与述职草稿，审阅后导出。</p>
      <p><sub>Python · FastAPI · LangGraph</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/SignalForge">SignalForge</a></h3>
      <p>对话查询 A 股与 ETF，回测均线策略，生成研究报告与交互看板。</p>
      <p><sub>TypeScript · Next.js · FastAPI · TimescaleDB</sub></p>
    </td>
  </tr>
</table>

更多：[面试练习室](https://github.com/xbzz1018/interview-room) · [LearningLoop](https://github.com/xbzz1018/learningloop) · [全部公开项目](https://github.com/xbzz1018?tab=repositories&amp;type=source)

## 开源贡献

| 项目 | 参与内容 |
| --- | --- |
| [DeerFlow](https://github.com/bytedance/deer-flow) | 模型调用参数适配与工具产物处理。<br>[#6898](https://github.com/bytedance/deer-flow/pull/6898) 保留 Codex `tool_choice` · [#6574](https://github.com/bytedance/deer-flow/pull/6574) 保留完整产物 URL（已合并） |
| [Cindy](https://github.com/makecindy/cindy) | 为超出首屏的命令匹配结果增加「显示更多」。<br>[#4866](https://github.com/makecindy/cindy/pull/4866)（待合并） |

[完整贡献记录](docs/open-source.md) · [查看公开 PR](https://github.com/search?q=author%3Axbzz1018+is%3Apr+is%3Apublic+-user%3Axbzz1018&amp;type=pullrequests)
