def createFrame(names):
    longest_name_num = len(max(names, key=len))
    frame = "*" * (longest_name_num + 4) + "\n"
    for i, name in enumerate(names):        
        frame += f"* {name}" + " " * (longest_name_num - len(name)) + " *\n"

    frame += "*" * (longest_name_num + 4)

    return frame

def main():
    print(createFrame(['midu', 'madeval', 'educalvolpz']))
    """***************
       * midu        *
       * madeval     *
       * educalvolpz *
       ***************"""

    print(createFrame(['midu']))
    """********
       * midu *
       ********"""

    print(createFrame(['a', 'bb', 'ccc']))
    """*******
       * a   *
       * bb  *
       * ccc *
       *******"""

    print(createFrame(['a', 'bb', 'ccc', 'dddd']))
    """********
       * a    *
       * bb   *
       * ccc  *
       * dddd *
       ********"""


if __name__ == "__main__":
    main()