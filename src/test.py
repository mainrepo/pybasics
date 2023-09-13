""" from itertools import permutations

def all_permutations(input_str):
    # Generate all permutations of the input string
    perms = permutations(input_str)
    
    # Iterate through the permutations and print each one
    for perm in perms:
        print(''.join(perm))

# Input string
input_string = input("Enter a string: ")

print("All permutations of the string:")
all_permutations(input_string) """


from reportlab.pdfgen import canvas

def generate_report(event, context):
    # Create a PDF report
    xpos, ypos = 85, 800
    c = canvas.Canvas("/tmp/report.pdf")
    c.drawString(xpos, ypos, "Sample Report")

    ypos = ypos - 20
    c.drawString(xpos, ypos, "This is a sample PDF report generated by AWS Lambda.")
    
    ypos = ypos - 15
    c.drawString(xpos, ypos, "This is a second sample PDF report generated by AWS Lambda.")
    c.save()

    # Return the path to the generated report
    return "/tmp/report.pdf"

if '__main__' == __name__:
    report = generate_report(None, None)
    print(report)