# LLW Team's Issue (半保密)

---

## 零、主要操作信息

+ 使用Nexent平台、ModelEngine平台结合部分数据和API设计AI AGENT，以达成医学问答功能。
+ 本项目需要存储测试文件。
+ 主要使用Python来微调训练模型或处理获取的数据。
+ 可采用其他方法进行调试或处理数据效果。

本帖作者 @wubolieng80594

---

## 壹、项目设计思想：病理问答分析

### 模型功能设定理解
1. 病理知识问答的作用对象：医生与医学知识较为专业或专业学习者。
2. 病理问答的作用功能方面：辅助医生了解病症病理原因、结合医生诊断进行病症病理辅助解析（可能会出错但需要方便地协助医生处理80%以上的问题）
3. 所谓智能问答：中枢问答体--功能AGENT--信息知识库--联网搜索域--图文解析生成图文
4. 预计使用模型：语言模型（Qwen2.5-7B/14B-Instruct）,向量模型（embedding models）（bge-m3），视觉模型（上交瑞医RuiPath模型），语言合成播报与语言识别（TTS&STT）（讯飞或火山）
5. 问题关键：如何介入、训练、使用模型。

### 基础问答能力：
1. 选取模型介入Nexent平台，配置提示词，实现流畅、准确的病理知识问答。
  基于此，初步预设实现功能（明确性问答）为：
- - 对病症的病理整体描述的回答。
- - 对表征描述的医病猜测。
- - 对药用需求的答复。
- - 对药物药理特征与药物有效症状的整体答复。
- - 对表征、里征描述的合理性适配。
- - 对医疗资源的描述。

2. 此外，对病理问答的追问追答设计为：
- - 病理持续分析
- - 表征里征对应病理修订（比如系统性红斑狼疮怀疑，但是追问说明喉部表征为白色粒泡，诊断为水痘症；或里征为非典型里征，但仍然判定为该病症之类）

3. 模糊性问答的功能设计为：
- - 模糊性病症描述，基于此需要猜测是否有某其他表征，或是否有某其他症状。
- - 模糊性药物运用或特征描述，基于此需要进行纠正和追问核查。
- - 模糊性病理阶段特征描述，基于此需要进行猜测或追问追答。
- - 其余模糊性特征描述。
- - 非医学医理有关问题，需要有联网查询答复功能，但不能多回答，一行的略答。

### “病理描述”说明（*福建医科大学* 24级临床医学系 *范书颜*——证明此AI总结内容有效）
1. 病因：明确疾病的“源头”，即疾病由什么引起，如细菌感染、基因突变、长期吸烟、外伤等。
2. 发病机制：解释病因如何“一步步导致疾病”，是疾病发生、发展的核心过程，比如病毒如何入侵细胞、免疫系统如何异常攻击自身组织。
3. 病理变化：描述疾病导致的“身体结构改变”，包括组织细胞的形态、结构、功能异常，是病理诊断的核心依据（如肿瘤细胞的异型性）。
4. 病理结局：说明疾病的“最终走向”，即可能的转归，如治愈、迁延不愈、并发症（如肺炎可能发展为肺脓肿）或后遗症（如中风后的肢体偏瘫）。
- 此外，有必要对其中各个部分的问答进行提示词说明功能分割。

### 有关知识库与知识图谱（来自Deepseek搜索在线版搜索）
- OMAHA七巧板医学术语
- - 已证明本术语属于无用数据，不可导入数据库 *（OpenKG转OMAHA网站，术语属于案例小样，无法证明为有效信息，有效信息系OMAHA合作伙伴或会员可以获取的，年花费为**貳萬圓**人民币，小项目不推荐使用）*
- OMAHA汇知知识图谱
- - 来自OpenKG.cn，信息特色同*上一条*。
- CPubMed
- - 证明为有效信息，且可以调用搜索API或申请下载，下载凭证不知是否有效，网站系哈尔滨工业大学（深圳校区）开发。
- 医疗数据智能实验室（mdi.hkust-gz.edu.cn）
- 医知源（系综合性网站，使用OMAHA数据源，不可轻易获取）

本团队在2025年10月25日暂时决定使用CPubMed知识图谱API集成有关MCP。


### 初步模型结构设计

```结构设计
问答中枢：语言大模型AGENT----提示词控制功能
  |
  +--- 精准搜索知识库与图谱（RAG等方式）
  |      |
  |      +--- 权威医学文献与发病与药物知识体系（CPubMed，具有8个API，但也可以使用RAG）
  |      |
  |      +--- 其他信息
  |
  +--- MCP服务器工具库
  |      |
  |      +--- 联网搜索（API等方式，如上述CPubMed）
  |      |
  |      +--- 其他外接模型（多AGENT嵌套开始应用的情况）
  |      |
  |      +--- 时间（不论是问答即时时间都需要备用；如果涉及中医，可能需要调用农历库等）
  |
  +--- 模型问答数据库训练
```

---

## 贰、测试文档 MCP server 与 client

---

## 主要Server框架搭建方法

### 一、Python FastMCP

1. 在`Python`使用`FastMCP`构建实例化对象
2. 使用`@mcp.tool()`对定义的函数方法进行修饰

### 二、Node.js 实现


### 三、Java Spring AI 实现

---

## 主要Client测验方法

### 一、LangChain
* 使用LangChain编写客户端

### 二、Cursor
* 使用Cursor客户端配置

### 三、CLine
* 使用VSCODE中CLine配置，例如以下代码
```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```
* 其中使用了绝对路径来调用本端程序、

### 四、MCP Inspector
* 这个纯命令行格式

---
## 部分前置需求

* uv
* Python
* mcp

---
## 运行
1. 安装Inspector
```bash
npx @modelcontextprotocal/inspector
```

2. 安装依赖

```bash
uv init "mcp[cli]"
```

3. 运行程序

```bash
mcp dev TimeServerFastMCP.py
```

4. 如果下载时候需要传递参数，则需要通过以下下载

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

5. 调试

```bash
npx @modelcontextprotocol/inspector uvx mcp-serverDemo-fetch
```

* 在BHC876的电脑上面的访问位置：
* `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=a3f1b308d5d14f9d110f84896fd608ae77fee2b2836e47cc3ac11354916e0f56`

* 其他推荐的直观方便的方法：使用CherryStudio进行MCP调试。

---

## 叁、CPubMed集合数据

api-key(日期2025/10/25) = b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d

（用户/@author：BOHONCUE876）
（API Key 变化条件：更改用户名或密码）

传输HTTP
请求方式GET/POST

字符UTF-8

响应格式JSON

User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1000.0 Safari/537.36

基本URL:http://cpubmed.openi.org.cn/graph/

---
三元组查询

URL:http://cpubmed.openi.org.cn/graph/schema

调用示例：
http://cpubmed.openi.org.cn/graph/schema?entity=库欣病&sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d

1. 实体关联三元组API：
访问字段名：
必填： entity:(text,True) ; sign:(text,True)
返回字段名：
entity_schema:(dict)

示例：
http://cpubmed.openi.org.cn/graph/schema?
      entity=糖尿病
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
    返回结果
    { 
        "糖尿病": { 
        "辅助检查": [[ "生化检验", "2420" ],[ "眼底荧光造影检查", "84106" ],...],
        "病因": [[ "饮食不规律", "44484" ],[ "胰岛功能减退", "81235" ],...],
        "药物治疗": [[ "依帕司他", "696" ], [ "甲钴胺", "697" ],...],
        "并发症": [ [ "尿毒症", "1086" ], [ "冠心病", "1352" ],...],
        ...
        }
    }

---
2. 三元组信息详细搜索

URL:http://cpubmed.openi.org.cn/graph/triple-info

访问参数：ID（见上例，储存的三元组）,sign（API-Key）

返回参数：triple(array),text(text),doc_num(integer),doc_title(array)

示例：
 接口调用
      http://cpubmed.openi.org.cn/graph/triple-info?
      ID=14529
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
      
    返回结果
    {
        "triple_id": "14529",
        "doc_id": "46790947,22917575,...",
        "text": "糖尿病大鼠血管平滑肌细胞内质网应激因子GRP78和caspase12的表达及阿托伐他汀的干预作用",
        "doc_num": 198,
        "doctitle": ["糖尿病大鼠血管平滑肌细...", "阿托伐他汀对2型糖尿病鼠...", ...]
    }   

---
3. 医学类辅助分词

URL:http://cpubmed.openi.org.cn/graph/cut

params: query(text),sign(text)

return keys: cut_result(array)

示例：
接口调用
      
      http://cpubmed.openi.org.cn/graph/cut?
      query=肝癌的发生是多因素作用的结果,其中乙型、丙型肝炎病毒和黄曲霉毒素B1是发生肝癌的主要危险因素.
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
    返回结果
    [
        ["肝癌", "疾病"],
        ["的", "停用词"],
        ["发生", "停用词"],
        ["是", "停用词"],
        ...
    ]

---

4. 三元组匹配：
URL:http://cpubmed.openi.org.cn/graph/match

params: query(text),sign(text)

return keys:match_result(array)

三元组格式：[ID,头实体,关系,尾实体]
（意义；头实体与尾实体有关联，ID是三元组的ID）

---

5. 医学文献检索API

URL:http://cpubmed.openi.org.cn/graph/retrieve

params: query, sign

return keys: docid(text), title(text), keywords(array), abstract(text)

示例：
接口调用
      http://cpubmed.openi.org.cn/graph/retrieve?
      query=肝癌
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
      
    返回结果
    [
        {
            "f_ID": "13262879",
            "f_Title": "晚期肝癌介入置管埋泵化疗的常见并发症及护理对策",
            "f_keyword": "肝癌%介入%置管%化疗泵%护理",
            "f_Abstract": "回顾性分析30例晚期肝癌患者施,娴熟的注射...",
        },
        {
            ,,,
        },
        ...
    ]

---
6. 查找实体之间的三元组路径
URL:http://cpubmed.openi.org.cn/graph/path

params:source-entity,target-entity,sign
（两个实体之间的关系，有概率找不到关系）

return keys: path-result(array)

示例
    接口调用
      http://cpubmed.openi.org.cn/graph/path?
      source-entity=心脏病&target-entity=糖尿病
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
      
    返回结果
    [
        [
            ["心脏病",相关（导致）,心律失常],[心律失常,高危因素,"糖尿病"]
        ],
        [
            ["心脏病",病理分型,主动脉夹层],[主动脉夹层,病因,"糖尿病"]
        ],
        [
            ["心脏病",病因,感染],[感染,高危因素,"糖尿病"]
        ],
        ...
    ]

---
7. 相似度计算API

URL:http://cpubmed.openi.org.cn/graph/similarity

接口调用参数
调用API需要向接口发送以下字段来访问服务。

字段名	类型	含义	必填	备注
ent1	text	实体词	True	用于计算相似度的实体词
ent2	text	实体词	True	用于计算相似度的实体词
sign	text	密钥	True	每个账号一个独有的密钥
返回结果
字段名	类型	含义	备注
score	float	相似度距离	距离越小，相似度越大，距离最小为0。

示例
    接口调用
      
      http://cpubmed.openi.org.cn/graph/similarity?
      &ent1=心脏病&ent2=糖尿病
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
    返回结果
        45.75966703459426

---
8. 获取疾病相关辅助检查项 API

应用地址：
http://120.24.161.253:8586/graph/auxiliary-tests
接口调用方法
使用 POST 方法进行调用。

接口调用参数
字段名	类型	含义	必填	备注
diseases	JSON Array of Strings	疾病名称列表	True	必须为 JSON 数组格式，例如：["糖尿病", "高血压"]
sign	text	密钥	True	每个账号一个独有的密钥
返回结果
字段名	类型	含义	备注
[疾病名]	List of Strings	对应疾病的相关辅助检查项	键为标准化后的疾病名，值为其关联的检查项列表
示例请求（推荐方式）
POST http://120.24.161.253:8586/graph/auxiliary-tests
Content-Type: application/json

{
  "diseases": ["糖尿病", "高血压"],
  "sign": "your_signature_here"
}
示例响应
{
    "糖尿病": ["眼底检查", "神经传导速度"],
    "高血压": ["心脏超声", "肾功能检测"]
}

---

## 备注
- 网站符合协议 CC BY-ND 4.0
https://creativecommons.org/licenses/by-nd/4.0/

- 网站主地址：https://cpubmed.openi.org.cn/graphwiki

- 网站有关信息：
联系邮箱：qingcai.chen@hit.edu.cn
CPubMed-KG
CPubMed-KG由中国中文信息学会医疗健康与生物信息处理专业委员会、语言与知识计算专委会医疗知识图谱专业组、深圳计算机学会人工智能专委会发起，哈尔滨工业大学（深圳）联合国内高水平医疗机构，在中华医学会高质量全文期刊数据支持下，所构建的大规模中文开放医学知识图谱及开放式医学知识在线协同构建平台，旨在通过完全开放、协作的机制来打破中文医学知识的瓶颈，支撑智慧医疗技术的发展。

项目负责人
陈清财，哈工大（深圳）
项目策划
马婷，哈工大（深圳）
相洋，鹏城实验室
知识图谱构建
朱田恬，哈工大（深圳）
陈静，哈工大（深圳）
李东方，哈工大（深圳）
户保田，哈工大（深圳）
陈俊杰，哈工大（深圳）
刘欣，哈工大（深圳）、鹏城实验室
知识图谱开放平台构建
陈俊颖，哈工大（深圳）
周文秀，哈工大（深圳）
褚达文，哈工大（深圳）

- 知识图谱全数据：
内科22
外科19
妇产科3
小儿科12
生殖医学科1
骨科4
耳鼻喉科2
眼科2
口腔科5
皮肤性病科2
肿瘤科4
精神病科4
康复医学科2
介入科1
急诊科6
中医科1
疼痛科1
烧伤科1
专病1
罕见病1

---

## 写在最后：
- 参考GitHub上仓库的上传下载指南后，建议在本地先建立origin分支（-m选项）与main主支（-M选项），后使用`git push -u origin main`（也可以使用其他名称）。