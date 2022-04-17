import dev

if __name__ == '__main__':
    f = open("E:\AmesomeCloud\Blog2Me"+"\\blog\\beifen.txt","rb")
    out = dev.getNumStr(dev.bytes2str(f),"<br>",6)
    print(out)