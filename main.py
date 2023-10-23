
def process_data(path: str):
    """En funktion som läser in data från en fil och returnerar tidpunkten för datan samt resten av datan i form av en lista.

    Args:
        path (str): Platsen filen ligger på.

    Returns:
        time_info (str): Data om tidpunkt för temperaturerna
        temperatures(list[int]): Lista med samtliga temperaturer för månaden
    """
    with open() as f:
        time_info = ""
        temperatures = []

    return time_info, temperatures

def assignment(temperatures: list[int]):
    """Tar datan från listan temperatures och tar fram det högsta och det lägsta värdet samt medelvärdet och returnerar dessa.

    Args:
        temperatures (list[int]): Lista med temperaturer.

    Returns:
        mean (float): Medelvärdet av temperaturerna
        max_value (int): Maximala värdet av temperaturerna
        min_value (int): Minsta värdet av temperaturerna
    """
    mean: float = 0.0
    max_value: int = 0
    min_value: int = 0
    
    return mean, max_value, min_value

def main():
    pass

if __name__ == "__main__":
    main()
