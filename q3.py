def breakingrecords(scores):
    count=maxc=0
    score=minc=scores[0]
    for i in range(1,len(scores)):
        if score<scores[i]:
            score=scores[i]
            count+=1
        elif minc>scores[i]:
            minc=scores[i]
            maxc+=1
    return count,maxc