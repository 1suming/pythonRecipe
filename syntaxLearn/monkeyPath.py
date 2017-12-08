#coding=utf-8

def originalFunc():
    print("this is  original")

def modifiedFunc():
    print("this  is modified")

def main():
    originalFunc();

if __name__=="__main__":
    originalFunc=modifiedFunc
    main()

