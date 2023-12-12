k=input("Az idő (1),a sebesség (2) vagy a megtett út (3) hiányzik?")
if k==1:
    m=int(input("Kérem méterben a megtett távolságot."))
    v=int(input("Kérem a sebességet m/s-ban."))
    print("idő=",m//v)
elif k==2:
    m=int(input("Kérem méterben a megtett távolságot."))
    t=int(input("Kérem az időt mp-ben")) 
    print("Sebesség=",m//t)
elif k==3:
    v=int(input("Kérem a sebességet m/s-ban."))
    t=int(input("Kérem az időt mp-ben")) 
    print("A megtett út=",v*t)


    
