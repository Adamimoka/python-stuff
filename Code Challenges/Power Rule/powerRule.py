def powerRule(text_input: str) -> str:
    terms = text_input.split("+")
    out_terms = []
    for term in terms:
        if 'x' not in term:
            continue
        if '^' not in term:
            if term == 'x':
                out_terms.append('1')
            else:
                out_terms.append(term[:-1]) # all but the x (ex. 34x -> 34)
            continue
        left, right = term.split('x^')
        if left == '':
            left = 1
        left = int(left)
        right = int(right)
        out_left = left * right
        out_right = right - 1
        if out_right == 1:
            out_terms.append(f"{out_left}x")
        else:
            out_terms.append(f"{out_left}x^{out_right}")
    output = '+'.join(out_terms)
    
    if output == '':
        return '0'
    return output

if __name__ == "__main__":
    answer = powerRule(input("Enter an expression (ex. 5x^2+4x+2): "))
    print(answer)
