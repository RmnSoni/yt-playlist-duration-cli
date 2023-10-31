def retrieve_pl_id(url):

    sub1 = "list="
    sub2 = "&"

    idx1 = url.find(sub1)
    if idx1 ==-1 :
        idx1=0

    idx2 = url[idx1:].find(sub2)
    if idx2==-1:
        idx2=len(url)
    else:
        idx2+=idx1
    
    # print(idx1,idx2)

    pl_id = url[idx1 + len(sub1)  : idx2]
    # print("The extracted string : " + pl_id)
    return pl_id
