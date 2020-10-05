class operations:
    def add(op1, op2):
        if isinstance(op1, float) and isinstance(op2, float):
            return f'fadd float {op1}, {op2}'
        elif isinstance(op1, int) and isinstance(op2, int):
            return f'add i32 {op1}, {op2}'
        
    def sub(op1, op2):
        if isinstance(op1, float) and isinstance(op2, float):
            return f'fsub float {op1}, {op2}'
        elif isinstance(op1, int) and isinstance(op2, int):
            return f'sub i32 {op1}, {op2}'
        
    def mul(op1, op2):
        if isinstance(op1, float) and isinstance(op2, float):
            return f'fmul float {op1}, {op2}'
        elif isinstance(op1, int) and isinstance(op2, int):
            return f'mul i32 {op1}, {op2}'
        
    def div(op1, op2):
        if isinstance(op1, float) and isinstance(op2, float):
            return f'fdiv float {op1}, {op2}'
        elif isinstance(op1, int) and isinstance(op2, int):
            return f'sdiv i32 {op1}, {op2}'
