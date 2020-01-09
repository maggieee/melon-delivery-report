def create_delivery_report(day, file): # create a function that takes parameters day and file
    print(day) # print the day
    the_file = open(file) # create a file object out of the file
    for line in the_file: # for each line in the file
        line = line.rstrip() # remove the whitespace from the right
        words = line.split('|') # create a list out of the words in the line, splitting on the |

        melon = words[0] # create a variable melon and set the first word in the list to melon
        count = words[1] # create a variable count and set the second word in the list to count
        amount = words[2] # create a variable amount and set the third word in the list to amount

        print("Delivered {} {}s for total of ${}".format( 
            count, melon, amount)) # print out a line of the delivery report in a nice format
    the_file.close() # when all the lines have been iterated through, close the file


create_delivery_report("Day 1", "um-deliveries-20140519.txt") # do this for day 1

create_delivery_report("Day 2", "um-deliveries-20140520.txt") # do this for day 2

create_delivery_report("Day 3", "um-deliveries-20140521.txt") # do this for day 3

# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
