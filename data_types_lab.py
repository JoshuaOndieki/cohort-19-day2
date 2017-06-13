#data types lab

def data_type(inputs):
    type_of_input = type(inputs)
    if type_of_input == str:
        return len(inputs)
    elif type_of_input == bool:
        return inputs
    elif type_of_input == int:
        if inputs < 100:
            return "less than 100"
        elif inputs == 100:
            return "equal to 100"
        else:
            return "more than 100"
    elif type_of_input == list:
        if len(inputs) < 3:
            return None
        else:
            return inputs[2]
    else:
        return "no value"