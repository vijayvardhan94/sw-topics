
#this prints main
#print("This prints from module1:{}".format(__name__))
def main():
    print("The module's name is:{}".format(__name__))
    
if __name__ == "__main__":
    main()