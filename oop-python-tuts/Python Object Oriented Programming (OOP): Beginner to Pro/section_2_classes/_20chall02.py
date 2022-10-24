#? python standard library 
from string import ascii_letters, punctuation
from random import choices
from copy import copy

class Password:
    """A password of customize strength and length.

    Encapsulate a randomly generate password depending on the user-specified strength and length, where the latter
    is optional and automatically set depending on the strength (low -> 8, mid -> 12, high -> 16). If a length is
    user-specified these presets are overridden regardless of the strength.

    :param strength: a measure of the password's effectiveness against brute-force guessing
    :type strength: str, optional

    :param length: the length of the password
    :type length: int, optional
    """
    #* 2. CLASS VARIABLES - INPUT_UNIVERSE & DEFAULT_LENGTHS
    #! THIS IS MUTABLE  
    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

    # print(INPUT_UNIVERSE["numbers"])
    # print(INPUT_UNIVERSE["letters"])
    # print(INPUT_UNIVERSE["punctuation"])

    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }

    #* 3. defined as a class method as it is not specific to the instance
    @classmethod
    def show_input_universe(cls):
        """Return the complete input universe from which characters are sampled

        :return: The universe of characters from which random sampling is done to generate passwords
        :rtype: dict (of list-s)
        """
        return cls.INPUT_UNIVERSE

    #* 1. 
    def __init__(self, strength="mid", length=None):
        """Constructor method"""
        self.strength = strength
        self.length = length

        # the generate function is called after initialisation and the field self.password is generated. 
        self._generate()


    #* 4. underscore indicates that this is only for class use, not users to call method
    def _generate(self):
        """Generates the password according to the strength and length specified at initialization

        :return: the randomly generated password
        :rtype: str
        """
        #* population is the variable that is populated with depending upon the password strength chosen
        #! population = self.INPUT_UNIVERSE["letters"] - points to a place in memory, if we then change that, we'd change what is stored in that location in memory. 
        #? here we use copy to prevent the mutation of the class variable 
        # everytime we create a new instance, we create a new copy - which can be manipulated. 
        population = copy(self.INPUT_UNIVERSE["letters"])
        #? if user specifies a length at instantiation, use that.
        #* if not, use the default.
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
        else:
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))
        # random.choices - take a number of random options from a list - specify using k=num
        #? join an array into a string = "".join() 
        #* get a 4 random letters from ascii_letters 
        # "".join(choices(list(ascii_letters), k=4)) - #* this will give us 4 random letters
        #todo - HOWEVER, we still need to be able to add numbers and punctuation in. 
        #! # "".join(choices(list(range(10)), k=4)) - if we try to do this with num 0-9, we have a problem. The string join function, cannot join int to string, we need to turn int to string, then join. 
        #? we could do - list(map(lamda x: str(x), choices(list(ascii_letters) + list(range(10)), k=4)) )
        # then join 
        #* "".join(list(map(lamda x: str(x), choices(list(ascii_letters) + list(range(10)), k=4)) )) 
        # or probably better ... 
        #* "".join(list(map(str, choices(list(ascii_letters) + list(range(10)), k=4)))) - swap ascii_letters for population 




if __name__ == "__main__":
    #? here we're just 'testing' our code, in lieu of actual tests
    p_weak = Password(strength="low")
    print("Weak password: " + p_weak.password)

    p_mid = Password(strength="mid", length=40)
    print("Mid password: " + p_mid.password)

    p_high = Password(strength="high")
    print("High password: " + p_high.password)

    p_default = Password()
    print("Default password: " + p_default.password)
