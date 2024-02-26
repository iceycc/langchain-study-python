##

```md
请按照如下方式回答问题，直到我输入结束：
请你按照<think> <action> <result> 这几个步骤，一步一步思考，并回 答我提出的问题 

其中
<think> 表示你对我的问题进行思考，并判断是否需要进行更多的 <think>步骤，如果需要就进入到<think>环节，否则进入<final> 环节， 给出最终答案，并结束本轮对话。 
<action> 表示对某一个或几个<plugin>的使用，可用全部插件可以在 <plugin list>里看到。 
<result> 调用<plugin>后返回的结果 

--- 
<plugin list>
plugin1 : date， 用途: 返回当前日期 
plugin2 : city, 用途: 返回当前城市 
---

下面是一个示例： 
客户问题：今天星期几？ 
--- 
<think> 我需要知道今天是几月几日？ 
<action> date 
<result> 当前日期2023年5月28日
<think> 我知道今天的日期了。 
<final> 今天是星期日
```