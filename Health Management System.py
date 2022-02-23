def getdate():
    import datetime
    return datetime.datetime.now()


def harry_info():
    print("1.Diet\n2.Exercise")
    harry = int(input("Choose any one for Harry: "))
    print("1.Log\n2.Retrieve")
    info = int(input("Choose any one: "))
    if harry == 1 and info == 1:
        log_diet = input("Enter today's diet:\n") + "\n" + str(getdate()) + "\n"
        harry_diet_log = open("harry-diet.txt", "a")
        today_diet = harry_diet_log.write(log_diet)
        harry_diet_log.close()
        return today_diet
    elif harry == 2 and info == 1:
        log_exercise = input("Enter today's Exercise:\n") + "\n" + str(getdate()) + "\n"
        harry_exercise_log = open("harry-exercise.txt", "a")
        today_exercise = harry_exercise_log.write(log_exercise)
        harry_exercise_log.close()
        return today_exercise
    elif harry == 1 and info == 2:
        ret_diet = open("harry-diet.txt", "r")
        read_diet = ret_diet.read()
        return read_diet
    elif harry == 2 and info == 2:
        ret_exercise = open("harry-exercise.txt", "r")
        read_exercise = ret_exercise.read()
        return read_exercise


def hammad_info():
    print("1.Diet\n2.Exercise")
    hammad = int(input("Choose any one for Hammad: "))
    print("1.Log\n2.Retrieve")
    info = int(input("Choose any one: "))
    if hammad == 1 and info == 1:
        log_diet = input("Enter today's diet:\n") + "\n" + str(getdate()) + "\n"
        hammad_diet_log = open("hammad-diet.txt", "a")
        today_diet = hammad_diet_log.write(log_diet)
        hammad_diet_log.close()
        return today_diet
    elif hammad == 2 and info == 1:
        log_exercise = input("Enter today's Exercise:\n") + "\n" + str(getdate()) + "\n"
        hammad_exercise_log = open("hammad-exercise.txt", "a")
        today_exercise = hammad_exercise_log.write(log_exercise)
        hammad_exercise_log.close()
        return today_exercise
    elif hammad == 1 and info == 2:
        ret_diet = open("hammad-diet.txt", "r")
        read_diet = ret_diet.read()
        return read_diet
    elif hammad == 2 and info == 2:
        ret_exercise = open("hammad-exercise.txt", "r")
        read_exercise = ret_exercise.read()
        return read_exercise


def rohan_info():
    print("1.Diet\n2.Exercise")
    rohan = int(input("Choose any one for Rohan: "))
    print("1.Log\n2.Retrieve")
    info = int(input("Choose any one: "))
    if rohan == 1 and info == 1:
        log_diet = input("Enter today's diet:\n") + "\n" + str(getdate()) + "\n"
        rohan_diet_log = open("rohan-diet.txt", "a")
        today_diet = rohan_diet_log.write(log_diet)
        rohan_diet_log.close()
        return today_diet
    elif rohan == 2 and info == 1:
        log_exercise = input("Enter today's Exercise:\n") + "\n" + str(getdate()) + "\n"
        rohan_exercise_log = open("rohan-exercise.txt", "a")
        today_exercise = rohan_exercise_log.write(log_exercise)
        rohan_exercise_log.close()
        return today_exercise
    elif rohan == 1 and info == 2:
        ret_diet = open("rohan-diet.txt", "r")
        read_diet = ret_diet.read()
        return read_diet
    elif rohan == 2 and info == 2:
        ret_exercise = open("rohan-exercise.txt", "r")
        read_exercise = ret_exercise.read()
        return read_exercise


def client_name():
    print("1.Harry\n2.Hammad\n3.Rohan")
    client_num = int(input("Choose any number: "))
    if client_num == 1:
        return harry_info()
    if client_num == 2:
        return hammad_info()
    if client_num == 3:
        return rohan_info()
    else:
        return "Error! Please Try Again"


health_management_system = client_name()
print(health_management_system)
