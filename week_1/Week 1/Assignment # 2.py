
def no_of_input():
    take_input = int(input("How many records you want to enter : "))
    return take_input


def taking_record(input_no):
    record = []
    for j in range(input_no):
        dict = {}
        for i in range(1):
            dict['Roll#'] = input("Enter Roll# : ")
            dict['Name'] = input("Enter Name : ")
            dict['Age'] = int(input("Enter Age : "))
            dict['Marks(out of 100)'] = int(input("Enter Marks(out of 100) : "))
            print('\n\n')
        record.append(dict)
    return record

def show_record(l_record):
    print("Roll# | Name | Age | Marks out of hundred")
    for item in l_record:
        for value in item.values():
            print(value, end=' | ')
                  
def main():
    total_record = no_of_input()
    print(f"Enter {total_record} student record in the following.")
    list_record = taking_record(total_record)
    show_record(list_record)
    
if __name__ == '__main__':
    main()
