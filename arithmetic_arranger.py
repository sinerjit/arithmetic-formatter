def arithmetic_arranger(problems, val=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row, bottom_row, dashes, solutions = '', '', '', ''

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        top_row += operand1.rjust(width) + ' ' * 4
        bottom_row += operator + operand2.rjust(width - 1) + ' ' * 4
        dashes += '-' * width + '    '
        solutions += str(eval(problem)).rjust(width) + ' ' * 4

    arranged_problems = '\n'.join((top_row.rstrip(), bottom_row.rstrip(), dashes.rstrip()))
    if val:
        arranged_problems += '\n' + solutions.rstrip()

    return arranged_problems

