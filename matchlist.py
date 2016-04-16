# -*- coding: utf-8 -*-


class FuzzyMatch(object):
    def __init__(self):
        object.__init__(self)

    email_list = ["kenneth_lay@enron.net",
                "kenneth_lay@enron.com",
                "klay.enron@enron.com",
                "kenneth.lay@enron.com",
                "klay@enron.com",
                "layk@enron.com",
                "chairman.ken@enron.com",
                "jeffreyskilling@yahoo.com",
                "jeff_skilling@enron.com",
                "jskilling@enron.com",
                "effrey.skilling@enron.com",
                "skilling@enron.com",
                "jeffrey.k.skilling@enron.com",
                "jeff.skilling@enron.com",
                "kevin_a_howard.enronxgate.enron@enron.net",
                "kevin.howard@enron.com",
                "kevin.howard@enron.net",
                "kevin.howard@gcm.com",
                "michael.krautz@enron.com"
                "scott.yeager@enron.com",
                "syeager@fyi-net.com",
                "scott_yeager@enron.net",
                "syeager@flash.net",
                "joe'.'hirko@enron.com",
                "joe.hirko@enron.com",
                "rex.shelby@enron.com",
                "rex.shelby@enron.nt",
                "rex_shelby@enron.net",
                "jbrown@enron.com",
                "james.brown@enron.com",
                "rick.causey@enron.com",
                "richard.causey@enron.com",
                "rcausey@enron.com",
                "calger@enron.com",
                "chris.calger@enron.com",
                "christopher.calger@enron.com",
                "ccalger@enron.com",
                "tim_despain.enronxgate.enron@enron.net",
                "tim.despain@enron.com",
                "kevin_hannon@enron.com",
                "kevin'.'hannon@enron.com",
                "kevin_hannon@enron.net",
                "kevin.hannon@enron.com",
                "mkoenig@enron.com",
                "mark.koenig@enron.com",
                "m..forney@enron.com",
                "ken'.'rice@enron.com",
                "ken.rice@enron.com",
                "ken_rice@enron.com",
                "ken_rice@enron.net",
                "paula.rieker@enron.com",
                "prieker@enron.com",
                "andrew.fastow@enron.com",
                "lfastow@pdq.net",
                "andrew.s.fastow@enron.com",
                "lfastow@pop.pdq.net",
                "andy.fastow@enron.com",
                "david.w.delainey@enron.com",
                "delainey.dave@enron.com",
                "'delainey@enron.com",
                "david.delainey@enron.com",
                "'david.delainey'@enron.com",
                "dave.delainey@enron.com",
                "delainey'.'david@enron.com",
                "ben.glisan@enron.com",
                "bglisan@enron.com",
                "ben_f_glisan@enron.com",
                "ben'.'glisan@enron.com",
                "jeff.richter@enron.com",
                "jrichter@nwlink.com",
                "lawrencelawyer@aol.com",
                "lawyer'.'larry@enron.com",
                "larry_lawyer@enron.com",
                "llawyer@enron.com",
                "larry.lawyer@enron.com",
                "lawrence.lawyer@enron.com",
                "tbelden@enron.com",
                "tim.belden@enron.com",
                "tim_belden@pgn.com",
                "tbelden@ect.enron.com",
                "michael.kopper@enron.com",
                "dave.duncan@enron.com",
                "dave.duncan@cipco.org",
                "duncan.dave@enron.com",
                "ray.bowen@enron.com",
                "raymond.bowen@enron.com",
                "'bowen@enron.com",
                "wes.colwell@enron.com",
                "dan.boyle@enron.com",
                "cloehr@enron.com",
                "chris.loehr@enron.com",
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
                branch_1 = self.match_rank(keys[0],data,oringinal_size)
                branch_2 = self.match_rank(keys[1],data,oringinal_size)
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
        return result, "It takes %s s for matching"%t_end

    def pretty_print(self,dic):
        for key, value in dic:
            if value >= 0.5 :
                print 'Key : ',key,'        ','Value :',value
        return 'Done'



