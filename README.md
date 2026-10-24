# Hi, I'm kuku

后端与大模型应用开发，一起学习共同努力，每个人都有一个美好的未来。

## 开源贡献 · DeerFlow

截至 **2026-10-19**，在 [DeerFlow](https://github.com/bytedance/deer-flow) 有 **12 个 PR 已合并**。主要围绕模型适配与消息完整性、工具结果与文件引用链路贡献。

| 方向 | 已合并案例 |
| --- | --- |
| 模型适配与消息完整性 | [Codex 工具选择策略 #6898](https://github.com/bytedance/deer-flow/pull/6898) · [MiniMax reasoning_content #6071](https://github.com/bytedance/deer-flow/pull/6071) · [Claude thinking budget #6060](https://github.com/bytedance/deer-flow/pull/6060) |
| 工具结果与文件引用 | [保留完整的远程 Artifact URL #6574](https://github.com/bytedance/deer-flow/pull/6574) |

[查看全部已合并 PR](https://github.com/bytedance/deer-flow/pulls?q=is%3Apr+author%3Axbzz1018+is%3Amerged)

## 主要项目

主要项目是金融研究工作台 SignalForge 和农业知识图谱问答系统 AgriGraph，工程上侧重工具调用、证据引用、任务执行与结果校验。

| 项目 | 解决的问题 | 工程重点 |
| --- | --- | --- |
| [SignalForge](https://github.com/xbzz1018/SignalForge) | 用自然语言开展 A 股、指数与 ETF 研究，完成数据分析、策略回测和研究看板生成 | Agent 工具调用、市场数据服务、任务调度与恢复、沙箱构建、交付验收 |
| [AgriGraph · 农业知识图谱问答](https://github.com/xbzz1018/agrigraph) | 结合番茄、水稻病虫害文本与图片症状检索知识，生成带证据引用的回答 | LangGraph、Elasticsearch / BM25、可选重排、Neo4j、SSE 与引用核验 |

## 其他项目

| 项目 | 用途与工程重点 |
| --- | --- |
| [WorkPilot](https://github.com/xbzz1018/workpilot) | 将工作记录整理为报告草稿，保留 Fact / Evidence 引用，通过人工批准控制最终导出 |
| [LearningLoop](https://github.com/xbzz1018/learningloop) | 围绕学习计划、日常任务与 FSRS 复习，实践类型化工具、状态恢复和模型用量记录 |
| [Agent Quality Harness](https://github.com/xbzz1018/agent-quality-gate) | 为 Agent 版本对比提供冻结评测集、Trace、失败回放和 SHIP / WARN / BLOCK 发布门禁 |

各项目 README 说明运行方式、验证记录与当前限制。

## 技术

Python · TypeScript · FastAPI · LangGraph · Next.js / React · Vue · PostgreSQL · Redis · Docker · pytest · GitHub Actions
