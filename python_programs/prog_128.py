'''
Write a function to shortlist words that are longer than n from a given list of words.
'''

def shortListWords(n: int, words: list[str]) -> list[str]:
    '''
    Takes n and list of words as input and filter out the words whose length are longer than n
        Parameters:
            n(int): An integer
            words(list): list of words
        Returns:
            Filtered list with words whose lenght are more that n
        Raises:
            TypeError: if n is not a integer or words is not a list or empty
    '''
    if not list:
        raise Exception("list of words's can't be empty")
    if not isinstance(n, int) or not isinstance(words, list):
        raise TypeError
    filtered = list(filter(lambda x : len(x)> n, words))
    return filtered

if __name__ == "__main__":
    words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honey",
    "island", "jungle", "kite", "lemon", "mango", "nectar", "ocean", "pebble",
    "quartz", "river", "sunset", "thunder", "umbrella", "valley", "willow",
    "xylophone", "yacht", "zephyr", "mountain", "forest", "desert", "glacier",
    "volcano", "meadow", "canyon", "waterfall", "horizon", "galaxy", "comet",
    "asteroid", "nebula", "orbit", "rocket", "satellite", "signal", "network",
    "circuit", "engine", "turbine", "battery", "sensor", "robot", "algorithm",
    "dataset", "variable", "function", "object", "class", "module", "package",
    "script", "console", "terminal", "keyboard", "monitor", "speaker", "camera",
    "lens", "pixel", "vector", "matrix", "scalar", "equation", "theorem",
    "proof", "logic", "reason", "memory", "storage", "cloud", "server",
    "client", "protocol", "packet", "router", "switch", "firewall",
    "encryption", "security", "privacy", "identity", "access", "permission",
    "policy", "audit", "backup", "recovery", "archive", "version", "release",
    "update", "deploy"
    ]
    
    try:
        print(shortListWords(5,words))
    except TypeError as e:
        print("Error: ", e)
        print("first parameter should be integer and second should be list and list can't be empty")
    except Exception as e:
        print(e)