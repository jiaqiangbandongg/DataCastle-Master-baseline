# -*- coding: utf-8 -*-

import os
from collections import defaultdict

#把网络文件都列出来
networks = os.listdir('networks')
with open('submission_baseline.csv','w') as out:
    out.write('NetID,nodeID1,nodeID2,nodeID3,nodeID4,nodeID5,nodeID6,nodeID7,nodeID8,nodeID9,nodeID10,nodeID11,nodeID12,nodeID13,nodeID14,nodeID15,nodeID16,nodeID17,nodeID18,nodeID19,nodeID20,nodeID21,nodeID22,nodeID23,nodeID24,nodeID25,nodeID26,nodeID27,nodeID28,nodeID29,nodeID30,nodeID31,nodeID32,nodeID33,nodeID34,nodeID35,nodeID36,nodeID37,nodeID38,nodeID39,nodeID40,nodeID41,nodeID42,nodeID43,nodeID44,nodeID45,nodeID46,nodeID47,nodeID48,nodeID49,nodeID50,nodeID51,nodeID52,nodeID53,nodeID54,nodeID55,nodeID56,nodeID57,nodeID58,nodeID59,nodeID60,nodeID61,nodeID62,nodeID63,nodeID64,nodeID65,nodeID66,nodeID67,nodeID68,nodeID69,nodeID70,nodeID71,nodeID72,nodeID73,nodeID74,nodeID75,nodeID76,nodeID77,nodeID78,nodeID79,nodeID80,nodeID81,nodeID82,nodeID83,nodeID84,nodeID85,nodeID86,nodeID87,nodeID88,nodeID89,nodeID90,nodeID91,nodeID92,nodeID93,nodeID94,nodeID95,nodeID96,nodeID97,nodeID98,nodeID99,nodeID100,nodeID101,nodeID102,nodeID103,nodeID104,nodeID105,nodeID106,nodeID107,nodeID108,nodeID109,nodeID110,nodeID111,nodeID112,nodeID113,nodeID114,nodeID115,nodeID116,nodeID117,nodeID118,nodeID119,nodeID120,nodeID121,nodeID122,nodeID123,nodeID124,nodeID125,nodeID126,nodeID127,nodeID128,nodeID129,nodeID130,nodeID131,nodeID132,nodeID133,nodeID134,nodeID135,nodeID136,nodeID137,nodeID138,nodeID139,nodeID140,nodeID141,nodeID142,nodeID143,nodeID144,nodeID145,nodeID146,nodeID147,nodeID148,nodeID149,nodeID150,nodeID151,nodeID152,nodeID153,nodeID154,nodeID155,nodeID156,nodeID157,nodeID158,nodeID159,nodeID160,nodeID161,nodeID162,nodeID163,nodeID164,nodeID165,nodeID166,nodeID167,nodeID168,nodeID169,nodeID170,nodeID171,nodeID172,nodeID173,nodeID174,nodeID175,nodeID176,nodeID177,nodeID178,nodeID179,nodeID180,nodeID181,nodeID182,nodeID183,nodeID184,nodeID185,nodeID186,nodeID187,nodeID188,nodeID189,nodeID190,nodeID191,nodeID192,nodeID193,nodeID194,nodeID195,nodeID196,nodeID197,nodeID198,nodeID199,nodeID200,nodeID201,nodeID202,nodeID203,nodeID204,nodeID205,nodeID206,nodeID207,nodeID208,nodeID209,nodeID210,nodeID211,nodeID212,nodeID213,nodeID214,nodeID215,nodeID216,nodeID217,nodeID218,nodeID219,nodeID220,nodeID221,nodeID222,nodeID223,nodeID224,nodeID225,nodeID226,nodeID227,nodeID228,nodeID229,nodeID230,nodeID231,nodeID232,nodeID233,nodeID234,nodeID235,nodeID236,nodeID237,nodeID238,nodeID239,nodeID240,nodeID241,nodeID242,nodeID243,nodeID244,nodeID245,nodeID246,nodeID247,nodeID248,nodeID249,nodeID250,nodeID251,nodeID252,nodeID253,nodeID254,nodeID255,nodeID256,nodeID257,nodeID258,nodeID259,nodeID260,nodeID261,nodeID262,nodeID263,nodeID264,nodeID265,nodeID266,nodeID267,nodeID268,nodeID269,nodeID270,nodeID271,nodeID272,nodeID273,nodeID274,nodeID275,nodeID276,nodeID277,nodeID278,nodeID279,nodeID280,nodeID281,nodeID282,nodeID283,nodeID284,nodeID285,nodeID286,nodeID287,nodeID288,nodeID289,nodeID290,nodeID291,nodeID292,nodeID293,nodeID294,nodeID295,nodeID296,nodeID297,nodeID298,nodeID299,nodeID300,nodeID301,nodeID302,nodeID303,nodeID304,nodeID305,nodeID306,nodeID307,nodeID308,nodeID309,nodeID310,nodeID311,nodeID312,nodeID313,nodeID314,nodeID315,nodeID316,nodeID317,nodeID318,nodeID319,nodeID320,nodeID321,nodeID322,nodeID323,nodeID324,nodeID325,nodeID326,nodeID327,nodeID328,nodeID329,nodeID330,nodeID331,nodeID332,nodeID333,nodeID334,nodeID335,nodeID336,nodeID337,nodeID338,nodeID339,nodeID340,nodeID341,nodeID342,nodeID343,nodeID344,nodeID345,nodeID346,nodeID347,nodeID348,nodeID349,nodeID350,nodeID351,nodeID352,nodeID353,nodeID354,nodeID355,nodeID356,nodeID357,nodeID358,nodeID359,nodeID360,nodeID361,nodeID362,nodeID363,nodeID364,nodeID365,nodeID366,nodeID367,nodeID368,nodeID369,nodeID370,nodeID371,nodeID372,nodeID373,nodeID374,nodeID375,nodeID376,nodeID377,nodeID378,nodeID379,nodeID380,nodeID381,nodeID382,nodeID383,nodeID384,nodeID385,nodeID386,nodeID387,nodeID388,nodeID389,nodeID390,nodeID391,nodeID392,nodeID393,nodeID394,nodeID395,nodeID396,nodeID397,nodeID398,nodeID399,nodeID400,nodeID401,nodeID402,nodeID403,nodeID404,nodeID405,nodeID406,nodeID407,nodeID408,nodeID409,nodeID410,nodeID411,nodeID412,nodeID413,nodeID414,nodeID415,nodeID416,nodeID417,nodeID418,nodeID419,nodeID420,nodeID421,nodeID422,nodeID423,nodeID424,nodeID425,nodeID426,nodeID427,nodeID428,nodeID429,nodeID430,nodeID431,nodeID432,nodeID433,nodeID434,nodeID435,nodeID436,nodeID437,nodeID438,nodeID439,nodeID440,nodeID441,nodeID442,nodeID443,nodeID444,nodeID445,nodeID446,nodeID447,nodeID448,nodeID449,nodeID450,nodeID451,nodeID452,nodeID453,nodeID454,nodeID455,nodeID456,nodeID457,nodeID458,nodeID459,nodeID460,nodeID461,nodeID462,nodeID463,nodeID464,nodeID465,nodeID466,nodeID467,nodeID468,nodeID469,nodeID470,nodeID471,nodeID472,nodeID473,nodeID474,nodeID475,nodeID476,nodeID477,nodeID478,nodeID479,nodeID480,nodeID481,nodeID482,nodeID483,nodeID484,nodeID485,nodeID486,nodeID487,nodeID488,nodeID489,nodeID490,nodeID491,nodeID492,nodeID493,nodeID494,nodeID495,nodeID496,nodeID497,nodeID498,nodeID499,nodeID500')
    
    for network in networks:
        print(network)
        
        #准备一个计数器 把每个点出现次数都统计下来
        counter = defaultdict(lambda :0)
        
        with open('networks/%s'%network) as f:
            for line in f.readlines():
                a,b = line.strip().split(',')
                counter[a] += 1
                counter[b] += 1
        
        #出现次数多的排前面
        counter = [a[0] for a in sorted(counter.items(),key=lambda x:x[1],reverse=True)]
        network = network.split('.')[0]
    
    
        #直接按照格式输出答案吧
        for i,v in enumerate(counter):
            
            if i%500==0:
                out.write('\n'+network+','+v)
            else:
                out.write(','+v)
        t = i%500
        for i in range(t,499):
            out.write(',')
        