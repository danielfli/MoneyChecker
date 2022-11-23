import sys
import argparse
import json
# import backend.comdirectapi

from backend import comdirectapi

# if args.pos_arg > 10:
#     parser.error("pos_arg cannot be larger than 10")


# print("Argument values:")
# print(args.pos_arg)
# print(args.opt_pos_arg)
# print(args.opt_arg)
# print(args.switch)
  
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def afcn(str):
      print("Der String: " + str.name)



def main():
    print("python main function")
    
    comdirectapi.apifcn()



if __name__ == '__main__':
    main()