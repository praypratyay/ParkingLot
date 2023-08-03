from abc import abstractmethod

class FeesCalculatorStrategy:

    @abstractmethod
    def calculateFees():
        pass

class EASYFeesCalculatorStrategy(FeesCalculatorStrategy):

    def calculateFees():
        return 0
    
class HARDFeesCalculatorStrategy(FeesCalculatorStrategy):

    def calculateFees():
        return 0

class MEDFeesCalculatorStrategy(FeesCalculatorStrategy):

    def calculateFees():
        return 0