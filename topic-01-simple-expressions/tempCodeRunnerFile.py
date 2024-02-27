if ast["tag"] == "negate":
        operand = evaluate(ast["right"])
        return -operand
    