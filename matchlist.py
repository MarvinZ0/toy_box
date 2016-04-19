# -*- coding: utf-8 -*-


class FuzzyMatch(object):
    def __init__(self):
        object.__init__(self)

    email_list = ["kenneth_lay@enron.net",
                "kenneth_lay@enron.com",
                "klay.enron@enron.com",
                ]

    def trie_tree(self,word,keys):
        """生成单词组合字典...暂不使用"""
        l=len(word)
        if word == "":
            return "Done"
        else:
            keys.update({word:{word[0:l-1]:{},word[1:l]:{}}})


    def fragment_word(self,word):
        """分段输入字符串 生成包含两个元素的列表"""
        if len(word)==2:
            return None
        return [word[0:len(word)-1],word[1:len(word)]]


    def extract_Data(self,content,regex="(\@.*)|([^a-z]+)"):
        import re
        """提取有效片段"""
        # regex = (\@.*)|([^a-z]+) 提取内容中@开头的部分和非小写字母部分
        p =re.sub(regex,"",content)
        return p


    def match_rank(self,word,data,oringinal_size):
        import re
        import math
        """返回rank值"""
        if re.search(word,data):
            return 1-(-(len(word)/oringinal_size)*math.log((len(word)/oringinal_size),2))
        else:
            keys = self.fragment_word(word)
            if keys == None:
                return 0
            else:
                branch_1 = self.match_rank(keys[0],data,oringinal_size+2)
                branch_2 = self.match_rank(keys[1],data,oringinal_size+2)
                return branch_1 if branch_1 else branch_2 if branch_2 else 0

    def fuzzy_match(self,word="jeff",listdata=email_list):
        """返回匹配结果字典"""
        from time import time
        result = {}
        t_start = time()
        for list in listdata:
            list_extract = self.extract_Data(list)
            result.update({list:round(self.match_rank(word,list_extract,float(len(word))),2)})
        result = sorted(result.iteritems(), key=lambda d:d[1], reverse=True) # 对字典的value值排序
        t_end = round(time()-t_start,2)
        return result, t_end

    def pretty_print(self,dic,time):
        for key, value in dic:
            if value >= 0.5 :
                print 'Key : ',key,'        ','Value :',value
        print "It takes %s s for matching"%t_end
        return 'Done'



