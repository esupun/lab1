import logging

logging.basicConfig(filename="logging.log",level=logging.INFO)


def main():
        with open('hosts.txt') as f:
              lines = f.readlines()
            
    


if __name__ == "__main__":
    main()