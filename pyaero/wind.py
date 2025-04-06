import numpy as np

class Wind():
    """
    Class of wind object, can be initialize with zero argument.
    """
    def __init__(self, **kw) -> None:
        """
        Write something here
        """
        self.__keys = {}
        self.__keys.update(kw)

    def units(self, value):
        return self.__keys['units'] = value

    def size(self, value):
        return self.__keys['size'] = value

    def aero_force(self, speed: float, angle: float) -> float:
        """
        Return aero force of the
        """

        aero_coef = np.max(
          self.drag_coef * np.cos(angle) 
          - self.lift_coef * np.sin(angle))

        return 1 / 2 * aero_coef * 1.2 * self.units * self.size * speed ** 2
