

def printLabel(symbol:str, width:int, height:int):
    if len(symbol) != 1:
        raise Exception("Symbol should be only one character")
    
    if width <= 2 or height <=2:
        raise Exception("Width and/or Height should have a min value of 2")
    
    header_footer = symbol * width
    filler = ' ' * (width - 2)
    
    print(header_footer)
    
    for _ in range(height - 2):
        print(symbol + filler + symbol)
        
    print(header_footer)
    
if __name__ == '__main__':
    symbol = input("Enter symbol (1 char): ")
    width = int(input("Enter width (min: 2): "))
    height = int(input("Enter height (min: 2):"))
    
    printLabel(symbol, width, height)