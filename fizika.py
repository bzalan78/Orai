k=int(input("Az idő (1),a sebesség (2) vagy a megtett út (3) hiányzik? "))
l=1
h=2
j=3
if k==l:
    m=int(input("Kérem méterben a megtett távolságot. "))
    v=int(input("Kérem a sebességet m/s-ban. "))
    print("idő =",m//v,"mp")
elif k==h:
    m=int(input("Kérem méterben a megtett távolságot. "))
    t=int(input("Kérem az időt mp-ben. ")) 
    print("Sebesség =",m//t,"m/s")
elif k==j:
    v=int(input("Kérem a sebességet m/s-ban. "))
    t=int(input("Kérem az időt mp-ben. ")) 
    print("A megtett út =",v*t,"m")


    
