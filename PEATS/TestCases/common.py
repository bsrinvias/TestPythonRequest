Browsers = {1: "Microsoft Edge", 2: "Chrome", 3: "Mozilla"}

# FMO ='http://10.253.219.247/(S(rswe3lysuhmxuncceaa2blq4))/home.aspx'
# CMO = ' http://10.253.219.247/(S(rswe3lysuhmxuncceaa2blq4))/home.aspx'
Environments = {"FMO": "abc", "CMO": "bcd"}


# Classes
def get_env():
    while True:
        try:
            test_environment = input("Enter Environments [FMO/CMO] :")
            print(Environments.get(test_environment))

        except ValueError:
            print("This is not a valid environment")
            continue
        else:
            break
   # return test_environment


env1 = get_env()


#print(Environments.get(env1))
