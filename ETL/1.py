if __name__ == '__main__':
    t=1602820800000
    tt=86400000
    for i in range(1,18):
        count=0
        for j in range(0,(i*5-(i-1)*5)):
            if count<=2:
                count=count+1
                print(str(count)+"---1----"+str(t+tt*i))
            else:
                count=count+1
                print(str(count)+"---2-----"+str(t+tt*i))