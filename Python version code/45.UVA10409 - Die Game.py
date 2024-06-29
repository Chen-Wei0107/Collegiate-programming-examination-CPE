while True:
    try:
        top=1
        button=7-top
        north=2
        south=7-north
        west=3
        east=7-west
        n=int(input())
        if n==0:break
        for _ in range(n):
            a=input().strip()
            if a=='east': #往東滾:東=上 ;上=西 ; 西=7-東 ;下=7-上
                east=top
                top=west
                west=7-east
                button=7-top
                
            elif  a=='west': #往西滾 底=西 ; 西=上 ; 上=7-底 ; 東=7-西
                button=west
                west=top
                top=7-button
                east=7-west
                
            elif  a=='north': #往北滾 底=北 ; 北=上 ; 上=7-底 ; 南=7-北
                button=north
                north=top
                top=7-button
                south=7-north
                
            else :#south #往南滾 南=上 ; 上=北 ; 北=7-南 ; 下=7-上
                south=top
                top=north
                north=7-south
                button=7-top
                
        print(top)
    except:
        break