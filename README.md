# Hi, I'm kuku

后端与大模型应用开发，关注模型接入、工具调用、检索与评测。

项目侧重证据引用、运行记录和失败恢复；开源贡献从复现问题开始，通过小范围修复和回归测试验证结果。

## 开源贡献 · DeerFlow

截至 **2026-10-19**，在 [DeerFlow](https://github.com/bytedance/deer-flow) 有 **12 个 PR 已合并**。主要围绕模型适配与消息完整性、工具结果与文件引用链路贡献。

| 方向 | 已合并案例 |
| --- | --- |
| 模型适配与消息完整性 | [Codex 工具选择策略 #6898](https://github.com/bytedance/deer-flow/pull/6898) · [MiniMax reasoning_content #6071](https://github.com/bytedance/deer-flow/pull/6071) · [Claude thinking budget #6060](https://github.com/bytedance/deer-flow/pull/6060) |
| 工具结果与文件引用 | [保留完整的远程 Artifact URL #6574](https://github.com/bytedance/deer-flow/pull/6574) |

[查看全部已合并 PR](https://github.com/bytedance/deer-flow/pulls?q=is%3Apr+author%3Axbzz1018+is%3Amerged)

## 代表项目

| 项目 | 解决的问题 | 工程重点 |
| --- | --- | --- |
| [Agent Quality Harness](https://github.com/xbzz1018/agent-quality-gate) | 对比 Agent 版本，追踪失败并给出发布门禁结果 | 冻结评测集、Trace、失败回放、SHIP / WARN / BLOCK |
| [AgriGraph](https://github.com/xbzz1018/agrigraph) | 结合农业文本、图片症状与图谱，生成带证据引用的回答 | BM25 / 可选重排、Neo4j、SSE、引用核验 |
| [WorkPilot](https://github.com/xbzz1018/workpilot) | 将工作记录整理为可审阅、可追溯的报告草稿 | Fact / Evidence 校验、人工批准、断点恢复 |
| [LearningLoop](https://github.com/xbzz1018/learningloop) | 将学习目标转为计划、日常任务和复习安排 | 类型化工具、FSRS、状态恢复、模型用量记录 |

各项目 README 说明运行方式、验证记录与当前限制。

其他项目：[SignalForge](https://github.com/xbzz1018/SignalForge) · A 股与 ETF 研究工作区，包含市场数据、回测及生成看板校验。

## 技术

Python · TypeScript · FastAPI · LangGraph · Vue · PostgreSQL · Docker · pytest · GitHub Actions
