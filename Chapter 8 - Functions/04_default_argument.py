def goodDay(name, ending ="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Sanjit")
goodDay("Ram", "Thanks")

# if the value of ending is not supplied then the default value will be printed.
# Here on first function call, value of ending is not supplied 
# But on second function call, value for ending is supplied