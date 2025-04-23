##############################
#Author: Colter Frank
#Class: CI690 Cyber Security Graduate Project
#Version: 1.0
#Released: 4/23/2025
##############################

repeat = 1
while(repeat == 1):
    print("\n\nThis is the query generator for my SOC Operational Management Bot!\n\n")
    test = int(input("Provide a choice of testing mode(1) or demonstration mode(0).  "))

    if (test == 1):
        orgSize = "medium sized"
        orgIndustry = "aviation"
        orgService = "flight instruction"
        appsUsed = "self-hosted management system to pair up certified flight instructors with flight trainees"
        appHosting = "hybrid environment with both cloud and on-premises services"
        orgEmployeeCountAndType = "5 full-time"
        orgEmployeeWorkFormat = "they work from in office and from home"
        orgWorkDevice = "company issued devices"
        orgInternetAccess = "their own internet connections"
        socEmployeeLevels = "4 unskilled IT employees that do traige and one skilled on con senior SOC analyst"
        socToolType = "open source"
        socTools = "the Security Onion Suite"
        socDetectors = "on-premise networking equipment and any company issued devices"
    elif (test == 0):
        orgSize = input("What is the size of your organization? ")
        orgIndustry = input("What industry is your organization operating within? ")
        orgService = input ("What does your company provide to its customers? ")
        appsUsed = input ("What applications enable your service to be provided? ")
        appHosting = input("What kind of environment is your application hosted in (on-premises, cloud, hybrid)? ")
        orgEmployeeCountAndType = input("How many employees do you currently have working to what extent (full time, part time, etc...)? ")
        orgEmployeeWorkFormat = input("Where do your organizations employees work from? ")
        orgWorkDevice = input("What do your employees use to conduct work related activities? ")
        orgInternetAccess = input("How do your employees access the internet to conduct work related activities (vpn services, their own networks, etc...)? ")
        socEmployeeLevels = input("What size is the security operations center and what variations of employee’s are there (senior analysts, skilled analysts, unskilled analysts)? ")
        socToolType = input("What form of security tools do you use (paid, open source, custom, or a variety)? ")
        socTools = input("What are those tools being used? ")
        socDetectors = input("Where are the detectors for these tools installed? ")
    else:
        print("Invalid input.\n")
    
    gen = 1
    additionalContext = ""
    while (gen != 0):
        if(gen == 1):
            additionalContext = str(input("Please enter any additional context not covered by the questions here (leave blank to just generate query)  "))
            print("Following is the query that was generated: \n\n")
            print("\n\n\nI want a list of suggested changes to make to my", orgSize, orgIndustry, "organization's security operations center to reduce alarm fatigue through organizational restructuring.\n")
            print("Each of these changes should be given in prioritized order based off the expected results.\n")
            print("For each suggestion give the specific change that should be made, why it would be an improvement over the current infrastructure, and a cost analysis between it and the previous solution.\n")
            print("Return the top 3 suggestions.\n")
            print("Verify that this solution has been proven beyond information on vendor websites or any affiliated companies to avoid biased solutions.\n\n--\n")
            print("For context this company provides", orgService, "to paid customers using a", appsUsed+".")
            print("These services are hosted in a", appHosting, "for different aspects of the data.")
            print("We have around", orgEmployeeCountAndType, "who wor", orgEmployeeWorkFormat, "using", orgWorkDevice+".")
            print("Currently our security operations center consists of", socEmployeeLevels+".")
            print("All security implementations are", socToolType, "using", socTools, "and installed on all", socDetectors+".")
            print("Begin extra context section (ingore if blank):", additionalContext)
            #This code will continue seeing if they want to continue generating the query with additional context.
            gen = int(input("\n\n\n\n\nYou query can be pasted from above, would you like to add additional context(1) or proceed back to the main program(0)?  "))
        elif(gen != 1 or 0):
            gen = int(input("\n\nInvalid of unrecognized input, please respond with proper input to add additional context(1) or proceed back to the main program(0)?  "))


    repeat = int(input("\n\nDo you want to continue(1)or exit(0) the program?  "))