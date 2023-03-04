class base_n_counter:
    """
    A class for converting integers to and from base-n representation.

    """

    def __init__(self, BASE: int, LENGTH: int) -> None:
        """
        Initialize the base-n counter.

        """
        self.base = BASE
        self.max_number = BASE - 1
        self.bit = LENGTH
        self.max_possible_value = (self.base**(self.bit))
        self.zero_number = tuple([0 for _ in range(self.bit)])

    def convert_to_base(self, value: int) -> tuple:
        """
        Convert an integer to base-n representation.
        more info : https://math.libretexts.org/Courses/College_of_the_Canyons/Math_130%3A_Math_for_Elementary_School_Teachers_(Lagusker)/02%3A_Empathy_and_Primary_Mathematics/2.06%3A_Converting_Between_(our)_Base_10_and_Any_Other_Base_(and_vice_versa)#:~:text=To%20convert%20any%20number%20in,the%20algorithm%20will%20not%20work.&text=Keep%20dividing%20by%205%2C%20until%20your%20quotient%20is%20zero.&text=Now%20write%20your%20remainders%20backwards!
        """
        number = []
        if value > self.max_possible_value:
            raise Exception(
                f'given number is bigger than avalible space ({self.max_possible_value}))')

        while value != 0:
            quotient = value // self.base
            reminder = value % self.base
            number.append(reminder)
            value = quotient

        if len(number) < self.bit:
            tmp = []

            for _ in range(self.bit - len(number)):
                tmp.append(0)

            tmp += number[::-1]
            number = tmp
            return tuple(number)

        return tuple(number[::-1])

    def convert_to_base_10(self, number: tuple) -> int:
        """
        Convert a base-n representation to an integer.

        """
        if len(number) != self.bit:
            raise Exception(
                f'Invalid input : input number should have {self.bit} elements in tuple')

        tmp = 0
        tmp_lsd = list(number)[::-1]

        for i in range(self.bit):
            tmp += tmp_lsd[i]*(self.base)**i

        return tmp
