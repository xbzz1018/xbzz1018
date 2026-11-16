<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/banner-compact-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/banner-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner.svg">
  <img src="assets/banner.svg" alt="kukuP / xbzz1018 · 大模型应用与后端开发" width="100%">
</picture>

大模型应用与后端开发，关注 **Agent 工具调用、RAG 与任务编排**。

[项目](#项目) · [开源贡献](#开源贡献) · [English](README.en.md)

## 项目

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/agent-quality-gate">Agent Quality Harness</a></h3>
      <p>对比 Agent 版本的质量、延迟与成本，提供调用追踪、失败回放和发布门禁。</p>
      <p><sub>Python · FastAPI · Vue · PostgreSQL</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/SignalForge">SignalForge</a></h3>
      <p>对话查询 A 股与 ETF，回测均线策略，生成研究报告与交互看板。</p>
      <p><sub>TypeScript · Next.js · FastAPI · TimescaleDB</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/agrigraph">AgriGraph</a></h3>
      <p>结合图像症状与知识图谱检索番茄、水稻病虫害资料，生成带引用的回答。</p>
      <p><sub>Python · LangGraph · Elasticsearch · Neo4j</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/workpilot">WorkPilot</a></h3>
      <p>将工作记录整理为带来源引用的周报与述职草稿，审阅后导出。</p>
      <p><sub>Python · FastAPI · LangGraph · SQLite</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/interview-room">面试练习室</a></h3>
      <p>围绕简历与 JD 模拟面试，逐题复盘并重答练习。</p>
      <p><sub>TypeScript · React · Electron · SQLite</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/xbzz1018/learningloop">LearningLoop</a></h3>
      <p>把学习目标拆成每日任务，结合 FSRS 复习、练习反馈与定时提醒。</p>
      <p><sub>Python · FastAPI · FSRS · SQLite</sub></p>
    </td>
  </tr>
</table>

[浏览公开仓库](https://github.com/xbzz1018?tab=repositories&amp;type=source)

## 开源贡献

参与 DeerFlow 的模型适配与工具交付，以及 Cindy 的桌面交互改进。

| 项目 / PR | 修改内容 |
| --- | --- |
| [DeerFlow #6898](https://github.com/bytedance/deer-flow/pull/6898)<br><sub>已合并</sub> | 保留 Codex 的 `tool_choice` 参数 |
| [DeerFlow #6574](https://github.com/bytedance/deer-flow/pull/6574)<br><sub>已合并</sub> | 保留远程生成产物的完整 URL |
| [Cindy #4866](https://github.com/makecindy/cindy/pull/4866)<br><sub>待合并</sub> | 为超出首屏的命令匹配结果增加「显示更多」 |

[完整贡献记录](docs/open-source.md) · [查看公开 PR](https://github.com/search?q=author%3Axbzz1018+is%3Apr+is%3Apublic+-user%3Axbzz1018&amp;type=pullrequests)
