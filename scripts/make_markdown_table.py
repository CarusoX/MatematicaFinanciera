def make_markdown_table(array):
    """ Input: Python list with rows of table as lists
               First element as header. 
        Output: String to put into a .md file 

    Ex Input: 
        [["Name", "Age", "Height"],
         [":-:", ":-", "-:"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]] 
    """
    markdown = ""
    for entry in array:
        markdown += "| " + " | ".join(map(str, entry)) + "|\n"

    return markdown
