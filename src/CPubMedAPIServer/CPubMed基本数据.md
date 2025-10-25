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

1.实体关联三元组API：
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
2.三元组信息详细搜索

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
3.医学类辅助分词

URL:http://cpubmed.openi.org.cn/graph/cut

params: query(text),sign(text)

return keys: cut_result(array)



---

4.三元组匹配：
URL:http://cpubmed.openi.org.cn/graph/match

params: query(text),sign(text)

return keys:match_result(array)

三元组格式：[ID,头实体,关系,尾实体]

（意义；头实体与尾实体有关联，ID是三元组的ID）

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

5.医学文献检索API

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
6.查找实体之间的三元组路径
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
7.相似度计算API

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
8.获取疾病相关辅助检查项 API
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
9. 获取实体具体关系详细信息API
应用地址：
http://cpubmed.openi.org.cn/graph/triple-sp
接口调用参数
调用API需要向接口发送以下字段来访问服务。

字段名	类型	含义	必填	备注
header	text	头实体名称	True	支持模糊匹配最接近实体
relation	text	关系类型	True	实体间的特定关系
sign	text	密钥	True	每个账号一个独有的密钥
返回结果
字段名	类型	含义	备注
header	text	头实体名称	查询的实体名称
relation	text	关系类型	查询的关系类型
triples	Array	三元组详细信息	包含尾实体和来源信息的数组
end_entity	text	尾实体名称	三元组中的尾实体
triple_id	text	三元组ID	唯一标识符
source	Object	来源信息	包含文献详细信息的对象
返回示例
{
                        "header": "库欣病",
                        "relation": "病理分型",
                        "triples": [
                          {
                            "end_entity": "微腺瘤",
                            "source": {
                              "triple_id": "3602323",
                              "doc_id": "2735201",
                              "text": "方法回顾性分析本院1985年～1996年76例库欣病患者,其中包括大腺瘤患者12例和微腺瘤患者64例."
                            }
                          },
                          {
                            "end_entity": "大腺瘤",
                            "source": {
                              "triple_id": "3602324",
                              "doc_id": "2735201",
                              "text": "方法回顾性分析本院1985年～1996年76例库欣病患者,其中包括大腺瘤患者12例和微腺瘤患者64例."
                            }
                          },
                          {
                            "end_entity": "未缓解组",
                            "source": {
                              "triple_id": "10649957",
                              "doc_id": "41631167",
                              "text": "根据术后血皮质醇水平将208例库欣病患者分为内分泌早期缓解组(简称早期缓解组,143例)和未缓解组(65例)."
                            }
                          }
                        ]
                      }
---
10. 获取相近的实体词API
应用地址：
http://cpubmed.openi.org.cn/graph/similar-entity
接口调用参数
调用API需要向接口发送以下字段来访问服务。

字段名	类型	含义	必填	备注
entity	text	实体词	True	获取与该实体接近的实体词列表
sign	text	密钥	True	每个账号一个独有的密钥
返回结果
字段名	类型	含义	备注
entities	array	实体列表	[实体1，实体2，...]
示例
    接口调用
      
      http://cpubmed.openi.org.cn/graph/similar-entity?
      entity=心脏病
      &sign=b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d      
    返回结果
        [ "心脏病", "无心脏病", "心脏疾病", "肺心脏病", "心脏病变" ]
---

## 实际操作备注
1. 使用HTTPS方法访问，但是放弃审查，同时放弃使用通用UserAgent

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