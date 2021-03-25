
# colors_file = None

# try:
#     colors_file = open("colors.txt", "r")


#     # colors_content = colors_file.read()
#     # print(colors_content)

#     for color in colors_file:
#         print(color.rstrip())


# except IOError as exc:
#     print(exc)

# finally:
#     if colors_file:
#         colors_file.close()



try:
    with open("colors.txt", "r") as colors_file:

        # colors_content = colors_file.read()
        # print(colors_content)

        for color in colors_file:
            print(color.rstrip())

except IOError as exc:
    print(exc)

finally:
    print("I always run.")
