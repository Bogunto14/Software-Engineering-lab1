def fahToCel(fah):
    cel = 5.0*(fah - 32) / 9
    return cel

def celToFah(cel):
    fah = (9/5.0 * cel) + 32
    return fah

def main():
    while True:
        cmd = input("Write F to convert from fahrenheit to celsius, or C to convert from celsius to fahrenheit: \n")
        if cmd == "F":
            while True:
                try:    
                    fah = float(input("°F = "))
                    print("°C = ",fahToCel(fah))
                    break
                except Exception:
                    print("Enter the number!")
                
        elif cmd == "C":
            while True:
                try:
                    cel = float(input("°C = "))
                    print("°F = ",celToFah(cel))
                    break
                except Exception:
                    print("Enter the number!")  
            
        elif cmd == "Exit":
            break
if __name__ == '__main__':
    main()       

    
