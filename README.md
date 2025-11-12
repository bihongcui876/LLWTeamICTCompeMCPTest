# L-L-M 团队协作项目

[![最新文档](https://img.shields.io/badge/说明文件-README%20202511-red)](./README.md)
[![2025年10月版本说明文档](https://img.shields.io/badge/说明文件-README%20202510-blue)](./README_202510末.md)
[![源](https://img.shields.io/badge/源文件-source-green)](./src)
[![提示词](https://img.shields.io/badge/提示词-prompt-black)](./src/prompt)
[![xxAPI](https://img.shields.io/badge/小小API-xxAPI-black)](./src/xxAPIServer)
[![CPubMedAPI](https://img.shields.io/badge/PubMed-CPubMedAPI-black)](./src/CPubMedAPIServer)
[![配置文档](https://img.shields.io/badge/配置文档-models%20jsons-black)](./NexentModelsJsons)
[![配置文档](https://img.shields.io/badge/前端访问与端口-portss%20jsons-yellow)](./端口分法与网站地址.md)

---
## 零、主要操作信息

+ 应用Nexent平台（可能和ModelEngine平台）结合部分数据和API设计AI AGENT，以达成医学与病理问答和辅助诊断功能。
+ 本项目包含大量测试用文件。
+ 程序执行主要语言为Python。
+ 可采用其他方法进行调试或处理数据效果。

本帖笔主 bihongcui876/@wubolieng80594

---

## 壹、项目设计思想：病理问答分析

### 项目主体任务
1. 病理知识问答的作用对象：医生与医学知识较为专业或专业学习者。
2. 病理问答的作用功能方面：辅助医生了解病症病理原因、结合医生诊断进行病症病理辅助解析（可能会出错但需要方便地协助医生处理80%以上的问题）
3. 所谓智能问答：中枢问答体--功能AGENT--信息知识库--联网搜索域--图文解析生成图文
4. 预计使用模型：语言模型（GLM-4.5系列开放大模型（以Air为主的测试模型）/Qwen系列经微调模型）,向量模型（embedding models）（bge-m3），视觉模型（Qwen或GLM或GGLM系列模型），语言合成播报与语言识别（TTS&STT）（讯飞或火山）（较难）
5. 项目处理口径：
- 以国标文件为标向之众多（RAG与否的）知识库
- 以功能为导向之Nexent设计模式的AGENT
- 以API数据集获取为导向之SSE方法的MCP服务器工具集
- 以医学类知识为导向之基础模型微调训练

### 基础问答能力（新）
1. 用户问询病症信息时
- 依据API返回信息整理知识
- 合适时调用部分知识库
- 结合自身知识回答

2. 此外，对病理问答的追问追答设计为：
- 病理持续分析
- 表征里征对应病理修订（比如系统性红斑狼疮怀疑，但是追问说明喉部表征为白色粒泡，诊断为水痘症；或里征为非典型里征，但仍然判定为该病症之类）

3. 模糊性问答的功能设计为：
- 模糊性猜测型引导式回答（避免导致致命错误）
- 模糊性表层式基础性回答（基于数据作出分析）

4. 病症中有关和检查报告单、诊断方的辅助审核或辅助诊断
- 依据现有数据作普遍性
- 依据开方信息作辅助信息检测
- 依据病历对开方合理性分析

### “病理描述”说明（旧版沿用）（*福建医科大学* 24级临床医学系 *范书颜*——证明此AI总结内容有效）
1. 病因：明确疾病的“源头”，即疾病由什么引起，如细菌感染、基因突变、长期吸烟、外伤等。
2. 发病机制：解释病因如何“一步步导致疾病”，是疾病发生、发展的核心过程，比如病毒如何入侵细胞、免疫系统如何异常攻击自身组织。
3. 病理变化：描述疾病导致的“身体结构改变”，包括组织细胞的形态、结构、功能异常，是病理诊断的核心依据（如肿瘤细胞的异型性）。
4. 病理结局：说明疾病的“最终走向”，即可能的转归，如治愈、迁延不愈、并发症（如肺炎可能发展为肺脓肿）或后遗症（如中风后的肢体偏瘫）。
- 此外，有必要对其中各个部分的问答进行提示词说明功能分割。

### 投入运用的搜索API
- CPubMedAPI 基于C-Pub-Med的论文信息合集知识图谱，可以供给AI合理的

本团队在2025年10月25日暂时决定使用CPubMed知识图谱API集成有关MCP。
本团队在2025年11月11日确定成功应用和使用xxAPI（免费开源且项目属于测试，可合法使用）。


### 初步模型结构设计

```结构设计
问答中枢：语言大模型AGENT----提示词控制功能
  |
  +--- 精准搜索知识库与图谱（RAG等方式）
  |
  +--- MCP服务器工具库
  |      |
  |      +--- 联网搜索
  |      |
  |      +--- API查找
  |
  +--- 模型问答数据库训练
```
---
## 貳、环境测试

### 部分前置需求

* uv（不一定）
* Python（必须）


### Inspector安装与运行
1. 安装Inspector
```bash
npx @modelcontextprotocal/inspector
```

2. 安装依赖（对于uv项目）

```bash
uv init "mcp[cli]"
```

3. 如果下载时候需要传递参数，则需要通过以下下载

```bash
# 传递参数 arg1 arg2
npx @modelcontextprotocol/inspector build/index.js arg1 arg2

# 传递环境变量 KEY=value  KEY2=$VALUE2
npx @modelcontextprotocol/inspector -e KEY=value -e KEY2=$VALUE2 node build/index.js

# 同时传递环境变量和参数
npx @modelcontextprotocol/inspector -e KEY=value -e KEY2=$VALUE2 node build/index.js arg1 arg2

# Use -- to separate inspector flags from serverDemo arguments
npx @modelcontextprotocol/inspector -e KEY=$VALUE -- node build/index.js -e serverDemo-flag
```

4. 调试

```bash
npx @modelcontextprotocol/inspector uvx mcp-serverDemo-fetch
```

5. 注意：Nexent只支持SSE方式，并且（tmd）示例为本机端口地址，但实际只能连接从公网或域名的端口。

### 模拟性测试

本人认为，相比Nexent，Cherry Studio的特色更加友好，但部分功能也具有局限性。

### Nexent本地化部署
请通过 https://github.com/ModelEngine-Group/nexent 网址对Nexent的GitHub仓库进行研究（当然恕我直言，好多地方烂的不行）

一般建议通过docker进行部署

---
## 本地MCP Server源代码文件（挂后台一直用就行，可能不需要uv）

### xxAPIServer与其工具

见文件夹[![xxAPI](https://img.shields.io/badge/小小API-xxAPI-black)](./src/xxAPIServer)

即见文件夹src/xxAPIServer

1. 推荐运行本帖笔主已经调试完毕的xxAPIServer.py，可以在本机配置完毕有关库后启动。
2. 注意：请一定要改动主代码中uvicorn（本人放在代码后段）中的端口信息以适配运行端（host和post）！
```python
if __name__ == "__main__":
    uvicorn(......);
```

3. 有关库列表：

## 需要的外包服务端口

- 目前使用（2025年11月12日配）
  - 本文档之中，localhost:9090对应的网址是：（http或https）
https://58859ed.r38.cpolar.top
  - 因端口侵占问题，已然调整端口到localhost:3090，对应的网址是：
https://22757832.r38.cpolar.top

- 使用（2025年11月8日配）
  - 本文档之中，localhost:9090对应的网址是：（http或https）
https://2081f93c.r38.cpolar.top
  - 因端口侵占问题，已然调整端口到localhost:3090，对应的网址是：
https://3b58623f.r38.cpolar.top

- 使用（2025年11月7日配）
  - 本文档之中，localhost:9090对应的网址是：（http或https）
https://2081f93c.r38.cpolar.top
  - localhost:3000对应的网址是：
https://22d22915.r38.cpolar.top

---
## 知识库

知识库系在此文件之外另一个文档中存储。

其中参考的网页属于以下域名：

| 网址                          | 署    |
|-----------------------------|------|
| https://www.nhc.gov.cn/wjw/ | 卫健委  |
| ---                         | ---  |
| https://www.yixue.com/      | 医学百科 |
| ---                         | ---  |

此外这些知识库导入Nexent，使用开放大模型（智谱GLM）中的嵌入模型辅助做检索知识库（Embedding-3），以便实现有关功能。
（报销发票有关价格：人民币柒圓伍角，效果为：5000,0000 token，有效期2025年11月12日开始到2025年2月12日）

---
## 项目其他计划

使用类似思想真正服务人民，做到一个真正有效的项目闭环。

---
合作：(暂时不写)
