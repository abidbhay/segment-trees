def main():
    arr= [1,3,5,7,9,11]
    n= len(arr)
    seg=[0]*4*n
    build(arr, seg, 0, n-1, 0)
    print(seg)

def build(arr,seg,s,e,node):
    if s==e:
        seg[node]=arr[s]
        return
    mid=s+(e-s)//2
    build(arr,seg,s,mid,node*2+1)
    build(arr,seg,mid+1,e,node*2+2)
    seg[node]=seg[node*2+1]+seg[node*2+2]
    return
  

if __name__=="__main__":
    main()