def prime_no(num):
    prime=True
    if num<2:
        prime=False
    else:
        for i in range(2,num):
            if num%i==0:
                prime=False

    return prime

if __name__=="__main__":
    num=4

    isPrime=prime_no(num)

    if isPrime:
        print(num, "is a prime no")
    else:
        print(num, "is not a prime no")
