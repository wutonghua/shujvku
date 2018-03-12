#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import jieba
import re
ignoring_words = ['【','“','、', '】','.',' ','。' ,'！','？','，','：',',','\xa0','?','0','1','2','3','4','5','6','7','8','9','�','；','（','）','”']
def clean_text(text):
    text = jieba.lcut(text.strip().replace(r'^[a-zA-Z]', ''))

    words = [w for w in text if w not in ignoring_words]
    return ' ' .join(words)
import pandas as pd
df=pd.read_csv('分词数据.csv', encoding='gbk')
df['clean-text']=df.zhenduan.apply(clean_text)
print(df['clean-text'].head())
m=df['clean-text']
with open('yujv1.csv','w') as f1:
    for line in m:
        # print(line)
        f1.write(line+ '\n')

# shujvfile=pd.read_csv('分词数据.csv',encoding='gbk')
# print(shujvfile.head())
# yujv = shujvfile.iloc[:, 0].astype('str')
# print(yujv[:2])
# cw = lambda x: ' '.join(jieba.cut(x))
# shujvfile['zhenduan1'] = yujv.apply(cw)


# def preprocessing(sen):
#     res = []
#     for words in sen:
#         for word in words:
#             if word not in ignoring_words:
#                 res.append(word)
#     return res
# # X_zhenduan = shujvfile['zhenduan1']
# zhenduan1 = [preprocessing(x) for x in ren]
# # X_zhenduan.to_csv('yujv2.csv', sep=',', header=True, index=True)
# with open('yujv5.csv','w') as f1:
#     for line in zhenduan1:
#         # print(line)
#         f1.write(str(line)+ '\n')
# # import pynlpir
# # pynlpir.open()
# # # s='      你好，孩子摇头耸肩频繁眨眼斜视撅嘴说污言秽语等症状是抽动症的表现，出现这些情况需要去医院进一步检查。抽动症的发生与颅脑结构或中枢神经递质失衡有关，也跟家庭环境有关，长期的受惊吓焦虑，不良的家庭环境都可能诱发抽动症，长时间看电视也会诱发抽动症的发生。经常摇头抖动还要注意是不是缺钙需要化验微量元素,      病情分析：,      考虑是过度的精神压力紧张或者缺锌引起的现象，建议到医院检查下微量元素根据情况改善。,      指导意见：,      铅中毒也会有这类的症状，最好是检查后根据情况进行合理的改善和调节饮食注意牛奶的摄入。,      病情分析：,      你好，根据你描述的情况，你应该问问女儿，这是不是跟别人学的一种坏习惯。,      指导意见：,      你好，看到女儿有不好的习惯，你就应该，给女儿讲清道理，让女儿纠正。平时应该多和女儿沟通。,      以上是对“女儿最近老耸鼻，而且较为频繁，昨晚开始又”这个问题的建议，希望对您有帮助，祝您健康！,      病情分析：,      你好，孩子出现上述情况属于不自主的运动，和过度的紧张感冒等有关。,      指导意见：,      建议你带宝宝到医院耳鼻喉科就医，根据医生的嘱咐选用合适的检查和治疗方法。,      病情分析：,      你好，根据你描述的情况，孩子这种情况可能是肺热引起的。,      指导意见：,      这个季节比较干燥，给孩子多吃水果蔬菜，多饮水，可用冰糖雪梨，润肺，可以有效地缓解这种症状,      病情分析：,      多动症。特发于儿童学前时期，活动量多是明显症状。注意缺陷障碍是多动、注意力不集中、参与事件能力差，伴认知障碍和学习困难。,      指导意见：,      一般需要精神治疗，药物治疗是对症的。动作过多往往经药物治疗而得到控制。结合家庭教育。'
#
#
# # segments=pynlpir.segment(s)
# # for segment in segments:
# # 	print(segment[0], '\t', segment[1])
# # pynlpir.close()
# # import jieba
# # s=' '.join(jieba.cut(s))
# print(s)