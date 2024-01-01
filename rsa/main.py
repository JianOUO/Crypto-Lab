import binascii
import gmpy2
import math

n=[]
e=[]
c=[]
m={zip(['Frame'+str(i) for i in range(0,21)],'')}
sloved={}
filename=['./frame/Frame'+str(i) for i in range(0,21)]
for i in range(0,21):
        f=open(filename[i],'r')
        data=f.read()
        #str->hex->int
        n.append(int(data[:256],16))
        e.append(int(data[256:512],16))
        c.append(int(data[512:],16))
"""
e_list = {}
for i, num in enumerate(e):
        if num in e_list:
            e_list[num].append(i)
        else:
            e_list[num] = [i]

for num, indices in e_list.items():
    print(f"{num} : {indices}")
"""

"""
for i  in range(0,21):
    for j in range(i+1,21):
        if n[i]==n[j]:
            print('n['+str(i)+']=='+'n['+str(j)+']')

for i in range(0,21):
        for j in range(i+1,21):
            if n[i]==n[j]:
                continue
            else:
                rem=math.gcd(n[i],n[j])
                if rem!=1:
                        print('gcd(n['+str(i)+'],n['+str(j)+']>1')
"""
def exgcd(a,b):
        if b==0:
                return 1,0,a
        else:
                x,y,r=exgcd(b,a%b)
                x,y=y,(x-(a//b)*y)
                return x,y,r

def same_mod_attack(n,e1,e2,c1,c2):
    x,y,r=exgcd(e1,e2)
    if x<0:
        x=-x;
        c1=gmpy2.invert(c1,n)
    elif y<0:
        y=-y;
        c2=gmpy2.invert(c2,n)
    m=pow(c1,x,n)*pow(c2,y,n)%n
    m=hex(m)[2:]
    m=binascii.unhexlify(m)[-8:]
    return m

def same_factor_attack():
        p_of_prime=gmpy2.gcd(n[1],n[18])
        q1=n[1]//p_of_prime
        q18=n[18]//p_of_prime
        phi1=(p_of_prime-1)*(q1-1)
        phi18=(p_of_prime-1)*(q18-1)
        d1=gmpy2.invert(e[1],phi1)
        d18=gmpy2.invert(e[18],phi18)
        m1=pow(c[1],d1,n[1])
        m18=pow(c[18],d18,n[18])
        m1=hex(m1)[2:]
        m18=hex(m18)[2:]
        m1=binascii.unhexlify(m1)[-8:]
        m18=binascii.unhexlify(m18)[-8:]
        sloved['Frame1']=m1
        sloved['Frame18']=m18

def chinese_remainder_theorem(backup):
        N=1
        for a,n in backup:
                N*=n
        Ni=[]
        for a,n in backup:
                Ni.append(N//n)
        Ni_inverse=[]
        for i in range(0,len(Ni)):
                Ni_inverse.append(gmpy2.invert(Ni[i],backup[i][1]))
        x=0
        for i in range(0,len(Ni)):
                x+=backup[i][0]*Ni[i]*Ni_inverse[i]
        x=x%N
        return x,N

def low_exponent_attack3():
        frame_range=[7,11,15]
        backup=[]
        for i in frame_range:
                backup.append([c[i],n[i]])
        x,N=chinese_remainder_theorem(backup)
        m=gmpy2.iroot(x,3)[0]
        m=hex(m)[2:]
        m=binascii.unhexlify(m)[-8:]
        sloved['Frame7']=m
        sloved['Frame11']=m
        sloved['Frame15']=m

def low_exponent_attack5():
        frame_range=[3,8,12,16,20]
        backup=[]
        for i in frame_range:
                backup.append([c[i],n[i]])
        x,N=chinese_remainder_theorem(backup)
        m=gmpy2.iroot(x,5)[0]
        m=hex(m)[2:]
        m=binascii.unhexlify(m)[-8:]
        sloved['Frame3']=m
        sloved['Frame8']=m
        sloved['Frame12']=m
        sloved['Frame16']=m
        sloved['Frame20']=m

def fermat_factorization(n):
        a=gmpy2.iroot(n,2)[0]+1
        max=200000
        for i in range(0,max):
                b2=a*a-n
                b=gmpy2.iroot(b2,2)[0]
                if gmpy2.is_square(b2):
                        p=a-b
                        q=a+b
                        return p,q
                a+=1
def fermat_data():
        frame_range=[10]
        for i in frame_range:
                p,q=fermat_factorization(n[i])
                phi=(p-1)*(q-1)
                d=gmpy2.invert(e[i],phi)
                m=pow(c[i],d,n[i])
                m=hex(m)[2:]
                m=binascii.unhexlify(m)[-8:]
                sloved['Frame'+str(i)]=m

def pollard_p_1(n):
        b=2**20
        a=2
        for i in range(2,b+1):
                a=gmpy2.powmod(a,i,n)
                d=gmpy2.gcd(a-1,n)
                if d!=1 and d!=n:
                        q=n//d
                        n=q*d
        return d
def pollard_data(n):
        frame_range=[2,6,19]
        for i in frame_range:
                temp_n=n[i]
                temp_c=c[i]
                temp_e=e[i]
                p=pollard_p_1(temp_n)
                q=temp_n//p
                phi=(p-1)*(q-1)
                d=gmpy2.invert(temp_e,phi)
                m=pow(temp_c,d,temp_n)
                m=hex(m)[2:]
                m=binascii.unhexlify(m)[-8:]
                sloved['Frame'+str(i)]=m

if __name__ == '__main__':
    for i in range(0,21):
        for j in range(i+1,21):
            if n[i]==n[j]:
                m2=same_mod_attack(n[i],e[i],e[j],c[i],c[j])
                sloved['Frame'+str(i)]=m2
                sloved['Frame'+str(j)]=m2 
    same_factor_attack()
    low_exponent_attack3()
    low_exponent_attack5()
    fermat_data()
    pollard_data(n)
    print(sloved)
