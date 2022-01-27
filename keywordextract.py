import yake
def keywordextract(doctext1,doctext2):
    kw_extractor = yake.KeywordExtractor()
    language = "en"
    max_ngram_size = 1
    # deduplication_threshold = 0.8
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, top=numOfKeywords, features=None)
    keywords1 = custom_kw_extractor.extract_keywords(doctext1)
    keywords2 = custom_kw_extractor.extract_keywords(doctext2)
    
    list3=[]
    list4=[]

    for i in range(len(keywords1)):
        for j in range(len(keywords1[i])):
            if(j==0):
                list3.append(keywords1[i][j])

    print(list3)

    for i in range(len(keywords2)):
        for j in range(len(keywords2[i])):
            if(j==0):
                list4.append(keywords2[i][j])
    
    print(list4)

    list5 = list(set(list3)&set(list4))
    return list5
