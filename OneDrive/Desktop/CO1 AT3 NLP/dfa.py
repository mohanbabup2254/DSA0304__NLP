# DFA Simulator for strings ending with "ab"

def dfa_simulator(input_string):
    # States: q0 (start), q1, q2 (final)
    state = "q0"
    transition_path = ["q0"]

    for char in input_string:
        if state == "q0":
            if char == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if char == 'a':
                state = "q1"
            elif char == 'b':
                state = "q2"

        elif state == "q2":
            if char == 'a':
                state = "q1"
            else:
                state = "q0"

        transition_path.append(state)

    # Output
    print("\nTransition Path:")
    print(" -> ".join(transition_path))

    if state == "q2":
        print("Accepted")
    else:
        print("Rejected")


# Main
if __name__ == "__main__":
    string = input("Enter input string: ")
    dfa_simulator(string)