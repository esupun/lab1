import logging

logging.basicConfig(filename="logging.log",level=logging.INFO)


def main():
    with open('hosts.txt') as f:
        lines = f.readlines()
            
    for line in lines:
        print(f"lines are  {line}")    

    print("trust no one")

if __name__ == "__main__":
    main()