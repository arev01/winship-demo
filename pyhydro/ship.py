from pyhydro.physics import residual_resistance_coef, froude_number, reynolds_number, frictional_resistance_coef


class Ship:
    """
    Class of ship object, can be initialize with zero argument.
    """

    def __init__(self, **kw) -> None:
        """
        Assign values for the main dimension of a ship.

        :param displacement: cubic meters displacement :math:`CB*L*B*T` where CB is block coefficient of the ship,
            L is length of ship, B is beam of the ship, T is mean draft
        :param slenderness_coef: slenderness coefficient dimensionless :math:`L/(∇^{1/3})` where L is length of ship,
            ∇ is displacement
        :param prismatic_coef: prismatic coefficient dimensionless :math:`∇/(L\cdot A_m)` where L is length of ship,
            ∇ is displacement, Am is midsection area of the ship
        :param wetted_surface: square meters wetted surface area :math:`1.025*(1.7*L*T+∇/T)` where L is length of ship,
            T is mean draft, ∇ is displacement
        """
        self.__keys = {}
        self.__keys.update(kw)
        
        if "displacement" not in self.__keys and "block_coef" in self.__keys:
            self.displacement = self.block_coef * self.length * self.beam * self.draft
            
        if "slenderness_coef" not in self.__keys and "displacement" in self.__keys:
            self.slenderness_coef = self.length / self.displacement ** (1/3)

        if "prismatic_coef" not in self.__keys and "block_coef" in self.__keys and "midship_coef" in self.__keys:
            self.prismatic_coef = self.block_coef / self.midship_coef
            
        if "wetted_surface" not in self.__keys:
            self.wetted_surface = 1.025 * (1.7 * self.length * self.draft + self.displacement / self.draft)

    @property
    def length(self):
        return self.__keys["length"]

    @length.setter
    def length(self, value):
        self.__keys["length"] = value

    @property
    def beam(self):
        return self.__keys["beam"]

    @beam.setter
    def beam(self, value):
        self.__keys["beam"] = value

    @property
    def draft(self):
        return self.__keys["draft"]

    @draft.setter
    def draft(self, value):
        self.__keys["draft"] = value

    @property
    def height(self):
        return self.__keys["height"]

    @height.setter
    def height(self, value):
        self.__keys["height"] = value

    @property
    def speed(self):
        return self.__keys["speed"]

    @speed.setter
    def speed(self, value):
        self.__keys["speed"] = value

    @property
    def deadweight(self):
        return self.__keys["deadweight"]

    @deadweight.setter
    def deadweight(self, value):
        self.__keys["deadweight"] = value

    @property
    def gross_tonnage(self):
        return self.__keys["gross_tonnage"]

    @gross_tonnage.setter
    def gross_tonnage(self, value):
        self.__keys["gros_tonnage"] = value

    @property
    def block_coef(self):
        return self.__keys["block_coef"]

    @block_coef.setter
    def block_coef(self, value):
        self.__keys["block_coef"] = value

    @property
    def midship_coef(self):
        return self.__keys["midship_coef"]

    @midship_coef.setter
    def midship_coef(self, value):
        self.__keys["midship_coef"] = value

    def resistance(self) -> float:
        """
        Return resistance of the vehicle.

        :return: newton the resistance of the ship
        """
        total_resistance_coef = frictional_resistance_coef(self.length, self.speed) + \
                                residual_resistance_coef(self.slenderness_coef,
                                                         self.prismatic_coef,
                                                         froude_number(self.speed, self.length))
        return 1 / 2 * total_resistance_coef * 1025 * self.wetted_surface * self.speed ** 2

    def maximum_deck_area(self, water_plane_coef: float = 0.88) -> float:
        """
        Return the maximum deck area of the ship

        :param water_plane_coef: optional water plane coefficient
        :return: Area of the deck
        """
        return self.beam * self.length * water_plane_coef

    def reynold_number(self) -> float:
        """
        Return Reynold number of the ship

        :return: Reynold number of the ship
        """
        return reynolds_number(self.length, self.wetted_surface)

    def propulsion_power(self, propulsion_eff: float = 0.7, sea_margin: float = 0.2, external_force: float = 0.0) -> float:
        """
        Total propulsion power of the ship.

        :param propulsion_eff: Shaft efficiency of the ship
        :param sea_margin: Sea margin take account of interaction between ship and the sea, e.g. wind, wave
        :param external_force: External force acting on the ship
        :return: Watts shaft propulsion power of the ship
        """
        return ((1 + sea_margin) * self.resistance + external_force) * self.speed / propulsion_eff
