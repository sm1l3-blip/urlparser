if __name__ == "__main__":
    
    try:
        fileName = raw_input("Dosya konumu : ")
        f = open(fileName, "r")

        f2 = open("output.html","w+")

        sayac = 0
        while True:
            sayac += 1
            line = f.readline()
            line = line.replace(" ","")
            line = line.replace("\n","")
            if not line:
                break
            f2.writelines("<h2>"+str(sayac)+"</h2><br>\n")
            f2.writelines("<iframe src=\""+line+ "\"></iframe><br>\n")


       

    except:
        print("Dosya Bulunamadi :'(")