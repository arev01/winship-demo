from pyresis.physics import residual_resistance_coef, froude_number, reynolds_number, frictional_resistance_coef


class Ship:
    """
    Class of ship object, can be initialize with zero argument.
    """

    def __init__(self, **kw) -> None:
        """
        Assign values for the main dimension of a ship.

        :param length: metres length of the vehicle
        :param draught: metres draught of the vehicle
        :param beam: metres beam of the vehicle
        :param speed: m/s speed of the vehicle
        :param slenderness_coef: slenderness coefficient dimensionless :math:`L/(∇^{1/3})` where L is length of ship,
            ∇ is displacement
        :param prismatic_coef: prismatic coefficient dimensionless :math:`∇/(L\cdot A_m)` where L is length of ship,
            ∇ is displacement Am is midsection area of the ship
        """
        self.__keys = {}
        self.__keys.update(kw)
        
        if "displacement" not in self.__keys and "block_coef" in self.__keys:
            self.displacement = self.block_coef * self.length * self.draft * self.beam
            
        if "slenderness_coef" not in self.__keys and "displacement" in self.__keys:
            self.slenderness_coef = self.length / self.displacement ** (1/3)

        if "prismatic_coef" not in self.__keys and "block_coef" in self.__keys and "midship_coef" in self.__keys:
            self.prismatic_coef = self.block_coef / self.midship_coef
            
        if "wetted_surface" not in self._keys:
            self.wetted_surface = 1.025 * (1.7 * self.length * self.draft + self.displacement / self.draft)

    @property
    def resistance(self, speed: float) -> float:
        """
        Return resistance of the vehicle.

        :return: newton the resistance of the ship
        """
        total_resistance_coef = frictional_resistance_coef(self.length, speed) + \
                                residual_resistance_coef(self.slenderness_coef,
                                                         self.prismatic_coef,
                                                         froude_number(speed, self.length))
        return 1 / 2 * total_resistance_coef * 1025 * self.wetted_surface * speed ** 2

    def maximum_deck_area(self, water_plane_coef: float = 0.88) -> float:
        """
        Return the maximum deck area of the ship

        :param water_plane_coef: optional water plane coefficient
        :return: Area of the deck
        """
        return self.beam * self.length * water_plane_coef

    @property
    def reynold_number(self) -> float:
        """
        Return Reynold number of the ship

        :return: Reynold number of the ship
        """
        return reynolds_number(self.length, self.wetted_surface)

    def propulsion_power(self, speed: float, propulsion_eff: float = 0.7, sea_margin: float = 0.2) -> float:
        """
        Total propulsion power of the ship.

        :param propulsion_eff: Shaft efficiency of the ship
        :param sea_margin: Sea margin take account of interaction between ship and the sea, e.g. wave
        :return: Watts shaft propulsion power of the ship
        """
        return (1 + sea_margin) * self.resistance * speed / propulsion_eff
