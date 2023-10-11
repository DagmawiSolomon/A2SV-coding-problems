if __name__ == '__main__':
    N = int(input())

    def func(N):
        my_list = []
        for i in range(N):
            commands = input()
            commands_split = commands.split(" ")
            if commands_split[0] == "insert":
                my_list.insert(int(commands_split[1]), int(commands_split[2]))
            if commands_split[0] == "print":
                print(my_list)
            if commands_split[0] == "remove":
                my_list.remove(int(commands_split[1]))
            if commands_split[0] == "append":
                my_list.append(int(commands_split[1]))
            if commands_split[0] == "sort":
                my_list.sort()
            if commands_split[0] == "pop":
                my_list.pop()
            if commands_split[0] == "reverse":
                my_list.reverse()
        return my_list

    func(N)
