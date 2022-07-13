def return_band_name() -> str:
    return f'{input("Tell me name of city where you were born ")} {input("What was the name of your first pet? ")}'


def show_band_name()-> None:
    print(return_band_name())
    


show_band_name()