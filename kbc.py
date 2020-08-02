question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]

i=0
while i<len(question_list):
    print('\n')
    print ("Aapka sawal hai:")
    print (question_list[i])
    print('\n')
    print ("Aapke options hai:")
    j=0
    while j<len(options_list[i]):
        print (str(j+1)+".",options_list[i][j])
        j=j+1

    user = int(input("enter a no. or life line 5050 :"))
    if user == 5050:
        print ("Aapke options hai:")
        options_5050=[
            ["Nine","seven"],
            ["chennai","Delhi"],
            ["Software Engineering","Tourism"]]
        j=0
        while j<len(options_5050[i]):
            print (str(j+1)+".",options_5050[i][j])
            j=j+1
        solution_5050=[2,2,1]
        user=int(input("enter a no."))
        if user==solution_5050[i]:
            print ("Congrats! Aapka answer sahi hai")
        else:
            print ("Sadly aapka javab galat hai.")
            break
    elif user==solution_list[i]:
        
        print ("Congrats! Aapka answer sahi hai")
    else:
        print ("Sadly aapka javab galat hai.")
        break
    i=i+1